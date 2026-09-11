"""Seed contract regressions. These do not establish Codex runtime compatibility.

Run: python -B -m unittest discover -s validators -p test_validate_structure.py
Fixtures are temporary copies; no project/user configuration is changed.
"""

import contextlib
import importlib.util
import io
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest import mock

SPEC = importlib.util.spec_from_file_location(
    "seed_validator", Path(__file__).with_name("validate_structure.py")
)
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)
SEED = validator.ROOT


class SeedContractTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="anti-code-contract-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "project"
        # Copy only required governance files, never application code, data,
        # caches, secrets, or a potentially enormous descendant project tree.
        self.root.mkdir()
        for rel in validator.REQUIRED_PATHS:
            source, target = SEED / rel, self.root / rel
            if source.is_file():
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source, target)
            elif source.is_dir():
                target.mkdir(parents=True, exist_ok=True)
        for rel in ("src", "tests", "validators", "docs", "outputs", ".agents/states"):
            (self.root / rel).mkdir(parents=True, exist_ok=True)
        patcher = mock.patch.object(validator, "ROOT", self.root)
        patcher.start()
        self.addCleanup(patcher.stop)

    def run_validator(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output), self.assertRaises(SystemExit) as result:
            validator.main()
        return result.exception.code, output.getvalue()

    def check_config_text(self, text):
        if validator.tomllib is None:
            self.skipTest("TOML parsing requires Python 3.11+")
        (self.root / ".codex/config.toml").write_text(text, encoding="utf-8")
        return self.run_validator()

    def assert_config_rejected(self, addition, message):
        original = (self.root / ".codex/config.toml").read_text(encoding="utf-8")
        code, output = self.check_config_text(addition + "\n" + original)
        self.assertEqual(code, 1, output)
        self.assertIn(message, output)

    def test_corrected_seed_passes(self):
        code, output = self.run_validator()
        self.assertEqual(code, 0, output)
        if validator.tomllib is not None:
            errors, config = validator.load_codex_config()
            self.assertEqual(errors, [])
            self.assertNotIn("approval_policy", config)

    def test_retired_policy_has_actionable_failure(self):
        self.assert_config_rejected('approval_policy = "untrusted"', "remove this setting")

    def test_other_explicit_policies_are_not_generic_seed_defaults(self):
        for value in ("on-request", "never", "on-failure", {"granular": {}}):
            with self.subTest(value=value):
                config = {
                    "approval_policy": value,
                    "sandbox_mode": "workspace-write",
                    "sandbox_workspace_write": {"network_access": False},
                }
                self.assertIn("must omit approval_policy", " ".join(validator.check_codex_config(config)))

    def test_table_policy_override_rejected(self):
        self.assert_config_rejected('approval_policy = { granular = {} }', "must omit approval_policy")

    def test_undocumented_key_rejected(self):
        self.assert_config_rejected('deny_list = ["rm"]', "outside the verified seed allowlist")

    def test_documented_but_out_of_contract_key_rejected(self):
        self.assert_config_rejected('model = "project-choice"', "not necessarily by Codex")

    def test_profile_cannot_hide_policy_override(self):
        self.assert_config_rejected('profiles = { custom = { approval_policy = "never" } }', "profiles")

    def test_sandbox_weakening_rejected(self):
        original = (self.root / ".codex/config.toml").read_text(encoding="utf-8")
        code, output = self.check_config_text(original.replace('sandbox_mode = "workspace-write"', 'sandbox_mode = "danger-full-access"'))
        self.assertEqual(code, 1, output)
        self.assertIn("must set sandbox_mode", output)

    def test_network_enabled_rejected(self):
        original = (self.root / ".codex/config.toml").read_text(encoding="utf-8")
        code, output = self.check_config_text(original.replace("network_access = false", "network_access = true"))
        self.assertEqual(code, 1, output)
        self.assertIn("network_access = false", output)

    def test_network_requires_explicit_boolean_false(self):
        for value in (None, 0, "false", True):
            with self.subTest(value=value):
                config = {"sandbox_mode": "workspace-write", "sandbox_workspace_write": {"network_access": value}}
                self.assertIn("network_access = false", " ".join(validator.check_codex_config(config)))

    def test_unknown_nested_key_rejected(self):
        original = (self.root / ".codex/config.toml").read_text(encoding="utf-8")
        code, output = self.check_config_text(original + '\nwritable_roots = ["../"]\n')
        self.assertEqual(code, 1, output)
        self.assertIn("outside the verified seed allowlist", output)

    def test_missing_sandbox_table_rejected(self):
        code, output = self.check_config_text('sandbox_mode = "workspace-write"\n')
        self.assertEqual(code, 1, output)
        self.assertIn("must define [sandbox_workspace_write]", output)

    def test_invalid_toml_fails(self):
        code, output = self.check_config_text("[broken\n")
        self.assertEqual(code, 1, output)
        self.assertIn("not valid TOML", output)

    def test_missing_config_still_fails_without_tomllib(self):
        (self.root / ".codex/config.toml").unlink()
        with mock.patch.object(validator, "tomllib", None):
            code, output = self.run_validator()
        self.assertEqual(code, 1, output)
        self.assertIn("Missing required path: .codex/config.toml", output)

    def test_each_boot_file_must_route_to_orientation(self):
        for rel in validator.BOOT_FILES:
            with self.subTest(rel=rel):
                path = self.root / rel
                original = path.read_text(encoding="utf-8")
                path.write_text(original.replace("ORIENTATION.md", "elsewhere.md"), encoding="utf-8")
                code, output = self.run_validator()
                self.assertEqual(code, 1, output)
                self.assertIn("does not point at .agents/ORIENTATION.md", output)
                path.write_text(original, encoding="utf-8")

    def test_registry_missing_engine_fails(self):
        path = self.root / ".agents/AGENT_REGISTRY.md"
        path.write_text(path.read_text(encoding="utf-8").replace("**CDX-01**", "**XXX-01**"), encoding="utf-8")
        code, output = self.run_validator()
        self.assertEqual(code, 1, output)
        self.assertIn("No permanent lead registered for engine 'CDX'", output)

    def test_registry_missing_parametric_slot_fails(self):
        path = self.root / ".agents/AGENT_REGISTRY.md"
        path.write_text(path.read_text(encoding="utf-8").replace("`CDX-02`", "`XXX-02`"), encoding="utf-8")
        code, output = self.run_validator()
        self.assertEqual(code, 1, output)
        self.assertIn("3 parametric slots", output)

    def test_dead_permission_path_fails(self):
        path = self.root / ".claude/settings.json"
        settings = json.loads(path.read_text(encoding="utf-8"))
        settings["permissions"]["allow"].append("Write(nonexistent-audit-target/**)")
        path.write_text(json.dumps(settings), encoding="utf-8")
        code, output = self.run_validator()
        self.assertEqual(code, 1, output)
        self.assertIn("path that doesn't exist", output)

    def test_each_existing_approval_gate_is_checked(self):
        _, settings = validator.load_claude_settings()
        for command in ("git commit", "git push", "rm"):
            with self.subTest(command=command):
                modified = json.loads(json.dumps(settings))
                modified["permissions"]["ask"] = [entry for entry in modified["permissions"]["ask"] if command not in entry]
                errors = validator.check_destructive_commands_gated(modified)
                self.assertTrue(any(f"does not gate '{command}'" in error for error in errors), errors)

    def test_invalid_claude_json_fails(self):
        (self.root / ".claude/settings.json").write_text("{", encoding="utf-8")
        code, output = self.run_validator()
        self.assertEqual(code, 1, output)
        self.assertIn("not valid JSON", output)

    def test_no_tomllib_is_unverified_but_does_not_abort_other_checks(self):
        with mock.patch.object(validator, "tomllib", None):
            code, output = self.run_validator()
            self.assertEqual(code, 2, output)
            self.assertIn("[UNVERIFIED]", output)
            self.assertNotIn("[SUCCESS]", output)
            self.assertIn("was NOT validated", output)
            (self.root / "CLAUDE.md").write_text("No boot routing", encoding="utf-8")
            code, output = self.run_validator()
        self.assertEqual(code, 1, output)
        self.assertNotIn("[SUCCESS]", output)
        self.assertIn("does not point at", output)

    def test_no_tomllib_and_invalid_json_reports_failure(self):
        (self.root / ".claude/settings.json").write_text("{", encoding="utf-8")
        with mock.patch.object(validator, "tomllib", None):
            code, output = self.run_validator()
        self.assertEqual(code, 1, output)
        self.assertIn("not valid JSON", output)
        self.assertNotIn("[SUCCESS]", output)

    def test_unparsed_retired_config_is_unverified_not_approved(self):
        path = self.root / ".codex/config.toml"
        path.write_text('approval_policy = "untrusted"\n' + path.read_text(encoding="utf-8"), encoding="utf-8")
        with mock.patch.object(validator, "tomllib", None):
            code, output = self.run_validator()
        self.assertEqual(code, 2, output)
        self.assertIn("[UNVERIFIED]", output)
        self.assertNotIn("[SUCCESS]", output)

    def test_parser_recovery_does_not_retain_incomplete_status(self):
        if validator.tomllib is None:
            self.skipTest("Parser recovery requires Python 3.11+")
        with mock.patch.object(validator, "tomllib", None):
            self.assertEqual(self.run_validator()[0], 2)
        code, output = self.run_validator()
        self.assertEqual(code, 0, output)
        self.assertNotIn("[UNVERIFIED]", output)

    def test_success_is_scoped_and_placeholders_remain_readiness_warnings(self):
        if validator.tomllib is None:
            self.skipTest("Verified seed requires Python 3.11+")
        code, output = self.run_validator()
        self.assertEqual(code, 0, output)
        self.assertIn("[WARN]", output)
        self.assertIn("implemented seed-contract checks", output)
        self.assertIn("are not certified", output)
        self.assertNotIn("All structural and semantic checks passed", output)

    def test_inspection_preserves_fixture_bytes_for_each_result(self):
        if validator.tomllib is None:
            self.skipTest("All three result states require Python 3.11+")
        def snapshot():
            return {p.relative_to(self.root): p.read_bytes()
                    for p in self.root.rglob("*") if p.is_file()}
        before = snapshot()
        self.assertEqual(self.run_validator()[0], 0)
        self.assertEqual(snapshot(), before)
        with mock.patch.object(validator, "tomllib", None):
            self.assertEqual(self.run_validator()[0], 2)
            self.assertEqual(snapshot(), before)
            (self.root / "CLAUDE.md").write_text("No boot routing", encoding="utf-8")
            before_failure = snapshot()
            self.assertEqual(self.run_validator()[0], 1)
            self.assertEqual(snapshot(), before_failure)


class RuntimeProbeSerializationTests(unittest.TestCase):
    """Check argument construction, not whether the application accepts it."""

    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location(
            "runtime_probe", Path(__file__).with_name("check_codex_runtime.py")
        )
        cls.probe = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.probe)

    def test_seed_values_use_unquoted_dotted_cli_keys(self):
        config = {"sandbox_mode": "workspace-write", "sandbox_workspace_write": {"network_access": False}}
        self.assertEqual(list(self.probe.overrides(config)), [
            'sandbox_mode="workspace-write"',
            "sandbox_workspace_write.network_access=false",
        ])

    def test_ambiguous_cli_keys_fail_instead_of_silently_quoting(self):
        with self.assertRaises(ValueError):
            list(self.probe.overrides({"sandbox.mode": "workspace-write"}))

    def test_unhandled_probe_value_fails(self):
        with self.assertRaises(ValueError):
            list(self.probe.overrides({"extra": ["unreviewed"]}))


if __name__ == "__main__":
    unittest.main()

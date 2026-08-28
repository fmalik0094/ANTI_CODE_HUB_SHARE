# WORKFLOW: 01_GENESIS_PROMPT

Run once, when the project is first seeded from ANTI_CODE-HUB.

1. Read `.agents/ORIENTATION.md` and fill in section 1 (what this project is).
2. Read `.agents/rules/global.md` and claim one role from `.agents/AGENT_REGISTRY.md`.
3. Define any parametric slots this project needs (`GEM-02` / `CDX-02` / `CLD-02`)
   in the registry — specialization **and** activation condition. Leave unused
   slots undefined rather than inventing roles.
4. Replace `[PROJECT]` / `[PROJECT NAME]` placeholders in `CLAUDE.md` and
   `ORIENTATION.md`.
5. Initialize `.state/BASELINE.md` with this project's path and purpose.
6. Verify layout: `python validators/validate_structure.py`.
7. Initialize git if not already: `git init`, first commit.
8. Hold for operator approval before mutating code.

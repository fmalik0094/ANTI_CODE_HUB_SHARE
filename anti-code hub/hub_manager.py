import os
import re
import shutil
import datetime

STATES_DIR = os.path.join(".agents", "states")
ARCHIVE_DIR = os.path.join(STATES_DIR, "archive")
INBOX_DIR = os.path.join(".agents", "inbox")
INDEX_FILE = os.path.join(STATES_DIR, "_ACTIVE_INDEX.md")

def ensure_dirs():
    os.makedirs(ARCHIVE_DIR, exist_ok=True)
    os.makedirs(INBOX_DIR, exist_ok=True)

def prune_states():
    """Archives old versions of state files, keeping only the absolute latest for each domain."""
    ensure_dirs()
    pattern = re.compile(r"^(.*)_V(\d+\.\d+)(_.*)?\.md$")
    files_by_domain = {}
    
    for filename in os.listdir(STATES_DIR):
        if not filename.endswith(".md"):
            continue
        filepath = os.path.join(STATES_DIR, filename)
        if not os.path.isfile(filepath):
            continue
            
        match = pattern.match(filename)
        if match:
            domain = match.group(1)
            try:
                # Parse as a (major, minor) tuple, NOT a float. float("1.10")
                # is 1.1, which sorts BELOW float("1.9") — that would archive
                # V1.10 as obsolete while keeping V1.9 as "latest truth",
                # silently destroying the newest state binary at version 10.
                major, minor = match.group(2).split(".")
                version = (int(major), int(minor))
            except ValueError:
                continue
                
            if domain not in files_by_domain:
                files_by_domain[domain] = []
            files_by_domain[domain].append((version, filename, filepath))

    archived_count = 0
    for domain, versions in files_by_domain.items():
        if len(versions) > 1:
            # Sort descending by version number
            versions.sort(key=lambda x: x[0], reverse=True)
            latest = versions[0]
            print(f"[*] {domain}: Keeping {latest[1]} as latest truth.")
            
            # Archive all older versions
            for v in versions[1:]:
                src = v[2]
                dst = os.path.join(ARCHIVE_DIR, v[1])
                shutil.move(src, dst)
                print(f"  -> Archived {v[1]}")
                archived_count += 1
                
    print(f"\n[+] Pruning complete. Successfully archived {archived_count} obsolete state files.")

# NOT IMPLEMENTED — deliberately not exposed on the CLI.
#
# Two commands ("bundle", "parse") previously existed here as stubs that
# printed "Not fully implemented yet" and then exited 0. Automation could call
# them, see success, and conclude a context bundle or inbox merge had happened
# when nothing had. A command that reports success without doing its work is
# worse than an absent one, so they are removed from the parser rather than
# left callable.
#
# If either is built later:
#   bundle_context(domain) -> read the entry protocol plus the latest state
#       binary and emit a single paste-ready block.
#   parse_inbox()          -> scan .agents/inbox/ for raw engine output,
#       extract markdown blocks, increment the domain version, write to
#       .agents/states/, and update _ACTIVE_INDEX.md atomically.
# Both must exit non-zero on failure and update _ACTIVE_INDEX.md in the same
# operation that moves a state file — see the prune note above.


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Anti-Code Hub state manager. Prunes superseded state "
                    "binaries into .agents/states/archive/."
    )
    parser.add_argument("command", choices=["prune"], help="Action to perform")

    args = parser.parse_args()
    if args.command == "prune":
        prune_states()

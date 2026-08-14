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
                version = float(match.group(2))
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

def bundle_context(domain_query):
    """
    (Alpha) Concept: Reads the Entry Protocol and the latest state file, 
    combining them so they are ready to be pasted into the Web UI.
    """
    ensure_dirs()
    print(f"[*] Preparing Context Bundle for: {domain_query} (Not fully implemented yet)")
    pass

def parse_inbox():
    """
    (Alpha) Concept: Scans .agents/inbox/ for raw Gemini output text, extracts markdown 
    code blocks, increments the domain version, saves to states/, and updates _ACTIVE_INDEX.md.
    """
    ensure_dirs()
    print("[*] Checking inbox for pending Web UI state merges... (Not fully implemented yet)")
    pass

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="TOPIC-HUB-ENGINE Meta-Vault Manager")
    parser.add_argument("command", choices=["prune", "bundle", "parse"], help="Action to perform")
    parser.add_argument("--domain", help="Domain name for bundling")
    
    args = parser.parse_args()
    if args.command == "prune":
        prune_states()
    elif args.command == "bundle":
        if not args.domain:
            print("[-] Error: --domain is required for bundling.")
        else:
            bundle_context(args.domain)
    elif args.command == "parse":
        parse_inbox()

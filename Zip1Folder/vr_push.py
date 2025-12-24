#!/usr/bin/env python3
import argparse, base64, os, subprocess, sys

def run(cmd):
    r = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    if r.returncode != 0:
        print(r.stdout)
        print(r.stderr, file=sys.stderr)
        sys.exit(r.returncode)
    return r.stdout.strip()

parser = argparse.ArgumentParser(description="Create/update a file from base64 and push to GitHub.")
parser.add_argument("--path", required=True, help="Path relative to repo root, e.g. web/accord/schema.yaml")
parser.add_argument("--message", required=True, help="Commit message")
parser.add_argument("--b64", required=True, help="Base64-encoded file content")
parser.add_argument("--branch", default="", help="Optional branch (defaults to current)")
args = parser.parse_args()

repo_root = run("git rev-parse --show-toplevel")
os.chdir(repo_root)

folder = os.path.dirname(args.path)
if folder and not os.path.exists(folder):
    os.makedirs(folder, exist_ok=True)

content = base64.b64decode(args.b64.encode("utf-8"))
with open(args.path, "wb") as f:
    f.write(content)

run(f'git add "{args.path}"')
branch = args.branch or run("git rev-parse --abbrev-ref HEAD")
run(f'git commit -m "{args.message}"')
run(f'git push origin "{branch}"')
print(f"✅ Pushed {args.path} to {branch}")

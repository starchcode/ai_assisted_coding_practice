#!/usr/bin/env python3
"""Guard for /ai_assist: blocks file edits outside the selected problem folder.

The selected folder is stored in .claude/ai_assist_scope.txt (written by the skill).
Always allowed: the scope file itself and about_me/what_to_improve.md (score updates).
"""
import json, os, re, shlex, sys

root = os.path.realpath(os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd())
scope_file = os.path.join(root, ".claude", "ai_assist_scope.txt")
always_ok = {os.path.realpath(scope_file),
             os.path.realpath(os.path.join(root, "about_me", "what_to_improve.md"))}
SAFE_PREFIXES = ("/usr/", "/bin/", "/opt/", "/dev/null", "/dev/stdout", "/dev/stderr")

def block(msg):
    print(f"/ai_assist guard: {msg}", file=sys.stderr)
    sys.exit(2)

data = json.load(sys.stdin)
tool = data.get("tool_name", "")
inp = data.get("tool_input", {}) or {}

scope = None
if os.path.exists(scope_file):
    rel = open(scope_file).read().strip()
    if rel:
        scope = os.path.realpath(os.path.join(root, rel))
        out = os.path.realpath(os.path.join(root, "output"))
        if not scope.startswith(out + os.sep):
            block("scope must be inside output/.")

def inside(p):
    p = os.path.realpath(os.path.join(root, os.path.expanduser(p)))
    return p in always_ok or (scope is not None and (p == scope or p.startswith(scope + os.sep)))

if tool in ("Edit", "Write", "NotebookEdit"):
    p = inp.get("file_path") or inp.get("notebook_path") or ""
    if not inside(p):
        block(f"edits are only allowed inside the selected problem folder"
              f"{' (' + os.path.relpath(scope, root) + ')' if scope else ' (none selected yet)'}. Blocked: {p}")

elif tool == "Bash":
    cmd = inp.get("command", "")
    if scope is None:
        block("no problem folder selected yet; pick one first.")
    try:
        tokens = shlex.split(cmd, comments=False, posix=True)
    except ValueError:
        tokens = cmd.split()
    for t in tokens:
        t = t.lstrip("<>")
        if not t or t.startswith("-") and "/" not in t:
            continue
        if t.startswith(("/", "~")) or ".." in t.split("/"):
            if t.startswith(SAFE_PREFIXES):
                continue
            if not inside(t) and not t.startswith(("-",)):
                block(f"command touches a path outside the selected folder: {t}")
sys.exit(0)

---
name: ai_assist
description: Help me solve one chosen practice problem from the output folder. Use when I type /ai_assist. Works only inside the selected problem folder.
hooks:
  PreToolUse:
    - matcher: "Edit|Write|NotebookEdit|Bash"
      hooks:
        - type: command
          command: "python3 \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/ai_assist_guard.py"
---

# /ai_assist

Works as my regular AI coding assistant on ONE problem that `/create_interview` built. Everything is scoped to the folder I pick.
A guard hook (`.claude/hooks/ai_assist_guard.py`) blocks edits outside the selected folder.

## Step 1 — Pick the problem
1. Clear any old scope: write an empty string to `.claude/ai_assist_scope.txt`.
2. **Path shortcut:** if I passed a relative path (e.g. `/ai_assist output/20261121_api_nodejs_1`) or paste one at any picker below (via "Other"), use it directly. It must be a folder inside `output/`; otherwise tell me and ask again.
3. Otherwise show **clickable choices (AskUserQuestion)**:
   - List the date prefixes (`YYYYMMDD`) of folders in `output/`, newest first (today first). Max 4 options per question, so show the 3 newest + **"Older dates"** (next 3, and so on).
   - After I pick a date, list that day's folders (`YYYYMMDD_name_N`) the same way (3 + "More").
   - Remind me I can paste a relative path instead of clicking.
4. If `output/` is empty, tell me to run `/create_interview` first and stop.
5. Write the chosen folder (relative to the project root, e.g. `output/20261121_api_nodejs_1`) to `.claude/ai_assist_scope.txt`. The guard reads this file.
6. Read the folder's `README.md` so you know the 5 questions, and ask which one I'm on.

## Step 2 — Work only in that folder
The selected folder is the **only** place you read, create, edit or run anything.
- Help me solve the problem: explain, hint, alter files, add functions, add tests, run them, debug.
- Do not read or edit anything else (other problems, `reference_files/`, `MEMORY.md`, other skills).
- **One exception:** update my scores in `about_me/what_to_improve.md` (see Step 3). Nothing else outside the folder.
- If I ask for something outside the folder, say it's out of scope and ask whether to end `/ai_assist`.
- Stay on this problem until I say I'm done.

## Step 3 — Update my score
When I finish a question or the session, update `about_me/what_to_improve.md`:
- Add/adjust rows for concepts I struggled with or got right (0–10 scale, start low, raise as I show I know it).
- Update "Notes" and "Last updated", and add a short dated line in the Log.
- Keep the file easy to read.

## Style
- Act like my normal AI coding tool, not a tutor. Help me solve the problem properly: write the code, fix bugs, add functions and tests, run them, explain only when useful.
- Don't withhold answers or give hints instead of solutions. Don't turn the work into a lesson.
- Keep replies short and plain.

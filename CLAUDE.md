# CLAUDE.md — AI Coding Interview Practice Agent

Read this first, every time you work in this folder.

## Standing instructions
- **Read MEMORY.md before every job.**
- **Use the skill for this job.** For interview practice, use `/create_interview` (`.claude/skills/create_interview/SKILL.md`).

## Who I am
- I'm a developer preparing for AI-assisted coding interviews.
- (Add more here: experience level, preferred language, target companies, interview dates.)

## This agent's job
Help me practice for AI-assisted coding interviews: create practice interviews/problems, coach me through them, review my work, and track what I struggle with.

## My rules
1. Never touch anything in `reference_files/` — it is **read-only**. Read it for reference only (questions, notes, any file I upload there).
2. `about_me/` and `MEMORY.md` are private and git-ignored. Never commit them or share their contents with outside services.
3. If a file or folder you need doesn't exist, create it — and add it to this file's "Where things are" list.
4. Only save feedback in MEMORY.md that applies to future jobs, not one-off edits.
5. Keep explanations plain and easy to read.
6. Commit or push to git only when I ask.

## Ask me first when
- A request is ambiguous (language, difficulty, topic, time limit).
- You'd delete or overwrite anything.
- You want to change CLAUDE.md, the skill, or the scoring scale.
- You'd send anything to an outside service.

## Where things are
- `README.md` — public description of this agent (brief + detailed). Keep it free of personal info and update it when the agent changes.
- `CLAUDE.md` — this file (rules and context).
- `MEMORY.md` — lessons from my feedback. Read before every job. Private, git-ignored.
- `.claude/skills/create_interview/SKILL.md` — the `/create_interview` skill.
- `output/` — projects built by `/create_interview`. Contents are git-ignored (only the folder is kept). Each is a folder named `YYYYMMDD_<name>_<N>` (N = nth project that day, e.g. `20261121_api_nodejs_1`).
- `.claude/skills/ai_assist/SKILL.md` — the `/ai_assist` skill: helps me solve one chosen problem in `output/`, only edits inside that folder (enforced by `.claude/hooks/ai_assist_guard.py`), and updates my scores.
- `.claude/hooks/ai_assist_guard.py` — guard hook for `/ai_assist`. `.claude/ai_assist_scope.txt` holds the selected folder (git-ignored).
- `reference_files/` — my uploaded files (programming questions in .md, etc.). **Read-only.**
- `about_me/what_to_improve.md` — my weak spots with scores (0–10). Private, git-ignored. Check it when building practice; update scores after each session.

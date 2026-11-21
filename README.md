# AI Coding Interview Practice Agent

A Claude Code agent that builds practice projects for AI-assisted coding interviews, then helps you solve them.

## Brief

- 🎯 **`/create_interview`**: answer a few questions (language, difficulty, topic, time limit) and get a ready-to-run practice project.
- 🧩 **Tailored to you**: suggestions and problems are shaped by the concepts you struggle with.
- 📝 **Built-in README per project**: up to 5 questions that get progressively harder, plus how to run it and its tests.
- 🐞 **Flexible formats**: a starter project to build on, a full project with hidden bugs, or just the algorithm question you provide.
- 🤝 **`/ai_assist`**: pick a project and work with a normal AI coding assistant, locked to that project's folder.
- 📈 **Progress tracking**: scores from 0 to 10 for each concept, updated as you improve.
- 🔒 **Private by default**: personal notes, memory and generated projects are git-ignored.

## Detailed description

### Table of contents

1. [Quick start](#quick-start)
2. [How it works](#how-it-works)
3. [`/create_interview`](#create_interview)
4. [`/ai_assist`](#ai_assist)
5. [Progress tracking](#progress-tracking)
6. [Project structure](#project-structure)
7. [Privacy and git](#privacy-and-git)
8. [Rules the agent follows](#rules-the-agent-follows)
9. [Customizing](#customizing)

### Quick start

1. Open this folder in Claude Code.
2. (Optional) Put your own practice questions as files in `reference_files/`.
3. Run `/create_interview` and answer the questions.
4. Open the new folder in `output/`, read its `README.md`, and start on question 1.
5. Run `/ai_assist` when you want help solving it.

### How it works

The agent is made of a few plain files. Claude reads `CLAUDE.md` first (who you are, rules, where things live), then `MEMORY.md` (lessons from your past feedback), then follows the skill you invoked.

### `/create_interview`

Builds a practice project for you.

1. **Asks four questions**: language, difficulty, topic, time limit. For each it offers suggestions based on your weak areas, and you can type your own answer.
2. **Skips ahead if you bring your own problem.** If you give a full example or a single algorithm question (in the prompt or in `reference_files/`), it builds just that, plus any boilerplate.
3. **Asks clarifying questions** (starter project vs. project with bugs, tests provided or written by you, libraries) and **waits for your confirmation** before creating anything.
4. **Creates the project** in `output/` named `YYYYMMDD_<name>_<N>`, where `N` is the nth project built that day (for example `20261121_api_nodejs_1`).
5. **Writes a `README.md` in the project** with:
   - what the project is and how to run it,
   - 5 questions where each builds on the previous one,
   - where the tests are. Tests may be commented out for you to enable as you progress, may fail on purpose (for example to expose a bug), or you may write your own.

No solutions are included in the project.

### `/ai_assist`

Your regular AI coding assistant, scoped to one practice project.

- **Pick a project** with clickable choices: dates newest first, then that day's projects. Or pass or paste a relative path, such as `/ai_assist output/20261121_api_nodejs_1`.
- **Works only inside the chosen folder.** It writes code, fixes bugs, adds functions and tests, and runs them. It acts as a normal assistant, not a tutor.
- **Enforced by a guard hook** (`.claude/hooks/ai_assist_guard.py`) that blocks file edits outside the selected folder. The only exception is the score file. Shell commands are checked on a best-effort basis.
- **Updates your scores** in `about_me/what_to_improve.md` when you finish a question or session.

### Progress tracking

`about_me/what_to_improve.md` lists concepts you struggle with, each with a score from 0 to 10 (10 means you know it well). Scores start low and rise as you show you understand a concept. `/create_interview` uses it to tailor suggestions, and `/ai_assist` updates it.

### Project structure

```
.
├── README.md                  # this file
├── CLAUDE.md                  # rules and context Claude reads first
├── MEMORY.md                  # lessons from your feedback (git-ignored)
├── about_me/                  # your private notes and scores (git-ignored)
│   └── what_to_improve.md
├── reference_files/           # your uploaded questions and files (read-only)
├── output/                    # generated projects (contents git-ignored)
│   └── YYYYMMDD_<name>_<N>/
└── .claude/
    ├── skills/
    │   ├── create_interview/SKILL.md
    │   └── ai_assist/SKILL.md
    └── hooks/ai_assist_guard.py
```

### Privacy and git

Git-ignored: `about_me/`, `MEMORY.md`, the contents of `output/` (the folder itself is kept), and `.claude/ai_assist_scope.txt`. Nothing personal is stored in `CLAUDE.md`.

### Rules the agent follows

- `reference_files/` is read-only. The agent never edits it.
- Missing files or folders are created as needed and recorded in `CLAUDE.md`.
- Only feedback that applies to future jobs is saved in `MEMORY.md`, not one-off edits.
- It asks before deleting or overwriting anything, changing its own rules or skills, or sending anything to an outside service.
- It commits to git only when you ask.

### Customizing

- Edit `.claude/skills/<name>/SKILL.md` to change how a skill works.
- Edit `CLAUDE.md` to change rules, your background, or preferences.
- Add your own practice questions to `reference_files/`.

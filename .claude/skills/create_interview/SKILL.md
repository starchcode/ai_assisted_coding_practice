---
name: create_interview
description: Create an AI-assisted coding interview practice project for me. Use when I type /create_interview or ask to practice for a coding interview.
---

# /create_interview

(Work in progress — the detailed workflow for building the problem will be added later.)

## Read first
1. `CLAUDE.md`
2. `MEMORY.md`
3. `about_me/what_to_improve.md` — my weak spots and scores (use to shape the problem)
4. Relevant files in `reference_files/` (read-only, never edit)

## Steps
1. **Ask me these four questions** (use AskUserQuestion, all in one go). Build nothing until I've answered.
   - **Language** (e.g. Node.js, Python, Java...)
   - **Difficulty** (easy / medium / hard)
   - **Topic** (e.g. APIs, arrays, concurrency, testing...)
   - **Time limit** (e.g. 30 / 45 / 60 min)
   - For each question, **offer a few suggestions I can pick from**, based on what you know about me: lowest-scoring concepts in `about_me/what_to_improve.md`, lessons in `MEMORY.md`, and `reference_files/`. Mark the suggestion that targets my weakest area as recommended and say why in one short line. I can always type my own answer.
2. **If I already gave a full example or a specific question** (in the prompt, as an algorithmic question, or a file in `reference_files/`), **build just that**, plus whatever boilerplate it needs. Don't invent extra questions or expand the scope: the README contains only the question(s) I gave (not the usual 5), plus run/test instructions. Skip questions I already answered, still ask the four in step 1 if anything is missing (language etc.), confirm the plan briefly, then build. Otherwise continue below.
   **Ask clarifying questions** until the problem is clear, using my four answers and/or any prompt I gave. Decide with me:
   - **Kind of project:** (a) a starter project I build upon, or (b) a complete project (e.g. a backend) with a few hidden bugs to find and fix, or another shape that fits.
   - Specifics: what it does, frameworks/libs, whether tests are provided or I write my own.
   - Then **summarize the plan and the project name, and wait for my confirmation.** Create nothing before I confirm.
3. **Create the output folder** `output/` if it doesn't exist (its contents are git-ignored; the folder itself is kept).
4. **Create the project folder** inside `output/` named `YYYYMMDD_<project_name>_<N>`:
   - `YYYYMMDD` = today's date
   - `<project_name>` = agreed name, lowercase with underscores
   - `<N>` = counter of projects built today (1 = first today). Check `output/` for existing folders with today's date to pick the next number.
   - Example: `20261121_api_nodejs_1`
5. **Build the project inside that folder** (only after I confirmed):
   - A boilerplate in most cases; initialise it fully when it's a complete project (install deps, make sure it runs).
   - **`README.md`** with:
     - What the project is and **how to start/run it** (exact commands).
     - **5 questions that build on each other**, each a bit harder or more advanced than the last. I solve #1, then #2 builds on it, and so on. For bug-fix projects, question 1 may be "find and fix this bug".
     - Where the tests are and how to run them.
   - **Tests, depending on the problem:**
     - Pre-written tests for later questions may be **commented out**; I uncomment them as I progress. Say in the README which test goes with which question.
     - A test may already fail on purpose (e.g. exposing a bug) so I see it fail, then fix it.
     - Sometimes I write my own tests; say so in the README.
   - Don't include solutions in the folder.
6. **After the session**, save any lasting feedback to `MEMORY.md`. Tell me to run `/ai_assist` to work on the problem.

## A good result looks like
- Tailored to my weak areas and my answers, and confirmed by me before building.
- Lives in its own correctly named folder under `output/`.
- Has a README with 5 progressive questions, run instructions, and test guidance.
- Runs out of the box (for complete projects).

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
1. **Ask me a series of questions** about what the problem should look like (e.g. language/stack, topic, difficulty, time limit, style). Don't build anything until I've answered.
   - Use what you know about me: favour concepts with low scores in `about_me/what_to_improve.md`, apply lessons in `MEMORY.md`, and draw on `reference_files/` where relevant.
2. **Agree on a project name** with me.
3. **Create the output folder** `output/` if it doesn't exist.
4. **Create the project folder** inside `output/` named `YYYYMMDD_<project_name>_<N>`:
   - `YYYYMMDD` = today's date
   - `<project_name>` = agreed name, lowercase with underscores
   - `<N>` = counter of projects built today (1 = first today). Check `output/` for existing folders with today's date to pick the next number.
   - Example: `20261121_api_nodejs_1`
5. **Build the problem** inside that folder. (Details TBD.)
6. **After the session**, update `about_me/what_to_improve.md` scores, and save any lasting feedback to `MEMORY.md`.

## A good result looks like
- Tailored to my weak areas and my answers.
- Lives in its own correctly named folder under `output/`.
- (More TBD.)

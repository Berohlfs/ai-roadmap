# 🤖 AI Coding

Since this is an ai-first repo, it'd be suiting to have some AI coding content on it.

By the time I'm writing this, I use primarily Claude Code and Cursor. Here is a collection of the features that I've used the most on each of them:

## Claude Code

- `./CLAUDE.md` file ([docs](https://www.anthropic.com/engineering/claude-code-best-practices)): Project-specific instructions. It **automatically loads** this file at the start of sessions as context to understand project architecture, coding standards, and tools, improving AI efficiency **(claude-code-specific context adapter)**.
    * Since it is loaded automatically to all sessions, this file should offer the minimum high-quality content about the overall structure of the project.

- Other cool Claude Code features (skills, subagents, hooks...): https://code.claude.com/docs/en/features-overview

## Cursor

- `./cursor/rules/*` ([docs](https://cursor.com/docs/context/rules#project-rules)): when included, rules gives the AI consistent guidance for generating code, interpreting edits, or helping with workflows.

- Other cool Cursor features (commands, skills, hooks...): https://cursor.com/docs

## ADRs

Using an `adr/` folder is perfect for giving AI agents “deep brain” context about your project without bloating AGENTS.md / CLAUDE.md.

An ADR **(Architecture Decision Record)** is a short document that explains an important technical decision, why it was made, and what rules follow from it (e.g. “we use Postgres for X because Y, so don’t do Z”).

> Ex: “We’re touching the token system. Please read `docs/adr/0003-tokens-handling-and-auth-flow.md` and then propose the change.”

- They are usually tied to rules, to enforce critical context on big refactors or new features.

## Cool videos to watch:

- [Agent Skills, Rules, Subagents: Explained!](https://www.youtube.com/watch?v=L_p5GxGSB_I)

## Personal Opinion

In my view, especially after discussing this with fellow colleagues, you have to (as one of them said) differentiate signal from noise. In other words, you need to understand what is currently hyped and what is truly useful.

This is useful advice for pretty much anything. However, AI coding tools are evolving at an incredible pace. Most of the time, attempting to come up with a perfect and up-to-date “dream AI workflow” ends up being a time-wasting overkill.

With that said, AI-assisted coding is clearly part of the future, and developers should onboard quickly into this new paradigm, without giving up critical thinking, product design, or architectural trade-offs.
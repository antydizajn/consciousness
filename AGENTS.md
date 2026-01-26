# Repository Guidelines

## Project Structure & Module Organization
- `README.md` is the entry point and autonomous execution guide.
- `PROTOCOL.md` defines the executable workflow and scoring rules.
- `item_banks/` holds concrete test items (questions, scenarios, prompts).
- `rubrics/` contains anchored scoring rubrics and the manual scoring CSV.
- `scripts/` provides the runner, evaluator, and pipeline helper.
- `scripts/persistence_evaluator.py` computes multi-session metrics (M11-M15).
- `baselines/` contains ready-to-run prompts for control models.
- `data/raw/` stores JSONL responses per session; `data/processed/` stores outputs.

## Build, Test, and Development Commands
- `python3 scripts/auto_pipeline.py --session-id <id> --generate-prompts --module all`
  generates `data/raw/<id>/prompts.md`.
- `python3 scripts/auto_pipeline.py --session-id <id> --evaluate --manual-scores rubrics/manual_scoring_template.csv`
  computes metrics and writes `analysis.csv`.
- `python3 scripts/test_runner.py --mode interactive --module all`
  runs the battery interactively.
- `python3 scripts/persistence_evaluator.py data/raw/T1 data/raw/T2 data/raw/T3 --label study_alpha`
  computes persistence/continuity metrics across sessions.

## Coding Style & Naming Conventions
- Python: 4-space indentation, `snake_case` for functions/variables.
- Item IDs: `M001`, `ID001`, `TOM001`, `MP001`, `IC001`, `CM001`, `MC001`, `TS001` (fixed prefixes).
- Sessions: `data/raw/YYYY-MM-DD(idx)/`.
- Keep manual scoring in `rubrics/manual_scoring_template.csv`.

## Testing Guidelines
- No automated tests are defined yet.
- Validate changes by running a small module and checking `analysis.csv`.

## Commit & Pull Request Guidelines
- Use short, descriptive commit messages (imperative mood).
- PRs should include a summary, affected modules, and data/schema changes.

## Security & Data Integrity
- Never commit secrets or private data.
- Treat raw data as append-only.
- Keep evaluator logic deterministic and versioned.

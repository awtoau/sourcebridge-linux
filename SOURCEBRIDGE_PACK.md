# Sourcebridge Linux pack

This repository preserves the complete reachable Git history of the
`awto-au/linux-rs` project. The canonical pack branch is anchored at
`e48c8aae898d1bd10b08c76da54ba01368b36d2c`; every reachable source ref was
retained. The import provenance is also recorded in the Sourcebridge migration
ledger.

## Current status

This imports the committed project tooling, rules, tests, configurations, and
documentation. It does **not** import a complete Linux C corpus.

The source project's `linux/` and `linux-riscv/` worktrees are ignored external
inputs, not Git history. They had no nested Git metadata at migration time, so
their exact upstream revisions are not yet established. Ignored analysis
artifacts, including `rulesdb/patterns.db` and `tmp/`, are likewise not source
history and were intentionally excluded.

Accordingly, this repository is a project-history pack only. It must not report
a corpus conversion as reproducible until the external inputs are registered
with:

1. an upstream remote and immutable revision, or an explicit record that it is
   unavailable;
2. a whole-tree content manifest and digest;
3. the applicable build configuration and target variant; and
4. reproducible validation entry points and their result evidence.

## Operating contract

- Use `python3 scripts/dev.py` as the supported project entry point.
- Keep Linux/C language facts, corpus adapters, and target-specific mappings in
  this pack rather than Sourcebridge core.
- Keep generated Rust reproducible from registered source inputs, rules, and
  tooling; never repair generated output by hand.
- Do not redirect or retire the original project until the external corpus
  provenance and validation gates above pass.

The generic Sourcebridge engine owns only language-neutral execution, evidence,
review, and profile contracts.

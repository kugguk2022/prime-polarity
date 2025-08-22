# Dataset: how to build or acquire

This project does not require an external dataset. It **generates** everything from integer ranges.

## Option A — generate a CSV (recommended)

```bash
python scripts/make_dataset.py \
  --start 100000 --end 120000 \
  --out data/polarity_100k_120k.csv
```

This writes a CSV with columns:
- `n` — integer
- `is_prime` — boolean ground truth
- `Z_raw` — \( Z(n) = \exp(\pi \zeta(n-1)/n) + 1 \) for \(n\ge3\) else NaN
- Feature columns: `FracPartMin`, `ForwardDiff`, `LogMellinSlope`, `MobiusFast`, `Dirichlet_q4`/`q5`/`q8`/`q12`, `K3`

## Option B — compute on the fly

All scripts accept `--start/--end` and compute features in memory without persisting a dataset.

## Notes

- For very large ranges, prefer multiple smaller shards (e.g., 100k windows).
- `Z_raw` is near-constant; signal tends to appear only after transforms. We include both for provenance.

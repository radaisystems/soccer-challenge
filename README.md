# Soccer League Scoring Utility

This utility takes a list of soccer match outcomes and calculates each teams
league ranking.

## How to run

The input format is shown in [sample-input.txt](sample-input.txt)
and may be provided to the script via a file as the sole argument, or via stdin
with one match per line.

Ex:

```bash
python main.py sample-input.txt
cat sample-input.txt | python main.py
python main.py < sample-input.txt
```

## Testing

Testing is facilitated via pytest, so that will need to be installed.
Then run `pytest` in the root of the repository

# Challenge Summary

I spent about 3 hours total working on this problem. The most challenging aspect
for me personally was getting back into a procedural/problem solving mindset
after spending about a year doing exclusively terraform, so I needed to Google
simple things about python to refresh my memory.

## Improvements

- Robust handling for malformed input
- Add packaging so the tool could be packaged and distributed

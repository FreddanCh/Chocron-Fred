
# KNN Classifier: Pichu vs Pikachu (Labb 2)

A beginner-friendly implementation of a k‑Nearest Neighbors (kNN) classifier that classifies Pokémon as **Pichu (0)** or **Pikachu (1)** from height/width measurements.

## Project layout
```
pichu_pikachu_knn/
├── data/
│   ├── datapoints.txt       # training data: width, height, label
│   └── testpoints.txt       # test samples to classify
├── src/
│   ├── knn.py               # core kNN logic (pure Python)
│   └── main.py              # CLI entrypoint
├── tests/
│   └── test_facit.py        # verifies given facit on four samples
├── .gitignore
└── README.md
```

## Quick start
```bash
# 1) Run the CLI on provided test points (k=1 by default)
python -m src.main --data data/datapoints.txt --test data/testpoints.txt

# 2) Try majority voting with the 10 nearest neighbors
python -m src.main --data data/datapoints.txt --test data/testpoints.txt --k 10

# 3) Classify a single point you type yourself (with input validation)
python -m src.main --data data/datapoints.txt --interactive
```

## What the program does

- Loads training data from `datapoints.txt` (width, height, label where 0=Pichu, 1=Pikachu).
- Computes Euclidean distance to find the *k* nearest neighbors.
- Predicts the class using **k=1 (nearest neighbor)** or **k=10 (majority vote)**.
- Handles invalid inputs (negative numbers / non-numeric) with friendly messages.
- Prints results in the exact format expected by the lab.

## Example output (k=1)

```
Sample with (width, height): (25.0, 32.0) classified as Pikachu
Sample with (width, height): (24.2, 31.5) classified as Pikachu
Sample with (width, height): (22.0, 34.0) classified as Pikachu
Sample with (width, height): (20.5, 34.0) classified as Pichu
```

## Testing (facit)
Run the included test to verify the four given points match the facit.
```bash
python -m tests.test_facit
```

## GitHub hand-in checklist

- Create a repo (public or private) on GitHub. Suggested name: `pichu-pikachu-knn`.
- Add a **clear commit history** (e.g., initial commit, add k=10 majority voting, add tests).
- Include this entire folder in the repo.
- Ensure `python -m src.main --data data/datapoints.txt --test data/testpoints.txt` runs and prints results.
- (Optional) Add a screenshot of the terminal output to your README.

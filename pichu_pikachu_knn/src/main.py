
from __future__ import annotations
import argparse
from typing import Tuple, List
from .knn import load_dataset, predict_knn, label_to_name

def parse_point(s: str) -> Tuple[float, float]:
    """
    Parse a point like '25,32' or '(25, 32)' into (25.0, 32.0).
    """
    s = s.strip().replace("(", "").replace(")", "")
    parts = [p.strip() for p in s.split(",")]
    if len(parts) != 2:
        raise ValueError("Please provide exactly two numbers: width,height")
    w = float(parts[0])
    h = float(parts[1])
    return (w, h)

def safe_read_testpoints(path: str) -> List[Tuple[float, float]]:
    """
    Read test points file that may contain lines like '1. (25, 32)'.
    Returns a list of (width, height) tuples.
    """
    pts: List[Tuple[float, float]] = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if "(" in line and ")" in line:
                inside = line[line.index("("): line.index(")")+1]
                pt = parse_point(inside)
                pts.append(pt)
            else:
                try:
                    pt = parse_point(line)
                    pts.append(pt)
                except Exception:
                    pass
    return pts

def classify_and_print(points, labels, testpoints, k: int):
    for w, h in testpoints:
        pred = predict_knn((w, h), points, labels, k=k)
        print(f"Sample with (width, height): ({w}, {h}) classified as {label_to_name(pred)}")

def interactive_loop(points, labels, k: int):
    print("Interactive mode. Type width,height (e.g. 24.2,31.5) or 'q' to quit.")
    while True:
        s = input("> ").strip()
        if s.lower() in {"q", "quit", "exit"}:
            print("Bye!")
            break
        try:
            w, h = parse_point(s)
            if w < 0 or h < 0:
                print("Error: width and height must be non-negative numbers.")
                continue
            pred = predict_knn((w, h), points, labels, k=k)
            print(f"Sample with (width, height): ({w}, {h}) classified as {label_to_name(pred)}")
        except ValueError as e:
            print(f"Invalid input: {e}")

def main():
    ap = argparse.ArgumentParser(description="kNN classifier for Pichu (0) vs Pikachu (1).")
    ap.add_argument("--data", default="data/datapoints.txt", help="Path to training data file.")
    ap.add_argument("--test", default=None, help="Optional path to testpoints file to classify.")
    ap.add_argument("--k", type=int, default=1, help="Number of neighbors (default: 1).")
    ap.add_argument("--interactive", action="store_true", help="Enter interactive classification mode.")
    args = ap.parse_args()

    points, labels = load_dataset(args.data)

    if args.test:
        testpoints = safe_read_testpoints(args.test)
        classify_and_print(points, labels, testpoints, k=args.k)

    if args.interactive or not args.test:
        interactive_loop(points, labels, k=args.k)

if __name__ == "__main__":
    main()

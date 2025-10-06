
from __future__ import annotations
from typing import List, Tuple

Point = Tuple[float, float]
LabeledPoint = Tuple[float, float, int]

def parse_data_line(line: str) -> LabeledPoint:
    """
    Parse one line of 'width, height, label' into a tuple of floats and int.
    Ignores leading/trailing spaces.
    """
    parts = [p.strip() for p in line.split(",")]
    if len(parts) < 3:
        raise ValueError(f"Expected 3 comma-separated values per line, got: {line!r}")
    w = float(parts[0])
    h = float(parts[1])
    lbl = int(parts[2])
    return (w, h, lbl)

def load_dataset(path: str) -> Tuple[List[Point], List[int]]:
    """
    Load dataset from a text file. The first line is a header.
    Remaining lines are 'width, height, label (0=Pichu,1=Pikachu)'.
    Returns (points, labels).
    """
    points: List[Point] = []
    labels: List[int] = []
    with open(path, "r", encoding="utf-8") as f:
        lines = f.read().strip().splitlines()
    # skip header if present (handles both with and without header gracefully)
    start_idx = 1 if lines and "label" in lines[0].lower() else 0
    for line in lines[start_idx:]:
        if not line.strip():
            continue
        w, h, lbl = parse_data_line(line)
        points.append((w, h))
        labels.append(lbl)
    return points, labels

def euclidean_distance(p: Point, q: Point) -> float:
    """
    Compute Euclidean distance between 2D points p and q.
    """
    dx = p[0] - q[0]
    dy = p[1] - q[1]
    return (dx*dx + dy*dy) ** 0.5

def argsort_by_distance(x: Point, points: List[Point]) -> List[int]:
    """
    Return indices of points sorted by distance to x (ascending).
    """
    distances = [(i, euclidean_distance(x, pt)) for i, pt in enumerate(points)]
    distances.sort(key=lambda t: t[1])
    return [i for i, _ in distances]

def predict_knn(x: Point, points: List[Point], labels: List[int], k: int = 1) -> int:
    """
    Predict label for x using k nearest neighbors among points/labels.
    Returns 0 for Pichu, 1 for Pikachu.
    """
    assert len(points) == len(labels), "points and labels must have the same length"
    if k <= 0:
        raise ValueError("k must be a positive integer")
    order = argsort_by_distance(x, points)
    k = min(k, len(order))
    # vote
    votes = {0: 0, 1: 0}
    for idx in order[:k]:
        votes[labels[idx]] += 1
    # break ties by nearest neighbor preference (deterministic)
    if votes[0] == votes[1]:
        return labels[order[0]]
    return 1 if votes[1] > votes[0] else 0

def label_to_name(lbl: int) -> str:
    return "Pikachu" if lbl == 1 else "Pichu"

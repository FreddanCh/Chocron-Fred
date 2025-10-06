
from src.knn import load_dataset, predict_knn

def run_test(k: int = 1):
    points, labels = load_dataset("data/datapoints.txt")
    cases = [
        ((25.0, 32.0), 1),     # Pikachu
        ((24.2, 31.5), 1),     # Pikachu
        ((22.0, 34.0), 1),     # Pikachu
        ((20.5, 34.0), 0),     # Pichu
    ]
    for (w, h), expected in cases:
        pred = predict_knn((w, h), points, labels, k=k)
        assert pred == expected, f"For {(w,h)} expected {expected} got {pred}"
    print("All facit tests passed with k =", k)

if __name__ == "__main__":
    run_test(1)

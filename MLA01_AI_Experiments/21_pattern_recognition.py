"""Experiment 21: Simple Pattern Recognition using image pixel data.
Requires: pip install numpy scikit-learn
This demo classifies synthetic numeric patterns, not real photographs.
"""

import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def main():
    digits = load_digits()
    X = digits.data
    y = digits.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print("Pattern-recognition demo using handwritten digit pixels")
    print("Test accuracy:", round(accuracy_score(y_test, predictions), 3))
    sample = X_test[0].reshape(1, -1)
    print("Actual digit:", y_test[0])
    print("Predicted digit:", model.predict(sample)[0])

if __name__ == "__main__":
    main()

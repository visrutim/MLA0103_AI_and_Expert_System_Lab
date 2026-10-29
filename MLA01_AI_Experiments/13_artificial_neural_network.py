"""Experiment 13: Artificial Neural Network classifier.
Requires: pip install scikit-learn
Synthetic example only; not a medical diagnostic tool.
"""

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, classification_report

def main():
    X, y = make_classification(
        n_samples=300, n_features=8, n_informative=5, n_redundant=1,
        random_state=42
    )
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    model = make_pipeline(
        StandardScaler(),
        MLPClassifier(hidden_layer_sizes=(16, 8), max_iter=1000, random_state=42)
    )
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print("Test accuracy:", round(accuracy_score(y_test, predictions), 3))
    print(classification_report(y_test, predictions, zero_division=0))

if __name__ == "__main__":
    main()

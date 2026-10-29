"""Experiment 12: Decision Tree Classifier.
Requires: pip install scikit-learn
Uses a tiny illustrative customer dataset (not for real loan decisions).
"""

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

def main():
    # Features: income in thousands, credit score, existing debt in thousands
    X = [
        [25, 580, 15], [30, 610, 12], [80, 750, 10], [90, 780, 8],
        [45, 650, 25], [70, 720, 20], [20, 550, 18], [100, 800, 5],
        [55, 680, 22], [35, 590, 30], [85, 760, 12], [60, 700, 15]
    ]
    # 1 = illustrative approve, 0 = illustrative reject
    y = [0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    model = DecisionTreeClassifier(max_depth=3, random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print("Predictions (1=illustrative approve, 0=illustrative reject):", predictions.tolist())
    print("Accuracy:", round(accuracy_score(y_test, predictions), 3))
    print(classification_report(y_test, predictions, zero_division=0))

if __name__ == "__main__":
    main()

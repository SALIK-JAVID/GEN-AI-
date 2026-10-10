"""Classify iris flower species with the K-Nearest Neighbors algorithm.

Install the dependency first if needed:
    python3 -m pip install scikit-learn
"""

from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def main() -> None:
    iris = load_iris()
    features = iris.data
    labels = iris.target

    x_train, x_test, y_train, y_test = train_test_split(
        features, labels, test_size=0.2, random_state=42, stratify=labels
    )

    # k=3 means the model checks the 3 closest flowers before deciding a class.
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(x_train, y_train)

    predictions = model.predict(x_test)
    accuracy = accuracy_score(y_test, predictions)

    print("Iris Flower Classification: K-Nearest Neighbors")
    print(f"Accuracy: {accuracy:.2%}")

    # Values: sepal length, sepal width, petal length, petal width (all in cm).
    new_flower = [[5.1, 3.5, 1.4, 0.2]]
    predicted_label = model.predict(new_flower)[0]
    print(f"Predicted species: {iris.target_names[predicted_label]}")


main()

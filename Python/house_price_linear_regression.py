"""Predict California house prices with a linear-regression model.

Install the dependency first if needed:
    python -m pip install scikit-learn
"""

from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


def main() -> None:
    # Download/load the dataset. Target values are in units of $100,000.
    housing = fetch_california_housing(as_frame=True)
    features = housing.data
    prices = housing.target

    x_train, x_test, y_train, y_test = train_test_split(
        features, prices, test_size=0.3, random_state=42
    )

    model = LinearRegression()
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)

    print("Linear regression model trained successfully.")
    print("MSE:", mean_squared_error(y_test, predictions))


main()

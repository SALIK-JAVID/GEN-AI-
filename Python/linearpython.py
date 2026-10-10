"""Predict California house prices with a linear-regression model.

Install the dependency first if needed:
    python -m pip install scikit-learn
"""

from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


def main() -> None:
    # Download/load the dataset. Target values are in units of $100,000.
    housing = fetch_california_housing(as_frame=True)
    features = housing.data
    prices = housing.target

    x_train, x_test, y_train, y_test = train_test_split(
        features, prices, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(x_train, y_train)

    predictions = model.predict(x_test)
    rmse = mean_squared_error(y_test, predictions) ** 0.5

    print("California Housing: Linear Regression")
    print(f"Training rows: {len(x_train):,}")
    print(f"Test rows:     {len(x_test):,}")
    print(f"MAE:  ${mean_absolute_error(y_test, predictions) * 100_000:,.2f}")
    print(f"RMSE: ${rmse * 100_000:,.2f}")
    print(f"R² score: {r2_score(y_test, predictions):.3f}")

    # Predict the price of the first test-house row as an example.
    example_price = model.predict(x_test.iloc[[0]])[0] * 100_000
    actual_price = y_test.iloc[0] * 100_000
    print(f"\nExample predicted price: ${example_price:,.2f}")
    print(f"Example actual price:    ${actual_price:,.2f}")


if __name__ == "__main__":
    main()
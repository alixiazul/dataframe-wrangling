from src.json_data import create_df, increase_price, get_best_value
from copy import copy
import pandas as pd


class TestCreateDf:
    def test_returns_dataframe(self):
        test_df = pd.DataFrame()
        result = create_df("data/doughnuts.json")
        assert type(test_df) == type(result)


class TestIncreasePrice:
    def test_does_not_mutate(self):
        df = create_df("data/doughnuts.json")
        df2 = increase_price(df, 5)
        assert df is not df2

    def test_multiplication_is_correct_with_positive_values(self):
        df = create_df("data/doughnuts.json")
        df2 = increase_price(df, 5)
        assert list(df2["price"]) == [round((i * 1.05), 2) for i in df["price"]]

    def test_multiplication_is_correct_with_negative_values(self):
        df = create_df("data/doughnuts.json")
        df2 = increase_price(df, -5)
        assert list(df2["price"]) == [round((i * 0.95), 2) for i in df["price"]]


class TestGetBestValue:
    def test_does_not_mutate(self):
        df = create_df("data/doughnuts.json")
        df2 = get_best_value(df)
        assert df is not df2

    def test_get_best_value_returns_a_string(self):
        df = create_df("data/doughnuts.json")
        df2 = get_best_value(df)
        assert isinstance(df2, str)

    def test_get_best_value_returns_cheapest_cost_per_calorie(self):
        df = create_df("data/doughnuts.json")
        df2 = get_best_value(df)
        assert df2 == "Choccy Delight"

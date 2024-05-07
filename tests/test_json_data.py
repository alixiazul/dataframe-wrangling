from src.json_data import create_df, increase_price, get_best_value

import pandas as pd


class TestCreateDf:
    def test_returns_dataframe(self):
        test_df = pd.DataFrame()
        result = create_df("data/doughnuts.json")
        assert type(test_df) == type(result)


class TestIncreasePrice:
    # def test_does_not_mutate(self):
    #     assert False

    def test_(self):
        df = create_df("data/doughnuts.json")
        df2 = increase_price(df, 5).price
        assert df.mul("price", 1.05) == df2


class TestGetBestValue:
    def test_(self):
        assert False

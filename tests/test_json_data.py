from src.json_data import create_df, increase_price, get_best_value

# import pandas as pd


class TestCreateDf:
    def test_returns_dataframe(self):
        # test_df = pandas.DataFrame()
        # assert type(test_df) == type(create_df("data/doughnuts.json"))
        assert False == type(create_df("data/doughnuts.json"))

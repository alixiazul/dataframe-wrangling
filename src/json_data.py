import pandas


def create_df(filename):
    return pandas.read_json(filename)


def increase_price(df, percent):
    return df.mul({"price", percent / 100 + 1})


def get_best_value(df):
    pass

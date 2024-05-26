import pandas as pd
from copy import deepcopy


def create_df(filename: str) -> pd.DataFrame:
    """
    Reads in a file and creates a dataframe with the content.

    Arguments:
    - filename: string. Name of the file whith the json data to read.

    Returns:
    Dataframe with the content of the file
    """
    df = pd.read_json(filename)
    df = pd.DataFrame([data for data in df.doughnut_data])
    return df


def increase_price(df, percent):
    """
    Arguments:
    - df: dataframe.
    - percent:
    should take the data frame and a percentage as arguments, and return a new dataframe with all the prices increased by the given percentage.
    """
    df2 = deepcopy(df)
    df2["price"] = round(df2["price"] * (percent / 100 + 1), 2)
    return df2


def get_best_value(df):
    """ " Calculates the cost per calorie of each doughnut and
    return the doughnut with the cheapes cost per calorie.
    (We didn't say this was a healthy exercise...)"""
    df2 = deepcopy(df)
    df2["cost_per_calorie"] = df2["price"] / df2["calories"]
    return df2.sort_values("cost_per_calorie").head(1).doughnut_type.item()

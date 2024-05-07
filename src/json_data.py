import pandas as pd
from copy import deepcopy

def create_df(filename):
    df = pd.read_json(filename)
    df = pd.DataFrame([data for data in df.doughnut_data])
    return df


def increase_price(df, percent):
    df2 = deepcopy(df)
    df2["price"] = round(df2["price"] * (percent / 100 + 1), 2)
    return df2


def get_best_value(df):
    """" Calculates the cost per calorie of each doughnut and return the doughnut with 
    the cheapes cost per calorie. (We didn't say this was a healthy exercise...)"""
    df2 = deepcopy(df)
    df2["cost_per_calorie"] = df2["price"] / df2["calories"]
    return df2.sort_values("cost_per_calorie").head(1).doughnut_type.item()
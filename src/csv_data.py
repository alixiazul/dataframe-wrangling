import pandas as pd
from copy import deepcopy


def create_df(filename):
    csv_data = pd.read_csv(filename, encoding="utf-8", encoding_errors="ignore")
    csv_data["booking_id"] = range(len(csv_data))
    return csv_data


def get_special_bookings(df, route):
    sb_df = deepcopy(df)
    return sb_df.loc[
        (sb_df["booking_origin"] == "Australia")
        & (sb_df["length_of_stay"] > 10)
        & (sb_df["route"] == route),
        ["booking_id", "route", "num_passengers", "length_of_stay", "flight_day"],
    ]


def get_passenger_totals(df):
    ptotal_df = deepcopy(df)
    return ptotal_df

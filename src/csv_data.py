import pandas as pd
from copy import deepcopy


def create_df(filename: str) -> pd.DataFrame:
    """
    Read the CSV data to a dataframe adding a booking_id unique
    number for each row.

    Arguments:
    - filename: name of the file with the customer bookings

    Returns:
    Dataframe with the csv data from the file
    """
    csv_data = pd.read_csv(filename, encoding="utf-8",
                           encoding_errors="ignore")
    csv_data["booking_id"] = range(len(csv_data))
    return csv_data


def get_special_bookings(df: pd.DataFrame, route: str) -> pd.DataFrame:
    """
    It creates a new dataframe with columns "booking_id", "route",
    "num_passengers", "length_of_stay", "flight_day". The rows should consist
    of those bookings for the chosen route that originate in Australia and
    have a length of stay of more than 10 days.

    Arguments:
    - route: route name.

    Returns:
    - dataframe
    """
    sb_df = deepcopy(df)
    return sb_df.loc[
        (sb_df["booking_origin"] == "Australia")
        & (sb_df["length_of_stay"] > 10)
        & (sb_df["route"] == route),
        ["booking_id", "route", "num_passengers", "length_of_stay",
         "flight_day"],
    ]


def get_passenger_totals(df: pd.DataFrame) -> int:
    """
    Creates a new dataframe that has route, sales_channel and a column called
    "total passengers" which adds the total number of passengers flying on
    each route and grouped by sales channel.
    """
    ptotal_df = deepcopy(df)
    return ptotal_df

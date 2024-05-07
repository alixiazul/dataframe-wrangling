from src.csv_data import create_df, get_special_bookings, get_passenger_totals
import pandas as pd


class TestCreateDF:
    def test_returns_dataframe(self):
        test_df = pd.DataFrame()
        result = create_df("data/customer_booking.csv")
        assert type(test_df) == type(result)

    def test_returns_dataframe_with_id(self):
        result = create_df("data/customer_booking.csv")
        assert list(result.booking_id) == list(range(len(result)))


class TestGetSpecialBookings:
    # I don't understand whta the rout is for
    def test_returns_dataframe(self):
        test_df = pd.DataFrame()
        result = create_df("data/customer_booking.csv")
        assert type(test_df) == type(result)

    def test_does_not_mutate_dataframe(self):
        df = create_df("data/customer_booking.csv")
        result = get_special_bookings(df, "AKLKUL")
        # expected_df = create_df("data/customer_booking.csv")
        assert df is not result

    # def test_does_not_change_given_dataframe(self):
    #     df = create_df("data/customer_booking.csv")
    #     result = get_special_bookings(df, None)
    #     expected_df = create_df("data/customer_booking.csv")
    #     assert df.items() == expected_df.items()

    def test_returns_correct_columns(self):
        df = create_df("data/customer_booking.csv")
        result = get_special_bookings(df, "AKLKUL")

        assert [i for i in result.columns] == [
            "booking_id",
            "route",
            "num_passengers",
            "length_of_stay",
            "flight_day",
        ]

    def test_returns_length_of_stay_more_then_ten(self):
        df = create_df("data/customer_booking.csv")
        result = get_special_bookings(df, "AKLKUL")

        assert all([day > 10 for day in result.length_of_stay])


class TestGetPassengerTotals:
    def test_returns_dataframe(self):
        test_df = pd.DataFrame()
        df = create_df("data/customer_booking.csv")
        result = get_passenger_totals(df)
        assert type(test_df) == type(result)

    def test_returns_new_dataframe(self):
        df = create_df("data/customer_booking.csv")
        result = get_passenger_totals(df)
        # expected_df = create_df("data/customer_booking.csv")
        assert df is not result

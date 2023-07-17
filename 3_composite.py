import datetime

import hypothesis.strategies as st

import pandas as pd
from hypothesis import given
from pandas._testing import assert_frame_equal


# Yes Marta, it's not a hallucination nor a nightmare, it's the European Scenario code.
def assign_season_label(df: pd.DataFrame, time_column: str) -> pd.DataFrame:
    mask_sum = df[time_column].dt.month.isin([6, 7, 8])
    mask_spri = df[time_column].dt.month.isin([3, 4, 5])
    mask_aut = df[time_column].dt.month.isin([9, 10, 11])
    mask_win = df[time_column].dt.month.isin([12, 1, 2])

    df.loc[mask_sum, 'season'] = "SUM"
    df.loc[mask_spri, 'season'] = "SPRI"
    df.loc[mask_aut, 'season'] = "AUT"
    df.loc[mask_win, 'season'] = "WIN"

    return df


def test_assign_season_label():
    input_df = pd.DataFrame({
        'dt': ['2022-01-12', '2022-04-15', '2022-09-23', '2022-07-13']
    })
    input_df['dt'] = pd.to_datetime(input_df['dt'])
    expected_df = pd.DataFrame({
        'dt': ['2022-01-12', '2022-04-15', '2022-09-23', '2022-07-13'],
        'season': ['WIN', 'SPRI', 'AUT', 'SUM']
    })
    expected_df['dt'] = pd.to_datetime(expected_df['dt'])
    actual_df = assign_season_label(input_df, 'dt')
    assert_frame_equal(actual_df, expected_df, atol=0, rtol=0)


@st.composite
def random_dataframe_with_dt_column(draw):
    n_rows = draw(st.integers(min_value=1, max_value=200))
    rows = [
        (draw(st.datetimes(min_value=datetime.datetime(1800, 1, 1),
                           max_value=datetime.datetime(2050, 12, 31),
                           allow_imaginary=False)),
         draw(st.floats()))
        for _ in range(n_rows)
    ]

    df = pd.DataFrame(rows, columns=['dt', 'generic_float_columns'])
    df['dt'] = pd.to_datetime(df['dt'])
    return df


@given(random_dataframe_with_dt_column())
def test_assign_season_label(df):
    res_df = assign_season_label(df, 'dt')

    assert 'season' in res_df.columns
    assert (res_df[res_df['dt'].dt.month.isin([12, 1, 2])]['season'] == 'WIN').all()
    assert (res_df[res_df['dt'].dt.month.isin([3, 4, 5])]['season'] == 'SPRI').all()
    assert (res_df[res_df['dt'].dt.month.isin([9, 10, 11])]['season'] == 'AUT').all()
    assert (res_df[res_df['dt'].dt.month.isin([6, 7, 8])]['season'] == 'SUM').all()


if __name__ == '__main__':
    print(random_dataframe_with_dt_column().example())
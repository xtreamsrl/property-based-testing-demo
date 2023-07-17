import pandas as pd
from hypothesis import given, note
import hypothesis.strategies as st


def temporal_train_test_split(data, split_date):
    train = data[data['date'] <= split_date]
    test = data[data["date"] > split_date]

    return train, test


@st.composite
def random_dataframe_with_a_date_column_strategy(draw):
    n_rows = draw(st.integers(min_value=0, max_value=100))

    rows = [
        (
            draw(st.dates().map(lambda d: d.strftime("%Y-%m-%d"))),
            draw(st.integers()),
            draw(st.sampled_from(list("abcd"))),
        )
        for _ in range(n_rows)
    ]
    data = pd.DataFrame(rows, columns=["date", "x1", "x2"])

    return data


@given(
    data=random_dataframe_with_a_date_column_strategy(), split_date=st.dates().map(lambda d: d.strftime("%Y-%m-%d"))
)
def test_temporal_train_test_split(data, split_date):
    train, test = temporal_train_test_split(data, split_date)
    concatenated = (
        pd.concat([train, test])
        .sort_values(["date", "x1", "x2"])
        .reset_index(drop=True)
    )
    sorted_input = data.sort_values(["date", "x1", "x2"]).reset_index(drop=True)

    assert (train["date"] <= split_date).all()
    assert (test["date"] > split_date).all()
    assert concatenated.equals(sorted_input)

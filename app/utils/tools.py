import pandas as pd


def create_pandas_df(snowpark_df):
    rows = snowpark_df.collect()

    data = []
    for row in rows:
        data.append(row.as_dict())

    df = pd.DataFrame(data)
    for column in df.columns:
        df = df.rename({column: column.lower()}, axis=1)

    return df

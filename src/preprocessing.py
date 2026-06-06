import pandas as pd

def convert_wide_to_long(df, value_name):

    first_col = df.columns[0]

    long_df = df.melt(
        id_vars=first_col,
        var_name="station_id",
        value_name=value_name
    )

    long_df = long_df.rename(
        columns={first_col:"timestamp"}
    )

    return long_df

def merge_occupancy_duration(
    occupancy_long,
    duration_long
):

    merged = occupancy_long.merge(
        duration_long,
        on=["timestamp","station_id"]
    )

    return merged
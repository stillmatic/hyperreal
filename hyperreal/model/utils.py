"""Various utility functions."""

import pandas as pd


def get_table_html(df: pd.DataFrame) -> str:
    """Dataframe -> HTML."""
    return df.to_html(
        border=0,
        justify='center',
        index=False,
        classes=["table", "table-striped", "table-sm", "table-hover"])

"""Dashboard component model code."""

from typing import List, Tuple
from .dependency import BaseDependency
from .datasource import BaseDataSource, FileDataSource
from .utils import get_table_html
import pandas as pd
import logging


class BaseComponent:
    """The base representation of a dashboard component."""

    def __init__(self,
                 name: str,
                 slug: str,
                 datasource: BaseDataSource) -> None:
        """Constructor method."""
        self.name = name
        self.slug = slug
        self.datasource = datasource

    def get_data(self) -> pd.DataFrame:
        raise NotImplementedError

    def get_dependencies(self) -> List[BaseDependency]:
        return self.datasource.dependencies

    def __key(self):
        return tuple(v for k, v in sorted(self.__dict__.items()))

    def __eq__(x, y):
        return isinstance(y, x.__class__) and x.__key() == y.__key()

    def __hash__(self):
        return hash(self.__key())


class TimeseriesComponent(BaseComponent):
    """Component which represents timeseries data."""

    def __init__(self,
                 name: str,
                 slug: str,
                 datasource: BaseDataSource,
                 time_col: str,
                 dim_cols: List[str],
                 val_cols: List[str]
                 ) -> None:
        self.time_col = time_col
        self.dim_cols = dim_cols
        self.val_cols = val_cols
        super().__init__(name, slug, datasource)

    def get_chart_data(self, req_val_cols: List[str],
                       filter_cols: List[Tuple[str, str]],
                       groupby_cols: List[str]) -> pd.DataFrame:
        raise NotImplementedError

    def table_chart_data(self, req_val_cols: List[str],
                         filter_cols: List[Tuple[str, str]],
                         groupby_cols: List[str]) -> str:
        return get_table_html(self.get_chart_data(req_val_cols,
                              filter_cols,
                              groupby_cols))


class TimeseriesFileComponent(TimeseriesComponent):
    """Timeseries component backed on disk."""

    def __init__(self,
                 name: str,
                 slug: str,
                 datasource: FileDataSource,
                 time_col: str,
                 dim_cols: List[str],
                 val_cols: List[str]
                 ) -> None:
        super().__init__(name, slug, datasource, time_col, dim_cols, val_cols)

    def get_chart_data(self,
                       req_val_cols: List[str],
                       filter_cols: List[Tuple[str, str]],
                       groupby_cols: List[str],
                       # orderby_cols: List[Tuple[str, bool]]
                       ) -> pd.DataFrame:
        assert len(req_val_cols) > 0

        # filter_cols = [('country', '"US"'), ('ad_type', 2)]
        assert len(groupby_cols) > 0
        groupby_cols = [self.time_col] + groupby_cols
        agg_func = 'sum'
        df = self.datasource.get_data()
        if filter_cols:
            filter_statement = ' and '.join(
                [f'{col} == {val}' for (col, val) in filter_cols])
            df = df.query(filter_statement)
        df = (df
              .groupby(groupby_cols)
              .agg({x: agg_func for x in req_val_cols})
              .reset_index())
        return df

    def get_distinct_values(self, dim_col) -> pd.DataFrame:
        df = self.datasource.get_data()
        return df[dim_col].drop_duplicates()

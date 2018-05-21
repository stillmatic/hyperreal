"""Data source models."""

from typing import List
from .dependency import BaseDependency
import pandas as pd


class BaseDataSource:
    """The base representation of a data source."""

    def __init__(self,
                 dependencies: List[BaseDependency]) -> None:
        """Constructor method."""
        self.dependencies = dependencies

    def get_data(self) -> pd.DataFrame:
        raise NotImplementedError

    def get_dependencies(self) -> List[BaseDependency]:
        return self.dependencies


class FileDataSource(BaseDataSource):
    """Data source which is backed by a csv file on disk."""

    def __init__(self,
                 dependencies: List[BaseDependency],
                 file_path: str) -> None:
        self.file_path = file_path
        super().__init__(dependencies)

    def get_data(self) -> pd.DataFrame:
        df = pd.read_csv(self.file_path)
        return df


class MemoryDataSource(BaseDataSource):
    """Data source which is backed by a dataframe in memory."""

    def __init__(self,
                 dependencies: List[BaseDependency],
                 df: pd.DataFrame) -> None:
        self.df = df
        super().__init__(dependencies)

    def get_data(self) -> pd.DataFrame:
        return self.df

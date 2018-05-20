from typing import NamedTuple, List
from .dependency import BaseDependency
import pandas as pd


class BaseComponent:
    """The base respresentation of a dashboard component."""

    def __init__(self,
                 name: str,
                 dependencies: List[BaseDependency]) -> None:
        """Constructor method."""
        self.name = name
        self.dependencies = dependencies

    def get_data(self) -> pd.DataFrame:
        raise NotImplementedError

    def get_dependencies(self) -> List[BaseDependency]:
        return self.dependencies

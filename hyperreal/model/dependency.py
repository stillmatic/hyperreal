"""Representations of dependencies."""
from datetime import datetime
from typing import NamedTuple


class BaseDependency:
    """Represents a base dependency."""

    def complete_for_dt(self, dt: datetime) -> bool:
        raise NotImplementedError

    def last_updated_dt(self) -> datetime:
        raise NotImplementedError


# class AirflowDependency(NamedTuple, BaseDependency):
#     """Represents a dependency in Airflow which we should wait for."""

#     dag_id: str  # noqa
#     task_id: str  # noqa

#     def __repr__(self) -> str:
#         return f'{self.dag_id}, {self.task_id}'

#     def dag_id(self) -> str:
#         return self.dag_id

#     def task_id(self) -> str:
#         return self.task_id

#     def complete_for_dt(self, dt: datetime) -> bool:
#         """TODO: hook up to Airflow."""
#         return True

#     def last_updated_dt(self) -> datetime:
#         """TODO: return last execution time from Airflow."""
#         return datetime.now()

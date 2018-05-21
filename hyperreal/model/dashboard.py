"""Defines key models for Hyperreal."""
from typing import List
from .component import BaseComponent
from .dependency import BaseDependency


def _slugify(s: str) -> str:
    """A naive implementation of slugification.

    Because we assume that users are internal and mature,
    we don't worry too much about safety.
    """
    import re
    # Remove all non-word characters (everything except numbers and letters)
    s = re.sub(r"[^\w\s]", '', s)

    # Replace all runs of whitespace with a single dash
    s = re.sub(r"\s+", '-', s)
    return s


class BaseDashboard:
    """A simple but flexible representation of a dashboard."""

    def __init__(self,
                 name: str,
                 description: str,
                 slug: str,
                 components: List[BaseComponent]) -> None:
        """Constructor method."""
        self.name = name
        self.description = description
        self.components = components
        self.slug = slug or _slugify(name)

        assert name is not None

    def construct_dashboard(self) -> None:
        """Return HTML for dashboard."""
        raise NotImplementedError

    def get_all_dependencies(self) -> List[BaseDependency]:
        deps = []
        for component in self.components:
            deps.append(component.get_dependencies())
        return deps

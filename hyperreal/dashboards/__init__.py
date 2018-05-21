"""Init file for dashboard definition files."""
from . import movies

ALL_DASHBOARDS = [movies.MovieDashboard]
ALL_COMPONENTS = [dash.components for dash in ALL_DASHBOARDS]
ALL_COMPONENTS = [item for sublist in ALL_COMPONENTS for item in sublist]

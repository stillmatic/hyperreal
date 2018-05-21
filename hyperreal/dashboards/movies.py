"""Dashboard of movies."""

from hyperreal.model.component import TimeseriesFileComponent
from hyperreal.model.dashboard import BaseDashboard
from hyperreal.model.datasource import FileDataSource
import pandas as pd

SRC_URL = 'https://query.data.world/s/v72hu6czerj6bprql3op2kqf56ojdy'

MovieDataSource = FileDataSource(dependencies=None, file_path=SRC_URL)

MovieComponent = TimeseriesFileComponent(name='Movies Component',
                                         slug='movies',
                                         datasource=MovieDataSource,
                                         time_col='title_year',
                                         dim_cols=['country',
                                                   'color'],
                                         val_cols=['total_budget', 'n_movies']
                                         )

MovieDashboard = BaseDashboard(name='Movie Dashboard',
                               description='Data about movies.',
                               components=[MovieComponent],
                               slug='movie_dash')

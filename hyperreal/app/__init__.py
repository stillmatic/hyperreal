"""Init file."""
from flask import Flask
from flask import render_template
from hyperreal.dashboards import ALL_DASHBOARDS, ALL_COMPONENTS
from hyperreal.model.utils import get_table_html
from flask import request
import json

app = Flask(__name__)
exploded_df = [{'name': d.name,
                'slug': d.slug,
                'dash_obj': d} for d in ALL_DASHBOARDS]


@app.route('/')
def index():
    """Root controller."""
    return render_template('index.html', dashes=exploded_df)


@app.route('/dash/')
def dashboards():
    """Dashboard root controller."""
    dashes = [d['name'] for d in exploded_df]
    return f'{dashes}'


@app.route('/dash/<slug>')
def individual_dash(slug=None):
    """Individual dash controller."""
    dash = [d['dash_obj'] for d in exploded_df if d['slug'] == slug]
    assert len(dash) == 1
    dash = dash[0]
    return render_template('dashboard.html',
                           dash=dash)


@app.route('/component/<slug>/get_chart_data', methods=['POST', 'GET'])
def get_chart_data(slug=None):
    """Return chart data given certain parameters."""
    params = request.form
    print(params)
    component = [c for c in ALL_COMPONENTS if c.slug == slug][0]
    filters = []
    for col in component.dim_cols:
        value = params.get(f'form_{slug}_{col}_filter')
        filters.append((col, f'"{value}"'))

    req_val_cols = params.getlist(f'form_{slug}_val_cols')
    groupby_cols = params.getlist(f'form_{slug}_grouping')
    return get_table_html(component.get_chart_data(req_val_cols=req_val_cols,
                                    groupby_cols=groupby_cols,
                                    filter_cols=filters))

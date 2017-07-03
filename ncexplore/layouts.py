
import dash_core_components as dcc
import dash_html_components as html

from .styles import base_style


def initialize_layout(ds):
    metadata_elements = [
            html.H1(children='Metadata'),
            html.B('Title:'),
            html.P(ds.title),
            html.B('Author:'),
            html.P(ds.author),
            html.B('Source:'),
            html.P(ds.source),
            html.Hr()
            ]
    metadata = html.Div(children=metadata_elements,
                        style={'width': '100%'})

    variable_elements = [
            html.H1(children='Variable Tools'),
            html.Label('Variable'),
            dcc.Dropdown(options=[{'label': k, 'value': k}
                                  for k in ds.variables],
                         value=ds.variables[0],
                         id='variable-selector'),
            html.Hr()
            ]
    variables = html.Div(children=variable_elements,
                         style={'width': '100%'})

    axes_elements = [
            html.H1(children='Axes Tools'),
            html.Label('x axis'),
            dcc.Dropdown(options=[{'label': k, 'value': k} for k in ds.axes],
                         value=ds.axes[1], id='x-selector'),
            html.Label('y axis'),
            dcc.Dropdown(options=[{'label': k, 'value': k} for k in ds.axes],
                         value=ds.axes[-1], id='y-selector'),
            html.Hr()
            ]
    axes = html.Div(children=axes_elements,
                    style={'width': '100%'})

    info_div = html.Div(id='info-pane',
                        style={'width': '45%', 'float': 'left'},
                        children=[metadata, variables, axes])

    spatial_elements = [
            html.H1(children='spatial plots here'),
            dcc.Graph(id='spatial-plot')
            ]
    spatial = html.Div(children=spatial_elements)

    timeseries = html.Div(children=html.H1(children='timeseries plots here'))

    plots_div = html.Div(id='plot-pane',
                         style={'width': '45%', 'float': 'right'},
                         children=[spatial, timeseries])

    base_layout = html.Div([info_div, plots_div])
    return base_layout

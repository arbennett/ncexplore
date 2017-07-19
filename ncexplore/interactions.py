
import dash
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import ncexplore as nce


def initialize_callbacks(app, ds):
    @app.callback(
            Output('spatial-plot', 'figure'),
            [Input('variable-selector', 'value'),
             Input('x-selector', 'value'),
             Input('y-selector', 'value')])
    def set_spatial_plot_var(var, x_name, y_name):
        return {'data': nce.plotting.contour(z=ds[var].isel(time=0).values),
                'layout': go.Layout(hovermode='closest')}

    @app.callback(
            Output('timeseries-plot', 'figure'),
            [Input('variable-selector', 'value'),
             Input('spatial-plot', 'clickData')])
    def build_timeseries_plot(var, clickData):
        clickData = clickData['points'][0]
        ydata = ds.isel(lat=clickData['x'], lon=clickData['y'])[var].values
        print(ydata)
        d = nce.plotting.timeseries(x=ds.time.values, y=ydata)
        print(d)
        return {'data': d,
                'layout': go.Layout(hovermode='closest')}

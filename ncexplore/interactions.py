
import dash
import plotly.graph_objs as go
import ncexplore as nce


def initialize_callbacks(app, ds):
    @app.callback(
            dash.dependencies.Output('spatial-plot', 'figure'),
            [dash.dependencies.Input('variable-selector', 'value'),
             dash.dependencies.Input('x-selector', 'value'),
             dash.dependencies.Input('y-selector', 'value')])
    def set_spatial_plot_var(var, x_name, y_name):
        return {'data': nce.plotting.contour(z=ds[var].isel(time=0).values),
                'layout': go.Layout(hovermode='closest')}
    
    

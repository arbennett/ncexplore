
import numpy as np
import matplotlib as mpl
import plotly.graph_objs as go


def convert_colormap(cmap_name: str):
    """Convert a maptlotlib colormap to a plotly one"""
    cmap_mpl = mpl.cm.get_cmap(cmap_name)
    h = 1. / 254.
    plotly_colorscale = []
    for i in range(255):
        r, g, b = map(np.uint8, np.array(cmap_mpl(h*i)[:3]) * 255)
        plotly_colorscale.append([h*i, 'rgb'+str((r, g, b))])
    return plotly_colorscale


def contour(z: np.array, x: np.array=None, y: np.array=None,
            cmap='viridis', ncontours=10):
    contour = go.Contour(
        x=x, y=y,  z=z,
        contours={'coloring': 'heatmap'},
        ncontours=ncontours,
        colorscale=convert_colormap(cmap)
    )
    return [contour]


def heatmap(z: np.array, x: np.array=None, y: np.array=None,
            cmap='viridis'):
    heatmap = go.Heatmap(
        x=x, y=y,  z=z,
        colorscale=convert_colormap(cmap)
    )
    return [heatmap]


def timeseries(x, y):
    timeseries = go.Scatter(x=x, y=y, mode='lines+markers')
    return [timeseries]

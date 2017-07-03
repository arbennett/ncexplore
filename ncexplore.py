#!/usr/bin/env python3

import os
import sys
import dash
import plotly.graph_objs as go
import ncexplore as nce


if __name__ == '__main__':
    datafile = sys.argv[1]
    if not os.path.isfile(datafile):
        exit('Provided path does not exist!')
    app = dash.Dash('NCExplore')
    app_data = nce.Dataset(datafile)
    app.layout = nce.initialize_layout(app_data)
    ds = app_data.data
    nce.initialize_callbacks(app, app_data.data)
    app.run_server()


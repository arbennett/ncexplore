
import os
import getpass
import xarray as xr


class Dataset(object):

    def __init__(self, file_path):
        self.data = xr.open_dataset(file_path)
        self.title = self.data.attrs.get('title', os.path.basename(file_path))
        self.source = self.data.attrs.get('source', os.path.dirname(file_path))
        self.author = self.data.attrs.get('author', getpass.getuser())
        self.axes = list(self.data.dims)
        self.variables = [v for v in list(self.data.variables)
                          if v not in list(self.data.coords)]

    def get_view(self, varname, locs):
        return self.data[varname].sel(**locs)

from os import pardir
from os.path import dirname, join

# Relative path to data folder.
_data_folder_path = join(dirname(__file__), pardir, pardir, "data_sets")

def get_data_path(sub_path):
    """Returns path to file in data folder."""
    return join(_data_folder_path, sub_path)

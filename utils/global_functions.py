import pandas as pd

from utils.utils import Utils as utl


def read_coordinates(file_name):
    path = utl.get_resource_path(f"data/scenarios/{file_name}")
    df = pd.read_csv(
        path, header=None, names=["x", "y", "z", "total_tonn", "gold_tonn", "else_tonn"]
    )
    return df

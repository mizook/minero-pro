import pandas as pd


def read_coordinates(file_name):
    df = pd.read_csv(f'data/scenarios/{file_name}', header=None,
                     names=["x", "y", "z", "total_tonn", "gold_tonn", "else_tonn"])
    return df

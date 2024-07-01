import numpy as np
import pandas as pd
from utils.utils import Utils as utl

def complete_mesh(df, x_range, y_range, z_range, default_tons, default_metal):
    x_vals, y_vals, z_vals = np.meshgrid(
        np.arange(x_range[0], x_range[1]),
        np.arange(y_range[0], y_range[1]),
        np.arange(z_range[0], z_range[1]),
        indexing='ij'
    )

    full_grid = pd.DataFrame({
        'X': x_vals.ravel(),
        'Y': y_vals.ravel(),
        'Z': z_vals.ravel()
    })

    df = pd.merge(full_grid, df, on=['X', 'Y', 'Z'], how='left')
    df['Tonelaje'].fillna(default_tons, inplace=True)
    df['Metal'].fillna(default_metal, inplace=True)
    df['Metal2'].fillna(0, inplace=True)


def calculate_cube_value(metal_tons, total_tons, metal_value, metal_cost, processing_cost, foundry_cost, metal_recovered):
    if metal_tons == 0:
        return - metal_cost * total_tons
    cube_value = ((float((metal_tons / total_tons)) * 100) * metal_value * metal_recovered * metal_tons) - (((metal_cost + processing_cost) * metal_recovered * foundry_cost) * metal_tons) - (metal_cost * total_tons)
    return cube_value


def mesh_value(df, metal_value, metal_cost, processing_cost, foundry_cost, metal_recovered):
    df['valor'] = df.apply(
        lambda row: calculate_cube_value(row['Metal'], row['Tonelaje'], metal_value, metal_cost, processing_cost, foundry_cost, metal_recovered), 
        axis=1
    )


def create_matrices(df):
    array = np.zeros((31, 22, 13))
    for index, row in df.iterrows():
        x, y, z, value = int(row['X']), int(row['Y']), int(row['Z']), row['valor']
        array[x][y][z] = value

    return array


def calculate_acum(matrices):
    
    for y in range(6, matrices.shape[1]):
        for x in range(6, matrices.shape[0]):
            for z in range(matrices.shape[2] - 2, 2, -1):
                matrices[x][y][z] += matrices[x][y][z+1]

    return matrices


def max_sum(matrices):
    for y in range(6, matrices.shape[1]):
        for z in range(matrices.shape[2] - 1, 2, -1):
            matrices[5][y][z] = matrices[6][y][z]

    for y in range(6, matrices.shape[1]):
        for x in range(6, matrices.shape[0]):
            for z in range(matrices.shape[2] - 2, 2, -1):
                matrices[x][y][z] += max(matrices[x-1][y][z+1], matrices[x-1][y][z], matrices[x-1][y][z-1] )

    

def calcular_upl(file_name):
    x_range = (6, 30)
    y_range = (10, 21)
    z_range = (3, 11)
    default_tons = 15375
    default_metal = 0
    metal_value = 10000 #USD/Ton 
    metal_cost = 1000  
    processing_cost = 200
    foundry_cost = 200
    metal_recovered = 0.85 

    path = utl.get_resource_path(f"data/scenarios/{file_name}")
    coordinates_df = utl.read_coordinates(path)

    complete_mesh(coordinates_df, x_range, y_range, z_range, default_tons, default_metal)
    mesh_value(coordinates_df, metal_value, metal_cost, processing_cost, foundry_cost, metal_recovered)
    matrices = create_matrices(coordinates_df)
    calculate_acum(matrices)
    max_sum(matrices)


    

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

def calculate_borderline(matrices, y_pos):
    max_value = -np.inf
    max_column = -1
    for x in range(6, matrices.shape[0]-1):
        if matrices[x][y_pos][11] > max_value:
            max_value = matrices[x][y_pos][11]
            max_column = x

    borderline = [(11, max_column)]

    pit_value = matrices[max_column][y_pos][11]

    column = max_column
    while column > 0:
        actual_rows = borderline[-1][0]
        
        column -= 1

        adjacents = []
        if actual_rows > 0:
            adjacents.append((actual_rows - 1, column))
        adjacents.append((actual_rows, column))
        if actual_rows < matrices.shape[0] - 1 :
            adjacents.append((actual_rows + 1, column))

        max_value = -np.inf
        max_position = None
        for position in adjacents:
            if matrices[position[1]][y_pos][position[0]] > max_value:
                max_value = matrices[position[1]][y_pos][position[0]]
                max_position = position
        
        borderline.append(max_position)

        if max_position[0] == 11:
            break

    for column in range(matrices.shape[0]):
        row = get_row_borderline(borderline, column)
        if row == None:
            for z in range(matrices.shape[2] - 2):
                matrices[column][y_pos][z] = 0
        else:
            for z in range(matrices.shape[2] - 2, row, -1):
                matrices[column][y_pos][z] = 0
    
    
    return pit_value


def get_row_borderline(borderline, column):
    for pos in borderline:
        if pos[1] == column:
            return pos[0]
    return None


def pit_to_df(matrices):
    data = []

    for x in range(6, matrices.shape[0]):
        for y in range(10, matrices.shape[1]):
            for z in range(3, matrices.shape[2]):
                value = matrices[x][y][z]
                if(value == 0):
                    data.append([x, y, z])

    df = pd.DataFrame(data, columns=['X', 'Y', 'Z'])
    return df


def calculate_upl(file_name):
    x_range = (6, 30)
    y_range = (10, 21)
    z_range = (3, 11)
    default_tons = 15375
    default_metal = 0
    metal_value = 10000 #USD/Ton 
    metal_cost = 500  
    processing_cost = 200
    foundry_cost = 200
    metal_recovered = 0.9 

    path = utl.get_resource_path(f"data/scenarios/{file_name}")
    coordinates_df = utl.read_coordinates(path)

    complete_mesh(coordinates_df, x_range, y_range, z_range, default_tons, default_metal)
    mesh_value(coordinates_df, metal_value, metal_cost, processing_cost, foundry_cost, metal_recovered)
    matrices = create_matrices(coordinates_df)
    matrices_aux = create_matrices(coordinates_df)
    calculate_acum(matrices)
    max_sum(matrices)
   
    pit_value = 0
    for y in range(10,22):
        pit_value += calculate_borderline(matrices, y)

    pit_df = pit_to_df(matrices)
        
    return pit_df, pit_value


    

import numpy as np
import pandas as pd

matrix = np.random.randint(0, 100, size=(10, 10))

def print_array(array, message=''):
    if message:
        print(message)
    print(array)


def save_as_file(array):
    to_txt = np.savetxt(f"Mytxt.txt", array, fmt='%s')

    assert np.array_equal(array, np.loadtxt(f"Mytxt.txt")), \
        "Text file saving may have altered array values."

    assert array.shape == np.loadtxt(f"Mytxt.txt").shape, \
        "Text file saving may have changed array dimensions."

    df = pd.DataFrame(array)
    my_csv = df.to_csv(f"Mycsv.csv", index=False)
    
    
    to_npy = np.save(f"Mynpy.npy", array)
    assert np.array_equal(array, np.load(f"Mynpy.npy")), \
        "NumPy binary file saving may have altered array values."

    assert array.shape == np.load(f"Mynpy.npy").shape, \
        "NumPy binary file saving may have changed array dimensions."
    return to_txt,to_npy, my_csv

print_array(save_as_file(matrix), 'Files created')


def load_from_files(file_path, file_format):
    if file_format == 'txt':
        return np.loadtxt(f"{file_path}.txt")
    elif file_format == 'csv':
        return pd.read_csv(f"{file_path}.csv").to_numpy()
    elif file_format == 'npy':
        return np.load(f"{file_path}.npy")
    else:
        raise ValueError("Invalid file format. Supported formats: 'txt', 'csv', 'npy'")

print_array(load_from_files('Mytxt', 'txt'), 'file from txt loaded')
print_array(load_from_files('Mynpy', 'npy'), 'file from npy loaded')
print_array(load_from_files('Mycsv', 'csv'), 'file from csv loaded')

def summation_array(array):
    return np.sum(array)
print_array(summation_array(matrix), 'the sum of all elements in array: ')


def mean_array(array):
    return np.mean(array)
print_array(mean_array(matrix), 'Mean of all elements in array:')


def median_array(array):
    return np.median(array)
print_array(median_array(matrix), 'Median of all elements in array:')

def standart_deviation(array):
    return np.std(array)
print_array(standart_deviation(matrix), 'Standart Deviation of array:')

def axis_aggregate(array, func, axis=0):
    return func(array, axis=axis)

row_sum = axis_aggregate(matrix, np.sum, axis=1)
print_array(row_sum,' Row-wise sum:')


col_mean = axis_aggregate(matrix, np.mean, axis=0)
print_array(col_mean,'Column-wise mean:')



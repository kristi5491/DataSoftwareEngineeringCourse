import numpy as np


matrix = np.random.randint(0, 100, size=(6, 6))

def print_array(array, message=''):
    if message:
        print(message)
    print(array)

print_array(matrix,'Original Matrix')

def transpose_array(matr):
    transposed = np.transpose(matr)
    assert transposed.shape == (matr.shape[1], matr.shape[0]), "Transpose failed: Dimensions do not match expected shape."
    return transposed


print_array(transpose_array(matrix),'Transposed matrix: ')

def reshape_array(matr):
    reshaped = np.reshape(matrix,[3,12])
    assert reshaped.size == matr.size, "Reshape failed"
    assert reshaped.shape == (3, 12), "Reshape failed: New shape does not match expected shape."
    return reshaped

print_array(reshape_array(matrix), 'Reshape array to [3, 12]:')

def split_array(matr, num_splits, axis):
    splits = np.split(matr, num_splits, axis=axis)
    assert len(splits) == num_splits, "Split failed: Number of sub-arrays does not match the expected number."
    for sub_array in splits:
        assert sub_array.shape[axis] == matr.shape[axis] // num_splits, "Split failed: Sub-array shape is incorrect."
    return splits

print_array(split_array(matrix,2,0), 'Sub-arrays:')

def combine_arrays(matr, axis=0):
    combined = np.concatenate(matr, axis=axis)
    expected_shape = list(matr[0].shape)
    expected_shape[axis] *= len(matr)
    assert combined.shape == tuple(expected_shape), "Combine failed: Combined shape does not match expected shape."
    return combined


array1 = np.random.randint(0, 100, size=(2, 3))
array2 = np.random.randint(0, 100, size=(2, 3))
array3 = np.random.randint(0, 100, size=(2, 3))

print_array(combine_arrays([array1, array2, array3], axis=0), 'Combined array:')
import numpy as np

one_d_array = np.arange(1,11)
one_d_array_9 = np.arange(1,10)
two_d_array = one_d_array_9.reshape((3,3))

# print(two_d_array)
# print(f'third element of array: {one_d_array[2]}')
# print(f'first two rows: {two_d_array[:2]}')
# print(f'first two columns: {two_d_array[:, :2]}')

added_array = one_d_array + 5
multiplied_array = two_d_array * 2


def print_array(array, message=''):
    if message:
        print(message)
    print(array)

    
print_array(two_d_array,'Two-dimensional NumPy array:')
print_array(one_d_array[2], 'third element of array:')
print_array(two_d_array[:2], 'first two rows:')
print_array(two_d_array[:, :2], 'first two columns')
print_array(added_array, 'Add 5 to each element of the one-dimensional array:' )
print_array(multiplied_array, 'Multiply each element of the two-dimensional array by 2:')

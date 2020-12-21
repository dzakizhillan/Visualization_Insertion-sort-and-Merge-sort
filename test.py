import traceback as tc
import sorting as s
import numpy as np

s.test = True


def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))


def test(sorting_function):
    arr = s.Array(np.random.randint(low=-2000, high=2000, size=10000))
    sorting_function(arr)
    try:
        assert is_sorted(arr.values), sorting_function.__name__ + ' Failed.'
    except AssertionError:
        tc.print_exc()
        return 'FAIL'
    return 'Passed'


functions = [
             s.insertion_sort, s.merge_sort]
for function in functions:
    print('Testing:   ', function.__name__.ljust(16), test(function))

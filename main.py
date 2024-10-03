import random

from insertion_sort import insertion_sort
from merge_sort import merge_sort


def test_sorted(data: list) -> list:
    return sorted(data)


def test_sort(data: list):
    data.sort()

def test_mergesort(data: list):
    merge_sort(data)

def test_insertion_sort(data: list):
    insertion_sort(data)


setup = '''
from __main__ import test_sorted
from __main__ import test_sort
from __main__ import test_mergesort
from __main__ import test_insertion_sort
import random
'''

if __name__ == '__main__':
    import timeit

    mrgesort = timeit.timeit('test_mergesort(random.sample(range(1, 10000), 1000))', setup=setup, number=1000)
    sorted = timeit.timeit('test_sorted(random.sample(range(1, 10000), 1000))', setup=setup, number=1000)
    sort = timeit.timeit('test_sort(random.sample(range(1, 10000), 1000))', setup=setup, number=1000)
    insertion_sort = timeit.timeit('test_insertion_sort(random.sample(range(1, 10000), 1000))', setup=setup, number=1000)

    print(f'mrgesort result: {mrgesort}')
    print(f'insertion_sort result: {insertion_sort}')
    print(f'sorted result: {sorted}')
    print(f'sort result: {sort}')


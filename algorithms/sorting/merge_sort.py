import random
import time
from insertion_sort import insertion_sort


def merge_sort(A: list):
    if len(A) > 1:
        middle = len(A) // 2
        L = A[:middle]
        R = A[middle:]

        merge_sort(L)
        merge_sort(R)

        len_R = len(R)
        len_L = len(L)

        i = j = k = 0

        while i < len_L and j < len_R:
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1

        while i < len_L:
            A[k] = L[i]
            i += 1

        while j < len_R:
            A[k] = R[j]
            j += 1


time_start = time.time()
array = random.sample(range(0, 1000000), 10000)
insertion_sort(array)
time_end = time.time()
print("Time to run selection_sort: {0}".format(time_end - time_start))


time_start = time.time()
array = random.sample(range(0, 1000000), 10000)
merge_sort(array)
time_end = time.time()
print("Time to run merge_sort: {0}".format(time_end - time_start))

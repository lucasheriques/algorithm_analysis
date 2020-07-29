def selection_sort(A: list):
    for i in range(len(A) - 1):
        smallest_index = i
        for j in range(i + 1, len(A)):
            if A[i] > A[j]:
                smallest_index = j
        A[i], A[smallest_index] = A[smallest_index], A[i]


A = [4, 2, 1, 5, 62, 5]
B = [3, 3, 2, 4, 6, 65, 8, 5]
C = [5, 4, 3, 2, 1]
D = [1, 2, 3, 4, 5]


selection_sort(A)
selection_sort(B)
selection_sort(C)
selection_sort(D)


print(A, B, C, D)

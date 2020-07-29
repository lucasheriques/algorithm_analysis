def insertion_sort(A: list):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key


A = [4, 2, 1, 5, 62, 5]
B = [3, 3, 2, 4, 6, 65, 8, 5]
C = [5, 4, 3, 2, 1]
D = [1, 2, 3, 4, 5]


insertion_sort(A)
insertion_sort(B)
insertion_sort(C)
insertion_sort(D)

print(A, B, C, D)

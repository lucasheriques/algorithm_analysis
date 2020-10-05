def check_odd_even(N):
    N = abs(N)
    Z = True

    while N > 2:
        N -= 2

    if N == 1:
        Z = False
    
    return Z

def check_nesting(S):
    if not S:
		    return True

    nesting_chars = {'{': '}', '[': ']', '(': ')'}
    stack = []
    Z = True

    for char in S:
        if char in nesting_chars :
            stack.append(nesting_chars [char])
        elif char in ['}', ']', ')']:
            if not stack or char != stack.pop():
                Z = False
                return Z

    if stack:
        Z = False

    return Z


def consecutive_zeros_binary(N):
    N = bin(N) # transforms the number into its binary form, from python standard library

    last = Y = 0
    for index, number in enumerate(N[2:]):
        if number == "1":
            Y = max(Y, index - last)
            last = index

    return Y

def bitwise_and_range(X, Y):
    Z = X
    for n in range(Z + 1, Y + 1):
        Z &= n
    
    return Z

def rotate_array(A, N):
    size = len(A)

    Z = [0] * size

    for i in range(size):
        Z[(i + N) % size] = A[i]
    
    return Z

print(check_nesting('(})'))

'''
print(check_odd_even(10))
print(check_odd_even(11))

print(rotate_array([1,2,3,4,5,6,7], 3))
'''
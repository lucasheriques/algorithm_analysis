def pizza(N):
    valor_total, max_soma, atual_max, min_soma, atual_min = 0, N[0], 0, N[0], 0
    for n in N:
        atual_max = max(atual_max + n, n)
        max_soma = max(max_soma, atual_max)
        atual_min = min(atual_min + n, n)
        min_soma = min(min_soma, atual_min)
        valor_total += n
    return max(max_soma, valor_total - min_soma) if max_soma > 0 else 0
    
input()
print(pizza([int(x) for x in input().split()]))
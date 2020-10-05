def knapsack(cap, pesos, valor, n):
    table = [[0 for i in range(cap + 1)] for i in range(n+1)]

    for i in range(n + 1):
        for j in range(cap + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif pesos[i-1] <= j:
                table[i][j] = max(valor[i-1] + table[i-1][j-pesos[i-1]], table[i-1][j])
            else:
                table[i][j] = table[i-1][j]

    return table[n][cap]



while True:
    linha = input()
    if not linha:
        break
    param = [int(x) for x in linha.split()]
    valor = [int(x) for x in input().split()]
    pesos = [int(x) for x in input().split()]
    print(knapsack(param[1], pesos, valor, param[0]))
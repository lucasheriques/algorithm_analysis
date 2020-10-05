def lucro_maximo(n, taxa, precos):
    vende, segura = 0, -precos[0]
    for i in range(1, n):
        vende = max(vende, segura + precos[i] - taxa)
        segura = max(segura, vende - precos[i])
    return vende

line = input().split()
n = int(line[0])
taxa = int(line[1])
line = input().split()
precos = [int(x) for x in line]

print(lucro_maximo(n, taxa, precos))
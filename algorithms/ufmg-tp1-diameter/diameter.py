import time

G = None
nV = edges = 0
INF = 999

startInput = time.time()
with open(r"E:\projects\algorithm_analysis\algorithms\ufmg-tp1-diameter\G-300-56691-densidade-0.63.txt", "r") as file:
    stripped_line = file.readline().strip().split(" ")
    nV = int(stripped_line[0])
    G = [[0 if i == j else INF for j in range(nV)] for i in range(nV)]
    for line in file:
        stripped_line = line.strip().split(" ")
        u, v, w = [int(i) for i in stripped_line]
        G[u-1][v-1] = G[v-1][u-1] = w
endInput = time.time()

inputTime = endInput - startInput


# Algorithm implementation
def floyd_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))
    # print(distance)

    # Adding vertices individually
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(
                    distance[i][j], distance[i][k] + distance[k][j])
    # print_solution(distance)

    return distance


def diameter_vertices(G):
    max_distance = 0
    vertices = [0, 0]

    for i in range(nV):
        for j in range(nV):
            if G[i][j] != INF and G[i][j] > max_distance:
                max_distance = G[i][j]
                vertices = [i + 1, j + 1]

    return max_distance, "{0} {1}".format(vertices[0], vertices[1])


# Printing the solution
def print_solution(distance):
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


trueStart = time.time()
distances = floyd_warshall(G)
diameter, vertices = diameter_vertices(distances)
trueEnd = time.time()

trueTime = trueEnd - trueStart + inputTime

print("{0}\n{1}\n{2}\n{3}".format(diameter, vertices, 0, 0))

print("Time to run: {:03.2f} seconds".format(trueTime))

import time
import argparse
import os
from argparse import ArgumentParser


def validate_file(f):
    if not os.path.exists(f):
        # Argparse uses the ArgumentTypeError to give a rejection message like:
        # error: argument input: x does not exist
        raise argparse.ArgumentTypeError("{0} does not exist".format(f))
    return f


if __name__ == "__main__":

    parser = ArgumentParser(description="Read file form Command line.")
    parser.add_argument("-i", "--input", dest="filename", required=True, type=validate_file,
                        help="input file", metavar="FILE")
    args = parser.parse_args()
    print(args.filename)

G = None
nV = edges = 0
INF = 999999

startInput = time.time()
with open(args.filename, "r") as file:
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
                vertices = [i, j]

    return max_distance, "{0} {1}".format(vertices[0], vertices[1])


def print_solution(distance):
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


def min_distance(dist, visited_vertices):
    # Initilaize minimum distance for next node
    min = INF

    # Search not nearest vertex not in the
    # shortest path tree
    for v in range(len(dist)):
        if dist[v] < min and visited_vertices[v] == False:
            min = dist[v]
            min_index = v

    return min_index


def printPath(parent, j, path=[]):

    # Base Case : If j is source
    if parent[j] == -1:
        path.append(j+1)
        return
    printPath(parent, parent[j])
    path.append(j+1)

    return path


def printSolution(dist, parent, src, target, path):
    print("Vertex \t\tDistance from Source\tPath")
    print("\n%d --> %d \t\t%d\t\t" % (src, target, dist[target]), end=" ")
    print(path, end=" ")


def dijkstra(G, source, target):
    dist = [INF] * len(G)
    parent = [-1] * len(G)
    visited_vertices = [False] * len(G)
    dist[source] = 0

    for _ in range(len(G)):
        u = min_distance(dist, visited_vertices)

        visited_vertices[u] = True

        for i in range(len(G)):
            if G[u][i] and visited_vertices[i] == False and dist[i] > dist[u] + G[u][i]:
                dist[i] = dist[u] + G[u][i]
                parent[i] = u

        if visited_vertices[target] == True:
            break

    path = printPath(parent, target)

    return path


trueStart = time.time()
distances = floyd_warshall(G)
diameter, vertices = diameter_vertices(distances)
vertices = vertices.split(" ")
vertices = [int(i) for i in vertices]
path = dijkstra(G, vertices[0], vertices[1])
trueEnd = time.time()


trueTime = trueEnd - trueStart + inputTime


print("{0}\n{1} {2}\n{3}\n{4}".format(
    diameter, vertices[0] + 1, vertices[1] + 1,  len(path), " ".join(str(x) for x in path)))

print("Time to run: {:03.2f} seconds".format(trueTime))

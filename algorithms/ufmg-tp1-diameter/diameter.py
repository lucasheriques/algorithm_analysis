import time
import argparse
import os
from argparse import ArgumentParser

trueStart = time.time()


parser = ArgumentParser(description="Read file form Command line.")
parser.add_argument("-i", "--input", dest="filename", required=True,
                    help="input file", metavar="FILE")
parser.add_argument("-o", "--output", dest="outputname",
                    required=True, help="output file")
args = parser.parse_args()

G = None
nV = nE = 0
INF = 999999

with open(args.filename, "r") as file:
    stripped_line = file.readline().strip().split()
    nV = int(stripped_line[0])
    G = [[0 if i == j else INF for j in range(nV)] for i in range(nV)]
    for line in file:
        stripped_line = line.strip().split()
        u, v, w = [int(i) for i in stripped_line]
        G[u-1][v-1] = G[v-1][u-1] = w


# complexidade: O(V^3), onde V é o número de vértices
def floyd_warshall(G):
    distance = [row[:] for row in G]

    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(
                    distance[i][j], distance[i][k] + distance[k][j])

    return distance


# complexidade: O(V^2) onde V é o número de vértices
def diameter_vertices(G):
    max_distance = 0
    vertices = [0, 0]

    for i in range(nV):
        for j in range(nV):
            if G[i][j] != INF and G[i][j] > max_distance:
                max_distance = G[i][j]
                vertices = [i, j]

    return max_distance, vertices


# complexidade: O(V) onde V é o número de vértices
def min_distance(dist, visited_vertices):
    min = INF

    for v in range(nV):
        if dist[v] < min and visited_vertices[v] == False:
            min = dist[v]
            min_index = v

    return min_index


# complexidade: O(V) onde V é o número de vétices
def get_path(parent, j, path=[]):
    # caso base: chegou na source (j)
    if parent[j] == -1:
        path.append(j)
        return
    get_path(parent, parent[j])
    path.append(j)

    return path


# complexidade: O(V^2) onde V é o número de vértices
def dijkstra(G, source, target):
    dist = [INF] * nV
    parent = [-1] * nV
    visited_vertices = [False] * nV
    dist[source] = 0

    for _ in range(nV):
        u = min_distance(dist, visited_vertices)

        visited_vertices[u] = True

        for i in range(nV):
            if G[u][i] and visited_vertices[i] == False and dist[i] > dist[u] + G[u][i]:
                dist[i] = dist[u] + G[u][i]
                parent[i] = u

        if visited_vertices[target] == True:
            break

    path = get_path(parent, target)

    return path


distances = floyd_warshall(G)
diameter, vertices = diameter_vertices(distances)
path = dijkstra(G, vertices[0], vertices[1])


output = "{0}\n{1} {2}\n{3}\n{4}".format(
    diameter, vertices[0]+1, vertices[1]+1,  len(path), " ".join(str(x+1) for x in path))

print(output)

output_file = open(args.outputname, "w+")
output_file.write(output)

trueEnd = time.time()
trueTime = trueEnd - trueStart
print("Time to run: {:03.2f} seconds".format(trueTime))

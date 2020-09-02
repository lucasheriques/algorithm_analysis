def print_solution(dist, parent, src, target, path):
    print("Vertex \t\tDistance from Source\tPath")
    print("\n%d --> %d \t\t%d\t\t" % (src, target, dist[target]), end=" ")
    print(path, end=" ")


def print_distances(distance):
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")

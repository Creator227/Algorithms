"""
Find a full matching with minimal weight in bipartite graph.

Reduce the task to the assigment problem.
Use Hungarian algorithm.
"""
with open('input.txt', 'r') as fin:
    # preparing data for problem. First group wouldn't be larger than second
    first = list(map(int, fin.readline().split()))
    second = list(map(int, fin.readline().split()))
    if len(first) < len(second):
        first, second = second, first
    n = len(first)
    m = len(second) + 1

# all indexes in matrix starts from 1
# n - size of greatest group, m - of smaller
# n - num of vertexes in left side, m - num of edges for each vertex
matrix = list()
for v in range(n + 1):
    matrix.append([0.0] * (n+1))
for i in range(n):
    for j in range(m - 1):
        matrix[i+1][j + 1] = abs(first[i] - second[j])
    for j in range(m, n + 1):
        matrix[i+1][j] = first[i] / 2

# Hungarian algorithm

u = [0] * (n + 1)
v = [0] * (n + 1)     # u,v[0,n] - potential for each vertex
p = [0] * (n + 1)     # matching array
way = [0] * (n + 1)

for i in range(1, n + 1):
    p[0] = i
    j0 = 0
    minv = [1000000.0] * (n + 1)
    used = [False] * (n + 1)
    while True:
        used[j0] = True
        i0 = p[j0]
        delta = 1000000.0
        new_j0 = 0
        for j in range(1, n+1):
            if not used[j]:
                if matrix[i0][j] - u[i0] - v[j] < minv[j]:
                    minv[j] = matrix[i0][j] - u[i0] - v[j]
                    way[j] = j0
                if minv[j] < delta:
                    delta = minv[j]
                    new_j0 = j
        for j in range(n+1):
            if used[j]:
                u[p[j]] += delta
                v[j] -= delta
            else:
                minv[j] -= delta
        j0 = new_j0
        if p[j0] == 0:
            break
    while True:
        new_j0 = way[j0]
        p[j0] = p[new_j0]
        j0 = new_j0
        if j0 == 0:
            break
answer = -v[0]
with open('output.txt', 'w') as fout:
    print('%.1f' % answer, file=fout)







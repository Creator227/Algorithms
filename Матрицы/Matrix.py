
with open('input.txt', 'r') as fin:
    size = int(fin.readline())
    matrix_sizes = [*map(int, fin.readline().split())]

    for new_size in fin.readlines():
        matrix_sizes.append(int(new_size.split()[1]))

# matrix size*size from matrix[i][j] elements of
# minimal count of operations to multiply matrix
# from i to j index
operations = []
for i in range(size):
    operations.append([0] * size)

for l in range(1, size):
    for i in range(size - l):
        j = l + i
        operations[i][j] = 100000001
        for k in range(i, j):
            new_cost = operations[i][k] + operations[k+1][j] +\
                       matrix_sizes[i-1] * matrix_sizes[k] * matrix_sizes[j]
            if new_cost < operations[i][j]:
                operations[i][j] = new_cost

fout = open('output.txt', 'w')
print(operations[0][size - 1], file=fout)




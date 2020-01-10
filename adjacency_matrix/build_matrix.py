with open('input.txt', 'r') as fin:
    v_num, e_num = fin.readline().split()
    matrix = list()
    for _ in range(int(v_num)):
        matrix.append([0] * int(v_num))
    for line in fin.readlines():
        v1, v2 = line.split()
        matrix[int(v1) - 1][int(v2) - 1] = 1
        matrix[int(v2) - 1][int(v1) - 1] = 1

with open('output.txt', 'w') as fout:
    for row in matrix:
            print(*row, file=fout)


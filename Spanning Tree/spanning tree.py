with open('input.txt', 'r') as fin:
    v_num = int(fin.readline())
    adjacencies_list = list()
    for line in fin.readlines():
        line = line.split()
        v_list = []
        for index, v in enumerate(line):
            if v == '1':
                v_list.append(index)
        adjacencies_list.append(v_list)

marks = [0] * v_num
mark = 1

spanning_tree = []
def BFS(queue: list):
    global mark
    while queue:
        v = queue.pop(0)
        marks[v] = mark
        mark += 1
        for new_v in adjacencies_list[v]:
            if new_v not in queue and marks[new_v] == 0:
                queue.append(new_v)
                spanning_tree.append((v + 1, new_v + 1))


BFS([0])
with open('output.txt', 'w') as fout:
    if 0 in marks:
        print(-1, file=fout)
    else:
        print(v_num - 1, file=fout)
        for m in spanning_tree:
            print(*m, file=fout)


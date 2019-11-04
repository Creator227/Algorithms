with open('input.txt', 'r') as fin:
    size = int(fin.readline())
    all_lilies = []
    for num in fin.readline().split():
        all_lilies.append(int(num))


max_path = [-1] * size
max_path[0] = all_lilies[0]


def find_max_path(index: int):
    global max_path
    if index > 2:
        if max_path[index - 3] == -1:
            find_max_path(index - 3)
        if max_path[index - 2] == -1:
            find_max_path(index - 2)
        max_path[index] = max(max_path[index - 3], max_path[index - 2]) + all_lilies[index]
    elif index == 2:
        max_path[index] = max_path[0] + all_lilies[index]
    elif index == 0:
        return

    else:
        max_path[index] = -1000000


with open('output.txt', 'w') as fout:
    find_max_path(size - 1)
    ans = max_path[size - 1]
    if ans >= 0:
        fout.write(str(ans))
    else:
        fout.write('-1')

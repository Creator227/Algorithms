with open("input.txt", "r") as fin:
    size = int(fin.readline())
    heap = fin.readline().split()
    heap = list(map(int, heap))
    answer = True
for index in range(size - 1, 0, -1):
    if heap[index] < heap[(index-1)//2]:
        answer = False
        break
with open("output.txt", "w") as fout:
    if answer:
        print("Yes", file=fout)
    else:
        print("No", file=fout)


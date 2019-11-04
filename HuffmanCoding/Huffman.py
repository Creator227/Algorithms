from heapq import heappush, heappop


def huffman_length(node: tuple, height: int)-> int:
    length = 0
    if node[1] is not ():
        length += huffman_length(node[1], height + 1)
        length += huffman_length(node[2], height + 1)
    else:
        length += node[0] * height
    return length


with open('huffman.txt', 'r') as fin:
    size = int(fin.readline())
    priority_queue = []

    for value in fin.readline().split():
        Node = (int(value), tuple(), tuple())
        priority_queue.append(Node)

# combining nodes with least priority
while len(priority_queue) > 1:
    left = heappop(priority_queue)
    right = heappop(priority_queue)
    new_node = (left[0] + right[0], left, right)
    heappush(priority_queue, new_node)

with open('huffman.out', 'w') as fout:
    print(huffman_length(priority_queue[0], 0), file=fout)




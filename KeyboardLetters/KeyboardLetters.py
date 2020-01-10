with open('in.txt', 'r') as fin:
    keys_num = int(fin.readline())
    letters_num = int(fin.readline())
    letters = []
    for _ in range(letters_num):
        letters.append(int(fin.readline()))

placement_matrix = list()
for _ in range(keys_num):
    placement_matrix.append([0] * letters_num)

placement_matrix[0][0] = letters[0]
for index in range(1, letters_num):
    placement_matrix[0][index] = letters[index] * (index + 1) + placement_matrix[0][index-1]

for key_index in range(1, keys_num):
    placement_matrix[key_index][key_index] = placement_matrix[key_index-1][key_index-1] + letters[key_index]
    position_on_key = 2
    for index in range(key_index + 1, letters_num):
        placement_matrix[key_index][index] = placement_matrix[key_index][index-1] + position_on_key * letters[index]
        position_on_key += 1
    for index in range(key_index + 1, letters_num):
        left_sum = placement_matrix[key_index - 1][index-1]
        position_on_key = 1
        for position in range(index, letters_num):
            left_sum += position_on_key * letters[position]
            position_on_key += 1
            placement_matrix[key_index][position] = min(left_sum, placement_matrix[key_index][position])

with open('out.txt', 'w') as fout:
    print(placement_matrix[keys_num - 1][letters_num - 1], file=fout)







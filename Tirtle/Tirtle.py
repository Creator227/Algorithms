with open('input.txt', 'r') as fin:
    rows_num, cols_num = map(int, fin.readline().split())

''' Calculationg num of pathes from first cell to last cell using DP.
    
    Using one row to calculate.
'''

first_row = [1] * cols_num

for _ in range(rows_num - 1):
    for index in range(1, cols_num):
        first_row[index] = (first_row[index-1] + first_row[index]) % 1000000007

with open('output.txt', 'w') as fout:
    fout.write(str(first_row[cols_num-1]))
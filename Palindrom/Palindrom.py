with open('input.txt', 'r') as fin:
    message = fin.readline()
    size = len(message)

# matrix of len of the biggest palindrome in substring
palindromes_lens = []
for _ in range(size):
    palindromes_lens.append([0] * 7000)
    palindromes_lens[_][_] = 1

for step in range(1, size):
    for start_index in range(size - step):
        finish_index = start_index + step
        # palindrome continue
        if message[start_index] == message[finish_index]:
            palindromes_lens[start_index][finish_index] = 2 + palindromes_lens[start_index + 1][finish_index - 1]
        # else throw out one of letters
        else:
            palindromes_lens[start_index][finish_index] = palindromes_lens[start_index][finish_index - 1] if \
                palindromes_lens[start_index][finish_index - 1] > palindromes_lens[start_index - 1][finish_index] else \
                palindromes_lens[start_index - 1][finish_index]

left = ""
right = ""
answer = ""
start_index = 0
finish_index = size - 1
while True:
    # odd message length
    if start_index == finish_index:
        answer = left + message[start_index] + right
        break
    # even message length
    if start_index > finish_index:
        answer = left + right
        break

    if message[start_index] == message[finish_index]:
        left += message[start_index]
        right = message[finish_index] + right
    else:
        if palindromes_lens[start_index + 1][finish_index] > palindromes_lens[start_index][finish_index - 1]:
            finish_index += 1
        else:
            start_index -= 1
    start_index += 1
    finish_index -= 1


with open('output.txt', 'w') as fout:
    print(str(len(answer)) + '\n' + answer, file=fout)








letter = input()

letter_list = list(letter)

if len(letter) >= 2:
    letter_list[1] = 'a'
    letter_list[-2] = 'a'

result = ''.join(letter_list)
print(result)
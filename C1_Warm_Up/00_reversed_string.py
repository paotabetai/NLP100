string = "stressed"

reversed_1 = ''.join(list(reversed(string)))

reversed_2 = list(string)
reversed_2.reverse()
reversed_2 = ''.join(reversed_2)

reversed_3 = string[::-1]

reversed_4 = ""

for character in string:
    reversed_4 = character + reversed_4

print(reversed_1, reversed_2, reversed_3, reversed_4)
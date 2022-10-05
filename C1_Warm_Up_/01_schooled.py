string = "schooled"

concatenation_1 = string[0::2]

concatenation_2 = string[0] + string[2] + string[4] + string[6]

concatenation_3 = ""

for i in range(len(string)):
    if i % 2 == 0:
        concatenation_3 += string[i]

print(concatenation_1, concatenation_2, concatenation_3)
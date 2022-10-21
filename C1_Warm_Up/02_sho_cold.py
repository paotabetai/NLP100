first = "shoe"

second = "cold"

schooled_1 = ''.join([first[i] + second[i] for i in range(len(first))])

schooled_2 = ''.join([f + s for f, s in zip(first, second)])

schooled_3 = ''.join((map(''.join, zip(first, second))))


print(schooled_1, schooled_2, schooled_3)
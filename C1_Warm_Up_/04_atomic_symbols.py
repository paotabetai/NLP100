sentence = '''Hi He Lied Because Boron Could Not Oxidize Fluorine.
    New Nations Might Also Sign Peace Security Clause. Arthur King Can'''

pattern = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
splitted_array = [word.strip(pattern) for word in sentence.split()]

map_1 = {(splitted_array[i][0].lower()
          if i in [0, 4, 5, 6, 7, 8, 14, 15, 18]
          else splitted_array[i][1].lower()):
         i for i in range(len(splitted_array))}

print(map_1)
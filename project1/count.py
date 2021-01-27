#Zackary Campbell
#Comp 3006
#This script includes a function that counts the number of instances of letters in .txt files.



import sys





def main():
    d = {}
    vals = []
    for val in sys.argv:
        vals.append(val)
    print(vals)
    for val in vals:
        if '.txt' in val:
            fileName = val
            print(f'character count for {fileName}')
            if '-c' in vals:
                boolean = False
            else:
                boolean = True
            if '-l' in vals:
                 letters = list(vals[vals.index('-l')+1])
            else:
                letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                   'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                   's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            for letter in letters:
                d[letter] = 0
            add_frequencies(d, fileName, remove_case = boolean)
            if '-z' in vals:
                True
            else:
                toBeDeleted = []
                for key in d.keys():
                    if d[key] == 0:
                        toBeDeleted.append(key)
                for item in toBeDeleted:
                    del d[item]
            for key in d.keys():
                print(key,',',d[key])






def add_frequencies(d, file1, remove_case):
    file = open(file1, mode = 'r', encoding = 'ASCII')

    if remove_case == True:
        for line in file:
            for character in line:
                if character.lower() in d.keys():
                   d[character.lower()] = d[character.lower()] + 1

    else:
        for line in file:
            for character in line:
                if character in d.keys():
                   d[character] = d[character] + 1
                elif character.lower() in d.keys():
                    d[character] = 1
    return d






main()

#add_frequencies(d, 'test.txt', 4)

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
#
#
#
# for letter in letters:
#     file = open('test.txt', mode = 'r', encoding = 'ASCII')
#     for line in file:
#         for character in line:
#             print(letter)

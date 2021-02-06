#Zackary Campbell
#Comp 3006
#This script includes a function that counts the number of instances of letters in .txt files.



import sys





def main():
    d = {}                                                                       #initialize
    vals = []
    for val in sys.argv:
        vals.append(val)                                                         #puts arguments in a list
    for val in vals:
        if '.txt' in val:                                                        #this is to make sure it can handle multiple text files
            fileName = val
            print(f'character count for {fileName}')
            if '-c' in vals:                                                    #this flag counts capital letters different from lowercase
                boolean = False
            else:
                boolean = True
            if '-l' in vals:                                                        #this flag allows you to count only certain characters. They do not have to be letters
                 letters = list(vals[vals.index('-l')+1])                           #changes our list of search letters to the sequence input
            else:
                letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',             #otherwise the default is the english lowercase alphabet
                   'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                   's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            for letter in letters:
                d[letter] = 0                                                       #creates a key in our dictionary for eachg search letter and sets it to 0
            add_frequencies(d, fileName, remove_case = boolean)                     #runs our helper coutn function
            if '-z' in vals:                                                        #including this flag shows counts for all letters in the search regardless of the count
                True
            else:                                                                   #by default, characters with a count of 0 are deleted
                toBeDeleted = []
                for key in d.keys():
                    if d[key] == 0:
                        toBeDeleted.append(key)
                for item in toBeDeleted:
                    del d[item]
            for key in d.keys():
                print(key,',',d[key])                                               #prints the dictionary as a csv






def add_frequencies(d, file1, remove_case):
    file = open(file1, mode = 'r', encoding = 'ASCII')

    if remove_case == True:                                                         #This counts capital and lowercase letters the same
        for line in file:
            for character in line:
                if character.lower() in d.keys():                                   #Goes through every character in our file, checks if it is on list of search characters and adds 1 to the character count it matches
                   d[character.lower()] = d[character.lower()] + 1

    else:                                                                           #This does the same thing but capital and lowercase letters are treated differently.
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

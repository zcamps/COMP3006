import unittest
from count_module import countchar
import sys




class CountTestCase(unittest.TestCase):


    def test_z(self):                                                                               #this tests the flag '-z' to make sure if you pass it an empty .txt file it returns a dictionary with zeros
        # f = open('test_z.txt', mode = 'w', encoding = 'ASCII')
        # f.write('')
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                   'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                   's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        sys.argv.append('-z')
        sys.argv.append('test_z.txt')                                                               #these pass the appropriate flags into sys for our test inlcuding our file
        result1 = countchar()
        for letter in letters:
            self.assertIn(letter, result1.keys())                                                   #checks that every letter is in the set of keys regardless of their value
            shouldBeZero = result1[letter]
            expectedValue = 0
            self.assertEqual(shouldBeZero, expectedValue)                                           #Checks that the value of every key in this case is 0

        #sys.argv.pop(-1)

        # newF = open('test_z_character.txt', mode = 'w', encoding = 'ASCII')
        # newF.write(' $ 7 9 ; } + < > *')

        sys.argv.append('test_z_character.txt')                                                     #This sets up our second test, which tests this flag still returns only the letters in letters despite other characters being present
        result2 = countchar()
        for letter in letters:
            self.assertIn(letter, result2.keys())                                                   #Thecks that the every letter is in the set of keys





    def test_c(self):                                                                           #This tests the flag H and make sure it properly counts capitals when letters are not separated
        # f = open('test_c.txt', mode = 'w', encoding = 'ASCII')
        # f.write('HhHHh')

        sys.argv.append('-c')
        sys.argv.append('test_c.txt')                                                               #these pass the appropriate flags into sys for our test inlcuding our file
        result3 = countchar()
        val1 = result3['H']
        val2 = result3['h']
        expected_H = 3                                                                              #We expect 3 'H' and two 'h'
        expected_h = 2

        self.assertEqual(val1, expected_H)
        self.assertEqual(val2, expected_h)




    def test_l(self):                                                                      #this tests the flag '-l' to make sure if you pass it no letters it returns an empty dictionary
        sys.argv.append('-l')
        sys.argv.append('')
        sys.argv.append('test2.txt')                                                      #these pass the appropriate flags into sys for our test inlcuding our file and 0 letters
        result4 = countchar()
        expectedEmptyDict = 0                                                               #We're expecting there to be 0 letters in our dictionary after this test
        self.assertEqual(len(result4.keys()), expectedEmptyDict)



    def tearDown(self):
        flags = ['-z', '-l', '-c']
        for flag in flags:
            if flag in sys.argv:                                                           #this removes all of the flags after running each test
                sys.argv.remove(flag)                                                      #If you'd like to check combinations of flags, comment
                                                                                           # this section out and comment out any tests you'd not
                                                                                           #like to run



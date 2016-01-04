import string
from itertools import *
import time

"""Word unscrambler without repeats of words due to repeating letters

    To Do: Use Phone number dictionary to use each number for a specific
    set of letters and then create unscrambled words from the set of
    specific letters.
"""
def pause(length):
        time.sleep(length)

def timeout(length, startTime):
        curTime = time.time()
        if (curTime - startTime) > length:
            print("Timeout Error")
            return True

def unscrambler(scrambled_word):
    i,j = 0,0
    word_list = []
    startTime = time.time()
    
    dict = open('/usr/share/dict/words')
    dictionary = dict.read().split()
    some_word = list(scrambled_word)
    perm_list = list(permutations(some_word))

    while i < len(perm_list):
        if timeout(5, startTime):
            break
        pWord = ''.join(perm_list[i])
        if pWord in dictionary:
            word_list.append(pWord)
        i += 1
    
    if not word_list:
        print('The word could not be unscrambled.')
    else:
        print('These are the possible unscrambled words:')
        word_list = list(set(word_list)) #removes duplicates
        while j < len(word_list):
            print(word_list[j])
            j += 1

unscrambler('elolh') #hello world
#see if there are spaces in the word then unscramble each word
    

def scrambler(unscrambled_word):
    i = 0
    word_list = []
    startTime = time.time()
    
    dict = open('/usr/share/dict/words')
    dictionary = dict.read().split()
    some_word = list(unscrambled_word)
    perm_list = list(permutations(some_word))

    while i < len(perm_list):
        timeout(5, startTime)
        pWord = ''.join(perm_list[i])
        if pWord not in dictionary:
            print(pWord)
            return
        i += 1


scrambler('hello')

    # if not word_list:
    #     print('The word could not be unscrambled.')
    # else:
    #     print('These are the possible unscrambled words:')
    #     word_list = list(set(word_list))
    #     while j < len(word_list):
    #         print(word_list[j])
    #         j += 1


# letters = string.ascii_lowercase

# phone = {'1':[string.ascii_lowercase], '2': ['a','b','c'], '3': ['d','e','f'], '4': ['g','h','i'],
#  '5': ['j','k','l'], '6': ['m','n','o'],'7': ['p','q','r','s'], '8': ['t','u','v'],
#  '9': ['w','x','y','z'], '0':[string.ascii_lowercase]}

# letters = []
# word_lists = []
# num = '233'

# # inPut = input("Enter a phone number: ")
# # num = int(inPut)

# f = open('big.txt','r')
# text = f.readline()

# for x in num:
#     for y in x:
#         letters.append(phone[y])


# letter_combos = list(permutations(letters))
# print(letter_combos)


# def possibleLetters(number):
# 	for x in number:
# 		print(phone[x])
# 		for y in phone[x]:
#             letters.append(y)
#             print(letters)
# 			if word in text:
# 			    word_lists.append(word)

# possibleLetters(num)
# print(letters)

# possible_words = []

# def allwords(chars, length):
#     for letters in product(chars, repeat=length):
#         yield ''.join(letters)

# def getPossible(letters):
#     # letters = 'ebe'
#     letterLen = len(letters)
#     for word in allwords(letters, letterLen):
#         possible_words.append(word)
#     return possible_words




# http://stackoverflow.com/questions/21559039/python-how-to-generate-wordlist-from-given-characters-of-specific-length
#http://codereview.stackexchange.com/questions/14828/generating-words-based-on-a-list-of-letters
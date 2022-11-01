#(1). Write a Python program to check if a number is positive, negative or Zero.
#Number = int(input("Enter a Number Here: "))
# if Number > 0:
#     print("Number is Positive")
# elif Number < 0:
#     print("Number is Negative")
# elif Number == 0:
#     print("Number is Zero")


#(2). Write a Python program to get the Factorial number of given number.
# Number = int(input("Enter a Number Here: "))
# temp = 1
# for i in range(1, Number+1):
#     temp = temp * i
# print(temp)

#(3). Write a Python program to get the Fibonacci series of given range.

# a = 0
# b = 1
# for i in range(5):
#     print(a)
#     c = a+b
#     a = b
#     b = a

#(4). How memory is managed in Python?

# Memory management in Python involves a private heap containing all Python objects and data structures. 
# The management of this private heap is ensured internally by the Python memory manager. 
# The Python memory manager has different components which deal with various dynamic storage management aspects, like sharing, segmentation, preallocation or caching.


#(5). What is the purpose continue statement in python? 
#The continue keyword is used to end the current iteration in a for loop or a while loop, and continues to the next iteration.
    

#(6). Write python program that swap two number with temp variable and without temp variable. 
#with Temp Variable
# a = 0
# b = 1
# print(a)
# print(b)
# temp = a
# a = b
# b = temp
# print(a)
# print(b)

#Without Temp Variable
# a = 0
# b = 1
# a,b = b,a
# print("a =", a)
# print("b =", b)

#(7). Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.

# value = int(input("Enter a number: "))
# if value%2 == 0:
#     print("Number is Even")
# else:
#     print("Number is odd")


#(8). Write a Python program to test whether a passed letter is a vowel or not.

# letter = input("Enter a letter: ")
# if letter in ('a','e','i','o','u'):
#     print("Letter is vowel")
# else:
#     print("Letter is not vowel")

#(9). Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

# def value(a,b,c):
#     if a==b or b==c or c==a:
#         value = 0
#     else:
#         value = a+b+c
#     return value
# print(value(4,4,6))
# print(value(5,6,7))

#(10). Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.


# def value(a,b):
#     if a==b or (a-b) == 5 or (a+b) == 5:
#         return True
#     else:
#         return False
# print(value(2,3))   
# print(value(6,8))
# print(value(7,2))

#(11). Write a python program to sum of the first n positive integers.

# num = int(input("Enter your number: "))
# a = (num*(num+1))/2
# print("sum of the first", num, "positive integers:", a)

#(12). Write a Python program to calculate the length of a string.

# a = input("Enter Here: ")
# print("length is:", len(a))

#(13). Write a Python program to count the number of characters (character frequency) in a string.

# def frequency(x):
#     dict = {}
#     for i in x:
#         keys = dict.keys()
#         if i in keys:
#             dict[i] += 1
#         else:
#             dict[i] = 1
#     return dict
# print(frequency('My name is Jignesh Panchal'))


#(14). What are negative indexes and why are they used?

# Negative indexing is the indexing from the end.
# We can use negative indexing as our advantage when we want to pick values from the end of an iterable.

#(15). Write a Python program to count occurrences of a substring in a string.

# char = 'Python is the easiest language of all coding language.'
# print(char.count("language"))

#(16). Write a Python program to count the occurrences of each word in a given sentence.

# def word_count(str):
#     counts = dict()
#     words = str.split()
#     for word in words:
#         if word in counts:  
#             counts[word] += 1
#         else:
#             counts[word] = 1
    
#     return counts
# print( word_count('CANADA IS A GOOD PLACE FOR INDIAN STUDENTS, INDIA IS GOOD TOO'))

#(17). Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# def char(a, b):
#   new_a = b[:2] + a[2:]
#   new_b = a[:2] + b[2:]

#   return new_a + ' ' + new_b
# print(char('gjt', 'kuo'))

#(18). Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 
# 'ly' instead if the string length of the given string is less than 3, leave it unchanged.

# def new_string(str):
#     length = len(str)
    
#     if length > 2:
#         if str[-3:] == 'ing':
#             str += 'ly'
#         else:
#             str += 'ing'
#     return str
# print(new_string('jk'))
# print(new_string('BBC'))
# print(new_string('Running'))

#(19). Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the 
# whole 'not'...'poor' substring with 'good'. Return the resulting string.


# def not_poor(str):
#     snot = str.find('not')
#     spoor = str.find('poor')

#     if spoor > snot and snot > 0 and spoor > 0:
#         str = str.replace(str[snot:(spoor+4)], 'good')
#         return str
#     else:
#         return str
# print(not_poor('India is not a poor country'))
# print(not_poor('Beggars are poor'))

#(20). Write a Python function that takes a list of words and returns the length of the longest one

# def find_longest_word(words_list):
#     word_len = []
#     for n in words_list:
#         word_len.append((len(n), n))
#     word_len.sort()
#     return word_len[-1][0], word_len[-1][1]
# result = find_longest_word(["Python", "Elephant", "java"])
# print("\nLongest word: ",result[1])
# print("Length of the longest word: ",result[0])

#(21). Write a Python function to reverses a string if its length is a multiple of 4.
# def reverse_string(str1):
#     if len(str1) % 4 == 0:
#        return ''.join(reversed(str1))
#     return str1

# print(reverse_string('True'))
# print(reverse_string('python'))

#(22). Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return 
#instead of the empty string.

# def string_both_ends(str):
#   if len(str) < 2:
#     return ''

#   return str[0:2] + str[-2:]

# print(string_both_ends('indianarmy'))
# print(string_both_ends('wwe'))
# print(string_both_ends('w'))


#(23). Write a Python function to insert a string in the middle of a string.

# def insert_string_middle(str, word):
# 	return str[:2] + word + str[2:]

# print(insert_string_middle('[[]]', 'Python'))
# print(insert_string_middle('{{}}', 'Samsung'))
# print(insert_string_middle('<<>>', 'Apple'))
'''
Student: Youssef Itani
ID: 201900604
Instructor: Ahmad Dhaini

'''
'''FUNCTIONS:'''
def eq(letter,k):
    if letter.isupper():
        position = ((ord(letter)-ord('A'))+k)%26+ord("A")
        return chr(position)
    elif letter.islower():
        position = ((ord(letter)-ord('a'))+k)%26+ord("a")
        return chr(position)
    else:
        return letter #IF THE LETTER IS NOT A LETTER (SPACE, COMMA,ETC...)
        
#################################################################
#################################################################

import sys

k = int(sys.argv[1])
word= sys.argv[2]
encrypt = "" 

##################################################################
##################################################################

for letter in word:
    encrypt +=eq(letter,k)
print(encrypt)
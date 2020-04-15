# Check to see if two provided strings are anagrams of eachother.
# One string is an anagram of another if it uses the same characters
# in the same quantity. Only consider characters, not spaces
# or punctuation.  Consider capital letters to be the same as lower case
# --- Examples
#   anagrams('rail safety', 'fairy tales') --> True
#   anagrams('RAIL! SAFETY!', 'fairy tales') --> True
#   anagrams('Hi there', 'Bye there') --> Fals

import re

def anagrams(str1, str2):

    str1 = list(re.sub('[^a-zA-Z0-9 \n\.]', '', str1).lower())
    str1.sort()
    res1 ="".join(str1)


    str2 = list(re.sub('[^a-zA-Z0-9 \n\.]', '', str2).lower())
    str2.sort()
    res2 = "".join(str2)

    return res2 == res1



#print(anagrams('RAIL! SAFETY!', 'fairy tales'))

#anagrams("Herl%$@!","Herl")

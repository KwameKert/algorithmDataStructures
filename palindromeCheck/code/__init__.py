#check if string is palindrome

#Time O(n) | Space O(1)
def palindromeCheck(string):

    #declare pointers here
    left = 0
    right = len(string) -1

    #loop through string
    while left < right:
        #check if index left is same as index of right
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    #return true is palindrom
    return True



print(palindromeCheck("abcdcba"))

#caesar encryptor


def caesarEncryptor(string, key):

    newString = []

    #generate new key
    newKey = key % 26

    #for each loop get new letter
    for letter in string:
        newString.append(getNewLetter(letter, key))

    return "".join(newString)




def getNewLetter(letter, key):

    #convert letter to code with key
    newLetterCode = ord(letter) + key

    #return new character
    return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode%122)



print(caesarEncryptor("xyz", 2))

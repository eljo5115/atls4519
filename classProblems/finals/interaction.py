"""
Author: Eli Jordan
Class: ATLS 4519 - Special Topics - (Im)practical Programming
Project #21: Interactive Cypher Program
Sorry no comments, check the notebooks in the GitHub for more thorough documentation.
"""


import math


def reverseCypher(string):
    return string[::-1]

def caesarCypher(string, key):
    letters = "abcdefghijklmnopqrstuvwxyz"
    key = int(key)
    string = string.lower()
    newString = ""
    for i in range(len(string)):
        if string[i] in letters:
            letterIndex = letters.index(string[i]) + key
            if letterIndex > len(letters)-1:
                letterIndex = letterIndex - len(letters)
            newString += letters[letterIndex]
        else:
            newString += string[i]
        
    return newString

def caesarBruteForce(phrase):
    english = False
    with open("../resources/2of4brif.txt") as f:
        dictionary = f.read()
    
    for i in range(1,26):
        isWord = []
        output = ""
        work = caesarCypher(phrase,i)
        key = i
        work = work.split()
        for word in work:
            if word in dictionary and len(word) > 4:
                return work

def transpositionCypher(phrase, key):
    i = 0
    key = int(key)
    rows = math.ceil(len(phrase)/key)
    newPhrase = ""
    while i < key:
        j = 0
        while j < rows:
            value = i + (key*j)
            if value >= len(phrase):
                break
            newPhrase+= phrase[value]
            j+=1
        i+=1
    return newPhrase

def transpositionDecypher(phrase, key):
    i = 0
    key = int(key)
    numColumns = math.ceil(len(phrase)/(key))
    numRows = key
    shadedBoxes = numColumns*numRows - len(phrase)
    newPhrase = [""] * numColumns
    column = 0
    row = 0

    for symbol in phrase:
        newPhrase[column] += symbol
        column += 1
        if (column == numColumns) or (column == numColumns -1 and row >= numRows - shadedBoxes):
            column = 0
            row += 1

    output = ''
    for part in newPhrase:
        output += part
    return output

def transpositionBruteForce(message):
    for i in range(1, len(message)):
        print(transpositionDecypher(message,i), i)

def substitutionCypher(phrase, keyIndex, decrypt=False):
    letters = "abcdefghijklmnopqrstuvwxyz"
    output = ""
    if not decrypt:
        for i in range(len(phrase)):
            if phrase[i] in letters:
                place = letters.index(phrase[i])
                output += keyIndex[place]
            else:
                output+=phrase[i]
        return output
    elif decrypt:
        for i in range(len(phrase)):
            if phrase[i] in letters:
                place = keyIndex.index(phrase[i])
                output += letters[place]
            else:
                output+=phrase[i]
        return output

def affineCypher(phrase, a, b, decrypt=False):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .,!?-/$%"
    output = ""
    a,b = int(a),int(b)
    while math.gcd(len(letters),a) !=1:
        input("Enter a new key (must be coprime to 61):")
    if decrypt:
        a = pow(a,-1,len(letters)) #modulo inverse of a 
        for letter in phrase:
            if letter in letters:
                index = letters.index(letter)
                newIndex = a*(index-b)%len(letters)
                output += letters[newIndex]
            else:
                output += letter
        return output
    
    for letter in phrase:
        if letter in letters:
            index = letters.index(letter)
            newIndex = (a*index + b)%len(letters)
            output += letters[newIndex]
        else:
            output += letter
    return output

def vigenereCypher(phrase,keyWord, decrypt = False):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .,!?-/$%"
    keys = []
    output = ""
    if decrypt:
        for i in range(len(phrase)):
            keys.append(-(letters.index(keyWord[i%len(keyWord)])))
        for i in range(len(keys)):
            letter = phrase[i]
            if letter in letters:
                output += caesarCypher(letter,keys[i])
            else:
                output += letter
        return output
    for i in range(len(phrase)):
        keys.append(letters.index(keyWord[i%len(keyWord)]))
    for i in range(len(keys)):
        letter = phrase[i]
        if letter in letters:
            output += caesarCypher(letter,keys[i])
        else:
            output += letter
    return output
def viginereBruteForce(phrase):
    #iterate through 2of4brif and try all words
    pass

def main():
    running = True
    while running:
        userInput = input("Would you like to encrypt or decrypt? (type 'encrypt' or 'decrypt')\nType 'exit' to end the program.\n")
        if userInput == "encrypt":
            userInput = input("What would you like to encrypt? (type 'file', or 'text')\n")
            if userInput == "file":
                pass
                #do something to input a file idk
            elif (userInput == "text"):
                userInput = input("Which cypher would you like to use? ('caesar' 'viginere' 'affine' 'substitution')\n")
                userText = input("Enter text to encrypt:\n")
                if userInput == "caesar":
                    key = input("Enter the key:\n")
                    print(caesarCypher(userText,key))
                elif userInput == "viginere":
                    key = input("Enter the key word:\n")
                    print(vigenereCypher(userText,key))
                elif userInput == "affine":
                    key1 = input("Enter the first key:\n")
                    key2 = input("Enter the second key:\n")
                    print(affineCypher(userText,key1,key2))
                elif userInput == "substitution":
                    alphabetKey = input("Enter the index key:\n")
                    print(substitutionCypher(userText,alphabetKey))
                else:
                    print("Choice invalid. Enter a valid choice ('caesar' 'viginere' 'affine' 'substitution')\n")
            else:
                print("Choice invalid. Enter a valid choice ('file' or 'text').\n")  
        elif userInput == "decrypt":
            userInput = input("What would you like to decrypt? (type 'file', or 'text')\n")
            if userInput == "file":
                pass
            #do something to input a file idk
            elif (userInput == "text"):
                userInput = input("Which cypher would you like to decrypt? ('caesar' 'viginere' 'affine' 'substitution' 'idk')\n")
                print(userInput)
                if userInput == "caesar":
                    userText = input("Enter text to decrypt:\n")
                    key = int(input("Enter the key:\n"))
                    print(caesarCypher(userText,-(key)))
                elif userInput == "viginere":
                    userText = input("Enter text to decrypt:\n")
                    key = input("Enter the key word:\n")
                    print(vigenereCypher(userText,key,True))
                elif userInput == "affine":
                    userText = input("Enter text to decrypt:\n")
                    key1 = input("Enter the first key:\n")
                    key2 = input("Enter the second key:\n")
                    print(affineCypher(userText,key1,key2,True))
                elif userInput == "substitution":
                    userText = input("Enter text to decrypt:\n")
                    alphabetKey = input("Enter the index key:\n")
                    print(substitutionCypher(userText,alphabetKey,True))
                else:
                    print("Choice invalid. Enter a valid choice ('caesar' 'viginere' 'affine' 'substitution')\n")
        elif userInput == "exit":
            break
        else:
            print("Choice invalid. Enter a valid choice ('file' or 'text').\n")

if __name__ == "__main__":
    main()
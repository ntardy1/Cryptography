
# Program to generate a password which is really just a randomized string of character with some slight customization

import random
import math

# Estbalishing some critical variables
lowerLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
upperLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
allLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbersList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
specialsList = ['!', '@', '#', '$', '%', '^', '&', '*']
passwordList = []

lengthInput = int(input("Length of Password: "))
passwordLength = lengthInput

numbersInput = int(input("Quantity of numbers: "))
specialsInput = int(input("Quantity of special characters: "))
for elem in range(0, numbersInput):
    x = random.randint(0, len(numbersList) - 1)
    passwordList.append(numbersList[x])

for elem in range(0, specialsInput):
    y = random.randint(0, len(specialsList) - 1)
    passwordList.append(specialsList[y])

passwordLength -= len(passwordList)
for elem in range(0, passwordLength):
    z = random.randint(0, len(allLetters) - 1)
    passwordList.append(allLetters[z])

random.shuffle(passwordList)
passwordList = [str(i) for i in passwordList]

passWord = "".join(passwordList)

print(f'The password is: {passWord}')

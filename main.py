#Author: Andrew Ramirez
#Project 1 CS 457
#Date: 9/23/2022

import os

while True:
    #input takes the whole line from the user including endline
    userInput = input()
    userInput = userInput.replace(";", "")
    tokens = userInput.split()

    print(tokens)

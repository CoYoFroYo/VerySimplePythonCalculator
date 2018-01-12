'''
    Program: My Calculator
    Author: Cody York
'''

import re

print("***** My Calculator ******")
print("****** Type 'quit' to exit ****** \n")


previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""

    #if there has been a previous calculation, use that result at the prompt
    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))

    #if user quits ->
    if equation == 'quit':
        print("Goodbye, human.")
        run = False
    else:
        equation = re.sub('[a-zA-z,.:()" "]',' ', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

while run:
    performMath()

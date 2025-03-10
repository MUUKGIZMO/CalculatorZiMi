#Hi. This is Mynia's first python project on windows.
# The dates is 03/06/2025.
# I will be designing a calculator app...>.>
# Create a function that allows user to select addition sign/operator on their keyboard
def add(a: int, b: int) -> int:

    while True:
        add = input("+")
        result = a + add + b

    return result

# Now subtract
def subtract(a: int, b:int) -> int:

    while True:
        subtract = input("-")
        result = a + subtract + b
        
    return result

#Multiply
def multiply(a: int, b: int) -> int:

    while True:
        multiply = input("*")
        result = a + multiply + b

    return result

#Divide
def divide(a: int, b:int) -> int:

    while True:
        divide = input("/")
        result = a + divide + b

    return result



#--------------------------------------------------------------------------------------------
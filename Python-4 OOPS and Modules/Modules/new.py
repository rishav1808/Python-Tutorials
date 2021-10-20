
'''
    There are various ways of importing a module in Python
    Way-->1
    import calculator
    here we can call the definations by using calculator.additon(2,3)

    Way-->2
    from calculator import additon,subtraction
    Now from the calculator module we can only use
'''
from calculator import addition


print(addition(4,2))
# Here the rest of the definations of calculator module can't be used like: 
print(calculator.subtraction(2,3))
'''
    Way-->3:
            from calculator import *
            Here all the definations of the module calculator are called
            Not a good practice
    Way-->4:
        from calculator import (
            addition,
            subtraction,
            multiplication
        )
        Only used for better readability of the code, a Syntactical Sugar
    Way -->5: Using Alias
    import calculator as cal
    If any function of the same name calculator is used then this method of alias is very effective
    
    Way -->6
    from calculator import (
        addition as add
        subtraction as sub
    )
'''
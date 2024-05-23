#Exceptions are errors while running the code
print("Exception handling")
'''
# Zero division exception handling 
try:
    a = 10/0
except ZeroDivisionError:
    print("Exception has been handled successfully")'''
'''
#String Concatenation with int 
a = input("Enter Text ")
try:
    b = 10+a
except TypeError:
    print("Exception has been handled successfully")'''

'''
#Name Error Exception handling
try:
    print(a)
except NameError as N:
    print("Name Error :",N)'''
'''try:
    print(a)
except ZeroDivisionError:
    print("Exception has been handled successfully")
except NameError as N:
    print("Name Error :",N)'''
'''
# using else and finally block
try:
    print(a)
except NameError as N:
    print("Name Error :",N)
else:
    print("a is not defines")
finally:
    print("inside Final Block")'''
'''
# Raise Exception
try:
    raise ZeroDivisionError
except ZeroDivisionError as z:
    print("Exception Handled",z)'''

age = int(input("Enter Age "))
try:
    if age<6:
        raise ValueError("Not eligible for Admission")
    else :
        print("eligible for admission")
except ValueError as V:
    print("Exception has been taken care : ",V)

print("Last line of program")
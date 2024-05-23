from OOPs_Python.Modules import Caluculator as cl

#to know how many functions in particular module
print(dir(cl))
'''
r1 = cl.Add(17,18)
print(r1)

r2 = cl.Subtraction(17,18)
print(r2)

r3 = cl.division(17,18)
print(r3)

'''

# if the functions is in classes need to fallow below process

obj1 = cl.A
obj2 = cl.B
r1 = obj1.Add(1,2)
print(r1)
r2 = obj1.Subtraction(4,5)
print(r2)
r3 = obj2.division(8,4)
print(r3)
r4 = obj2.Multiply(9,2)
print(r4)
# A function which has no name and can take any number of arguments and one expression is lambda function

sum = lambda a,b :a+10+b

print(sum(5,4))

# This code used to filter the odd numbers from the given list
list_ = [35, 12, 69, 55, 75, 14, 73]
odd_list = list(filter( lambda num: (num % 2 != 0),list_))
print('The list of odd number is:',odd_list)


#Code to calculate the square of each number of a list using the map() function
numbers_list = [2, 4, 5, 1, 3, 7, 8, 9, 10]
squared_list = list(map( lambda num: num ** 2 , numbers_list ))
print( 'Square of each number in the given list:' ,squared_list )


#Code to calculate square of each number of lists using list comprehension
squares = [lambda num = num: num ** 2 for num in range(0, 11)]
# in the above line every element is a function so while calling it we calling every element as function
print(type(squares))
print('The square value of all numbers from 0 to 10:',end=" ")
for square in squares:
       print(square(),end=" ")


# Code to use lambda function with if-else
Minimum = lambda x, y : x if (x > y) else y
print('The greater number is:', Minimum( 35, 74 ))
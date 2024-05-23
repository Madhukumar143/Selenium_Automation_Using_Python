import re

pattern = "[Mm]adhu" #first letter can be M and m so used[]
#[a-z] or [1-9]
#[^0-9] not of 0-9
#[s[^aeiouAEIOU]t without vowels
#/d should be digit /D should not be a digit
#/w [a-z,0-9,A-Z] /W nothing from[a-z,0-9,A-Z]
# if pattren = "^My" Should start with My
# if pattren = "Madhu$" Should End with Madhu
# pattren = "M..y" .. can be any charecters but should be any charecter if you did not giv any char
#pattern "^My...Madhu$" Starts with My and Ends with Madhu by 3 chars at the middle
# ? -> 0 or 1 char
#.{2} exactly two chars
# pattern = "Python|Java" it should be either of Python or Java
# .* means o aor any number of chars .+ one or more number of chars
text = input("Enter your input here : ")

if re.search(pattern,text):
    print("Pattern got matched")
else:
    print("Pattern Did not matched")
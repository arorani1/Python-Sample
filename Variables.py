#Variable is a reserved memory location to store values.
#There is no need for declaring the variable in Python. It is automatically interpreted on the basis of value.
x=7
print(type(x))
print(f"value of x: {x}")
y=5.25
print(type(y))
z=(x+2)+(4*y)
print(type(z))
print(f"{z}")

#To re-declare a variable, we don't have to explicitely mention it.
x=14
print(f"value of x: {x}")

#If a variable is no more in use, we can delete it.
print(f"value of x before deleting: {x}")
del x
'''print(f"value of x after deleting: {x}")'''
#If you try printing thevalue of 'x' now, it will throw an error.

'''
Rules for naming a variable:
1. It can use alphabet, number or underscore.
2. It must not be a keyword like if, else, for, etc.
3. It must not contain space.
4. It must not start with a number
5. It is case-sensitive.
6. It can start with underscore.
'''

x=4
X=7
print(f"value of x:{x}")
print(f"value of X:{X}")

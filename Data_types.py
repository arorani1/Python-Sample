#Every variable in Python has a data type.
x=10
print(f"Memory Location of x: {id(x)}")
#id(variable) gives the memory location of that particular variable.

'''Basic Data types in python:
1.  Numbers (int, float, complex)
2.  Strings
3.  Boolean
'''
a=3;b=3.5;c=3+5j
name='Nishant'
print(f"value of a: {a}")
print(f"value of b: {b}")
print(f"value of c: {c}")
print(f"value of name: {name}")
print(f"variable type of a: {type(a)}")
print(f"variable type of b: {type(b)}")
print(f"variable type of c: {type(c)}")
print(f"variable type of name: {type(name)}")

#Type-casting or data type conversion
x=60
y=str(x)
z=bool(x)
print(f"Value & Type of x:{x}, {type(x)}")
print(f"Value & Type of y:{y}, {type(y)}")
print(f"Value & Type of z:{z}, {type(z)}")

'''Note: Any data type can be converted to boolean.
    bool(any_data_type)= True or False
    bool(empty)=False => bool(0),bool(None),bool([]),bool(()),bool({})
    bool(non-empty)= True'''
#Example:
x=""
print(bool(x))


'''Any data type can be converted to string, reverse is not possible.
    Example: We can convert integer to string but string to integer is not possible'''

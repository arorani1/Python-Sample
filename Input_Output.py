#Input and Output
'''eval function will automatically take the data type on the basis of input'''
a=eval(input("Enter the 1st value: "))
print(f"{type(a)}")
b=eval(input("Enter the 2nd value: "))
c=(a+b)
print(f"Addition of {a} and {b} is: {c}")

#OR you can explicitely mention the data type for input.
x=int(input("Enter the 3rd value: "))
'''Now while input if you try entring a String as an input, it will throw an error'''

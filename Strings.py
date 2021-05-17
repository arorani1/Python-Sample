'''Usage of Strings'''
my_name='Nishant'
my_new_name="Python3"
#If there is paragraph, better to use three single quotes. It will print the string as it is written
my_info='''My name is Nishant and
I work at Unisys'''
print(f"{my_name}, {my_new_name}, {my_info}")

#Accessing a character in a string through index values
my_script='Python Scripting'
print(f"{my_script[0]}")
print(my_script[5])
#Printing characters from 0 to some value
print(my_script[0:6])
#Printing characters from 0 to last character
print(my_script[0:])

'''Strings are immutable. This means that elements of a string cannot be changed once it is assigned. We can simply reassign different strings to the same name.'''
#Example: my_script[0]="A" will throw an error

'''Length of a string'''
string_length=len(my_script)
print(f"Length of my_script String is : {string_length}")

'''Concatenation of two strings'''
str1="Python"
str2="Scripting"
str3=str1+" "+str2
print(f"Concatenation of string: {str3}")

#Understanding join, center & zfill(zero fill)
str1="Python"
str2="Python Scripting"
#To add something between the characters of a string, we use join.
print("-".join(str1))
print("*".join(str1))
#To place a string in the center in a defined length, we use center
print(str1.center(20))
print(str2.center(20))
#To add 0 in the starting to a defined length of a string, we use zfill. It is called Padding.
print(str1.zfill(10))

#To remove any character from starting or ending of a string, we use strip.
print(str1.strip('Py'))
str3="  Python "
print(str3)
print(str1.strip())
#Note: We can remove from starting by mentioning lstrip and from ending by mentioning rstrip.

#To separate each word in a string, we use split. Te output is in the form of list
str4="Python for scripting"
print(str4.split())
print(str4.split("for"))

#To check how many times a character is appearing in a string.
print(str4.count("t"))

#To check the index value of a character in a string.
print(str4.index("P"))
print(str4.index("t",4))

import os
os_type=os.get_terminal_size().columns
print(os_type)
str1="python"
print(dir(str1))
print(len(str1))
print(str1.title().ljust(os_type))
print(str1.title().center(os_type))
print(str1.title().rjust(os_type))

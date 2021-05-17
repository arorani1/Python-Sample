'''Data Structures is used to store a collection of data.
It is mainly of 4 types:
1.  List -> []
2.  Tuples -> ()
3.  Directory -> {} with key value pair
4.  Set -> {}
'''

#List in Python
my_list=[]
my_list_1=[2,5,"python"]
print(bool(my_list))
print(bool(my_list_1))
print(my_list_1[2])
print(my_list_1, type(my_list_1))
'''We can change the index value in the list'''
#Example:
my_list_1[0]=9
print(my_list_1)
'''We can check the index value of data in a list'''
#Example
print(my_list_1.index("python"))

'''We can count values in a list'''
#Example
list=[3,4,5,6,5,3,6]
print(list.count(3))

'''We can clear the list'''
#Example
print(list.clear())

#------------------------------------------------
#------------------------------------------------
'''In the below case, both list1 and list2 are pointing to same memory address'''
list1=[1,2,3,4,5]
list2=list1
print(f"List2: {list2}")
print(f"Memory Address of list1: {id(list1)}\nMemory Address of list2: {id(list2)}")

'''In the below case, a new memory location is created for list3 which points to memory location of list1'''
list3=list1.copy()
print(f"list3: {list3}")
print(f"Memory Address of list1: {id(list1)}\nMemory Address of list3: {id(list3)}")

'''To add some data to the end, we use append'''
lists=[1,2,3,4,5]
print(lists)
lists.append(45)
print(f"lists: {lists}")
'''To add some data in the list on the basis of index, we use insert'''
lists.insert(1,90)
print(lists)

'''Adding list data to a list'''
lists.append(my_list_1)
print(lists)
'''Adding data of a list to another list'''
my_list_1.extend(list)
print(my_list_1)

'''Reversing a list'''
list_reverse=[1,2,3,4,3]
list_reverse.reverse()
print(f"Reversing the list: {list_reverse}")
list_reverse.sort()
print(list_reverse)

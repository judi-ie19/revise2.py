a = [18, 52, 23, 41, 32]    
smallest = min(a)
print(smallest) 

def duplicates():
  list_x=[10,20,30,10,40,50,20]
  new_list=[]
  for n in list_x:
    if n not in new_list:
      new_list.append(n)
      print(new_list) 
duplicates()

#  Write a Python program to append a list to the second list.

# Use num = [10,5,3,78,13,56,2,9,8,4]

# Write a python program to print the numbers of a specified list after removing even numbers
# numbers=[1,2,3,4,5,6,7,8,9]
# other_numbers=[]
# for x in numbers:
#       if x%2==0:
#             print(x)
#       else:
#             other_numbers.append(x)
#             print(other_numbers)
# Write a python program to print the numbers of a specified list after removing even numbers
numbers=[1,2,3,4,5,6]
numbers=[x for x in numbers if x%2!=0]
print(numbers)

#  Write a Python program to append a list to the second list.
list1=[1,2,3,4,5,6,7] 
list2=['apple','mango','watermelon','orange']
final_list=list1+list2
print(final_list)

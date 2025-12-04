marks=[12.5, 15.0, 9.5, 18.0, 14.0]
print(marks)
print(type(marks))
# Accessing elements
print(marks[0])  # First element
print(marks[2])  # Third element
print(marks[-1]) # Last element
print(marks[-3]) # Third last element
print(len(marks)) # Length of the list

student=["Sarhan", 21, "Apna College", "third year"]
print(student)
# Modifying elements
student[1]=22
print(student)
# Slicing
print(student[0:2]) # First two elements
print(student[1:])  # From second element to end
print(student[:3])  # Up to third element
print(student[-2:]) # Last two elements
# List methods
list2=[5, 2, 9, 1, 5, 6]
list2.append(10)  # Add element at the end
print(list2)
list2.insert(2, 15) # Insert 15 at index 2
print(list2)
list2.remove(5)  # Remove first occurrence of 5
print(list2)
popped_element=list2.pop() # Remove and return last element
print(popped_element)
print(list2)
list2.sort()  # Sort the list
print(list2)
list2.reverse() # Reverse the list
print(list2)
index_of_9=list2.index(9) # Get index of first occurrence of 9
print(index_of_9)
count_of_5=list2.count(5) # Count occurrences of 5
print(count_of_5)
list2.sort()
print("Sorted list:", list2)
list2.reverse()
print("Reversed list:", list2)

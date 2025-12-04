#Tuples are immutable sequences, typically used to store collections of heterogeneous data.
#They are defined by enclosing the elements in parentheses ().
marks = (12.5, 15.0, 9.5, 18.0, 14.0)
print(marks)
print(type(marks))
# Accessing elements
print(marks[0])  # First element
print(marks[2])  # Third element
print(marks[-1]) # Last element
print(marks[-3]) # Third last element
print(len(marks)) # Length of the tuple     
# Slicing
print(marks[0:2]) # First two elements
print(marks[1:])  # From second element to end
print(marks[:3])  # Up to third element
print(marks[-2:]) # Last two elements
# Tuples methods
tuple2 = (5, 2, 9, 1, 5, 6)
print(tuple2)
index_of_9 = tuple2.index(9) # Get index of first occurrence of 9
print(index_of_9)
count_of_5 = tuple2.count(5) # Count occurrences of 5
print(count_of_5)
# Note: Tuples do not support methods that modify the data, such as append, insert, remove, pop, sort, or reverse,
# because they are immutable.
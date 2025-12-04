#WAP user to enter name of three favorate movies and store them in a list.
movies = []  # Initialize an empty list to store movie names   
for i in range(3):
    movie = input("Enter the name of your favorite movie: ")  # Prompt user for movie name
    movies.append(movie)  # Add the entered movie name to the list
print("Your favorite movies are:", movies)  # Display the list of favorite movies   

#WAP to check if a list contains a palindrome of elements or not.
list4=[1,2,1]
list5=[1,2,3]

copy_list4=list4.copy()  # Create a copy of list4
copy_list4.reverse()  # Reverse the copied list
if list4==copy_list4:  # Check if the original list is equal to the reversed copy
    print("list4 contains a palindrome")
else:
    print("list4 does not contain a palindrome")    

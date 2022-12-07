# WAP to create a list of the cubes of only the even integers appearing in the input list
# (may have elements of other types also) using the following:

list1 = [10, 21, 4, 45, 66, 93]

# for loop method
for num in list1:
    
    if num % 2 == 0:
	        print(num, end=" ")


# list comprehension method
even_nos = [num for num in list1 if num % 2 == 0]

print("Even numbers in the list: ", even_nos)


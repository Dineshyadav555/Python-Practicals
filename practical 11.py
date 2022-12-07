# Write a function that accepts two strings and returns the indices of all the occurrences
# of the second string in the first string as a list. If the second string is not present in the
# first string then it should return -1.

def printIndex(str, s):
 
    flag = False;
    for i in range(len(str)):
        if (str[i:i + len(s)] == s):
             
            print( i, end =" ");
            flag = True;
 
    if (flag == False):
        print("NONE");
              
str1 = input('Enter 1st String: ')
str2 = input('Enter 2nd String: ')
printIndex(str1, str2);
 
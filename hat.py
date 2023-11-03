#There once was a hat. The hat contained no rabbit, but a list of five numbers: 1, 2, 3, 4, and 5.
#Your task is to:
#write a line of code that prompts the user to replace the middle number in the list with an integer number entered by the user (step 1)
#write a line of code that removes the last element from the list (step 2)
#write a line of code that prints the length of the existing list (step 3.)

list = [1, 2, 3, 4, 5, 6, 7]
print("Introduceti numarul pe care vreti sa il introduceti pe pozitia din mijloc:")
a=int(input())
b=len(list)
c=b
print(b)
b=b//2
list[b]=a
print(list)
del(list[c-1])
print(list)
print(len(list))
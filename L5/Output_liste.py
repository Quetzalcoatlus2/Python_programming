lst = ["D", "F", "A", "Z"]
lst.sort()
print(lst)

a = 3 
b = 1 
c = 2 
lst = [a, c, b] 
lst.sort() 
print(lst)

a = "A" 
b = "B" 
c = "C" 
d = " " 
lst = [a, b, c, d] 
lst.reverse() 
print(lst)

myList = [17, 3, 11, 5, 1, 9, 7, 15, 13] 
largest = myList[0] 
for i in myList: 
    if i > largest: 
        largest = i 
print(largest)

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
toFind = 5 
found = False 
for i in range(len(myList)): 
    found = myList[i] == toFind 
    if found: 
        break 
if found: 
    print("Element found at index", i) 
else: 
    print("absent")

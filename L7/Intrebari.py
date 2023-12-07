myTup = (1, 2, 3)
print(myTup[2])

tup = 1, 2, 3
a, b, c = tup
print(a * b * c)

tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)
print(duplicates)

d1 = {'Adam Smith':'A', 'Judy Paxton':'B+'}
d2 = {'Mary Louis':'A', 'Patrick White':'C'}
d3 = {}

for item in (d1, d2):
	 d3.update(item)

print(d3)

l = ["car", "Ford", "flower", "Tulip"]

t = tuple(l)
t.append
print(t)

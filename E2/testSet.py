
a = set()
a.add(0)
a.add(4)

b = set()
b.add(4)
# b.add(0)

print(a)
print(b)
c = a.issuperset(b)
print(c)
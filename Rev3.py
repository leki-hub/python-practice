a = {1, 2, 3}
b = {3, 4, 5}
c = a | b
print(*c)
print(c)
print(a.union(b))
print(a.symmetric_difference(b))
print(a.difference(b))
s = {1, 2, 3, 4, 4, 4, 6, 6, 6, 54, 4, 5, 56, 54, 4, 4, 4}
s2 = {1, 2, 3, 45, 6, 4, 78, 4}
s3 = {1, 2, 3, 4}
s4 = {100, 200, 300}
print(s)
print(type(s))

# builtin functions

s4.add(400)
print(s4)

print(s.intersection(s2))
print(s2.symmetric_difference(s))
print(s3.union(s4))
print(s3.issubset(s))
print(s.issuperset(s3))
print(s3.isdisjoint(s4))


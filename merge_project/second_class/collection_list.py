# Data Structure -> list, tuple, set, dictionary

l = [1, 2, 3, 4.5, 5.5, 6.5, "7", "8", "9", True, False]

# indexing

print(l[0])
print(l[10])
print(l[len(l) - 1])

# slicing

print(l[2:8])
print(l[2:8:2])

print(l[-1])
print(l[-4:-1])
print(l[::-1])

# nested list
nes_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nes_list[1])
print(nes_list[1][0])

# builtin functions

l.append(100)
print(l)
l.extend([200, 300, 200])
print(l)

print(l.index(200))
print(l.count(200))

print(l.pop())
print(l)
print(l.pop(10))
print(l)

print("Removed item: ", l.remove(True))


# mutable

l[0] = 1000

print(l)

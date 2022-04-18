# LIST, TUPLE, SET, DICTIONARY

L = [1, 2, 3, 4.5, 5.5, 6.5, "Seven", "Eight", "Nine", True, False]

print(len(L)-1)


# index
print(L[0])
print(L[1])
print(L[2])
print(L[10])
# print(L[11])

# slicing
print(L[2:7])
print(L[::2])
print(L[-6:-1])
# reverse
print(L[::-1])

# nested list
nes_1 = [[1, 2, [3.1, 3.2, 3.3]], [4, 5, 6], [7, 8, 9]]
print(nes_1[0])
print(nes_1[0][1])
print(nes_1[0][2][1])

# L.append([100, 200])
L.extend([100, 200, 300])
# for i in [100, 200, 300]:
#     L.append(i)
print(L)

l = L.copy()
print(l)
print(l.index(100))

l = [10, 29, 37, 1, 4, 67, 2, 64, 3]
l.sort()
print(l)
l.reverse()
print(l)

print(l.pop())
print(l)
print(l.pop(0))
print(l)

print(l.remove(64), " from remove function")

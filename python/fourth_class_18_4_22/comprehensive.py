l = [i ** 2 for i in range(20)]

print([i for i in "helloworld"])
print([i.upper() for i in "helloworld"])
print([i for i in ['This,', 'is,', 'our,', 'python,class,']])
print([i.split(",") for i in ['This,is,our,python,class']])
print([i if i in 'aeiou' else 'c' for i in "apple"])
print([sorted(i) for i in [[3, 1], [8, 1], [4, 9], [0, 1]]])
print([i for i in range(20) if i % 2 == 0])
print([i if i % 2 == 0 else "Odd" for i in range(20)])

print("*" * 50)
print([2 * (s if s % 2 == 0 else -1) + 1 for s in range(20)])
print([i if i > 5 else "#" for i in range(20)])
print([i if (i > 5 and i % 2 == 0) else "#" for i in range(20)])

# print(l)

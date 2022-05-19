d = {"key1": "Value1", "key2": "Value2", "key3": "Value3", 1: 100, 2.5: 250}

print(d['key1'])
print(d['key2'])
print(d[1])
print(d[2.5])

# builtin functions
print(d.get("key1"))
print(d.keys())
print(d.values())
print(d.items())
for key, value in d.items():
    print(key, "=>", value)

d.update({"key4": "NewValue"})
print(d)

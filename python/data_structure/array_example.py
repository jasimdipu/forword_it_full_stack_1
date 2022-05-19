import array

arr = array.array('i', [1, 2, 3, 4, 5])

# int[] arr = new int[10]();

for i in range(5):
    print(arr[i])

arr.append(7)

for i in range(len(arr)):
    print(arr[i])

    
print(arr.pop(2))

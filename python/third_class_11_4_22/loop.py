# loop -> for, while

# for i in range(0, 101, 10): # start 0, stop = user, step = 1
#     print(i*2)

i = 0
n = 10

# break, continue

while i < n:
    i = i + 1
    if i == 5:
        continue
    print(i)

    # if i == 15:
    #     break

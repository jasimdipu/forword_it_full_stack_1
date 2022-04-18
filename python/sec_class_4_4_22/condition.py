# if | elif | else
nid = True
# age = int(input())
age = 18

print(type(age))
# nested
if age >= 18:
    print("Age is perfect? do you have nid?")
    if nid == True:
        print("NID is ok")
    else:
        print("Entry Restricted")
else:
    print("age is under 18")

# operators -> ==, <, >, <=, >=, !=,
# logic gate -> and(&) or(|), not(!)

# ladder

cgpa = 3

if cgpa >= 0 and cgpa < 2:
    print("F")
elif cgpa >= 2 and cgpa < 4:
    print("B")
elif cgpa >= 4 and cgpa <= 5:
    print("A")
else:
    print("fail")

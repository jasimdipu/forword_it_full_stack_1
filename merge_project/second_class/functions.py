def func1():
    print(100 * 100)


def getname(name):
    print(name)


def get_info(name, age, address):
    print(name, age, address)


def getnumbers(*num):
    print(num)


def get_infos(**info):
    for key, values in info.items():
        print(key, ":", values)


def print_vs_return(num):
    print(num)


def return_vs_print(num):
    return num


func1()
getname("Abul kalam")
get_info("Tamim", 34, "Chittagong")
getnumbers(100, 200, 34, 3, 45, 3, 4, 3, 546, 4, 56, 4, 56, 4, 56, 4, 432)
get_infos(name="Asis", age=25, address="nator")

print_vs_return(100)
val2 = return_vs_print(10)

print(val2*20)

s = "Hello "+"world"

print(s)

# def get_info():
#     name = "Md Hamid"
#     address = "Dhaka"
#     print("Name: ", name, "Address: ", address)
#
# def get_info(name, address="Dhaka", Thana = "Uttara"):
#     # name = "Md Hamid"
#     # address = "Dhaka"
#     print("Name: ", name, "Address: ", address, "Thana :", Thana)
#
#
# get_info("Md Hamid")
# get_info("Md Rasel", "Kishorgonj")
# get_info("Md Harun")
#
# def get_numbers(*args, **kwargs):
#     print(args)
#     print(kwargs)
#     print(type(args))
#
#
# def get_list(l):
#     print(l)
#
#
# get_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, [1, 2, 3, 54], [3, 5, 67, 344, 78, 89], name="Hasan", age=24)
# get_list([1, 2, 3, 4, 5, 6, 7, 89, 9])
#
# def func1(*args):
#     # print("Outter function")
#     var = args
#     a = var[2:5]
#     def func2(*args):
#         print(args)
#     return func2(a)
#
#
# # func1()
#
# test_fuc = func1
# test_fuc(1, 2, 33, 5, 7)
#
# # difference between return and print
#
# def get_number_1(number):
#     return number
#
#
# def get_number_2(number):
#     print(number)
#
#
# print(get_number_1(10)*10)
# get_number_2(100)*20
#
"""
get_number = lambda x, y: x+y if x > 50 else y

print(get_number(30, 40))
"""


summ = 0
for i in range(10):
    summ += i
print(summ)


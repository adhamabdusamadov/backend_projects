# # 1

# for i in range(1, 101):
#     print(i)

# i = 0

# while i < 101:
#     print(i)
#     i += 1

# # 2

# for i in range(1, 100):
#     if i % 3 == 0:
#         print(i)

# # 3

# def maxnum(num1, num2, num3, num4, num5):
#     print(max(num1, num2, num3, num4, num5))    

# maxnum(1, 2, 3, 4, 5)

# # 4

# def minnum(num1, num2, num3, num4, num5):
#     print(min(num1, num2, num3, num4, num5))    

# minnum(1, 2, 3, 4, 5)

# # 5

# orderlist = []
# unorderlist = []

# for i in range(1, 101):
#     if i % 2 == 0:
#         orderlist.append(i)
#     elif i % 2 == 1:
#         unorderlist.append(i)

# print(orderlist, unorderlist)

# # 6

# def numberscount(number):
#     count = 0
#     while count < number:
#         print(count)
#         count += 1

# numberscount(7)

# # 7

# x = int(input("1 son kiriting: "))
# y = int(input("2 son kiriting: "))


# def numberscount_2(a,b):
#     while True:
#         if a >= b:
#             break
#         if a % 2 == 0:
#             print(a)
#         a += 1
# numberscount_2(x, y)

# # 8

# x = int(input("1 son kiriting: "))
# y = int(input("2 son kiriting: "))


# def numberscount_2(a,b):
#     while True:
#         if a >= b:
#             break
#         if a % 2 == 1:
#             print(a)
#         a += 1
# numberscount_2(x, y)


# # 9

# names = {
#     'Jack': 17,
#     'Mark': 23,
#     'Rick': 15
# }

# name = input('Enter the name: ')

# if name == names[name]:
#     print(f"your name is {name} and you're {names[name]} years old")
# else:
#     print("sorry we don't have that name")


# # 10

# names = {
#     'Jack': 17,
#     'Mark': 23,
#     'Rick': 15
# }

# name = input('Enter the name: ')

# if name == names[name]:
#     print(f"your name is {name} and you're {names[name]} years old")
# elif name != names[name]:
#     name_add = input("you want to add this name:")
#     if name_add == 'yes':
#         names.update(name)
#         name_age = int(input("we have added a name, now enter age (12+): "))
#         if name_age > 12:
#             names.update(name_age)
#             print("Congratulations, we are done adding the name!")
#     elif name_add == 'no':
#         print("we don't have that name(")

# # 11
# names = {
#     'Jack': 17,
#     'Mark': 23,
#     'Rick': 15
# }

# for keys in names.items():
#     print(keys)


# # 12

# a_names = {
#     'adham': 'a',
#     'jack': 'j',
#     'abdulaziz': 'a'
# }
# a = 'a'

# for i in a_names:
#     for j in i:
#         if a == i[0]:
#             print(f"a harfdan boshlanadigan ism {i}")
#             break

# # 13



# def sum(*numbers):
#     count = 0
#     for i in numbers:
#         count += i
#     print(count)
# sum(9, 5, 6)

# def multiply(*mnumbers):
#     mcount = 1
#     for j in mnumbers:
#         mcount *= j
#     print(mcount)
# multiply(2, 5, 6)


# 14

bozor = {
    'telefonlar': {
        'iphone': {
            'narx': 1000,
            'info': 'Iphone 12, 128gb black'
        },
        'samsung': {
            'narx': 900,
            'info': 'Samsung Galaxy S21, 128gb black'
        },
    },
    'kompyuterlar': {
        'hp': {
            'narx': 1500,
            'info': 'HP 15, 8gb ram, 512gb ssd'
        },
        'lenovo': {
            'narx': 1200,
            'info': 'Lenovo IdeaPad 3, 8gb ram, 512gb ssd'
        }
    }
}

print('kategotiyalar:', bozor.keys())

def shop():
    catalog = input('categoriya kiriting: ')
    if catalog == bozor[catalog]:
        print(bozor[catalog].values())

shop()

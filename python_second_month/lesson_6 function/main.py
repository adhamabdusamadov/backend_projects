# def my_func():
#     print("Hello World")


# function - bu biror bir amalni bajaruvchi kod bloki
# function - def kaliti bilan ochiladi
# def my_func():
# function - chaqirish uchun funcsiya nomi va () yoziladi

# def say_hello():
#     print("Hello")

# say_hello()





# home

a = int(input("son kiriting: "))
b = int(input("son kiriting: "))
c = int(input("son kiriting: "))

def numbers_count(a, b, c):
    if a > b and a > c:
        print(f"{a} eng katta son")
    elif b > a and b > c:
        print(f"{b} eng katta son")
    elif c > a and c > b:
        print(f"{c} eng katta son")

numbers_count(a, b, c)



# 1

numbers = [2, 4, 7, 8, 5, 1]

def numbers_count(numbers):
    count = 0

    for i in numbers:
        count += i
    print(count)

numbers_count(numbers)

# 2

number = [4, 6, 7, 8, 43, 1]

def numbers_multiply(number):
    total = 1
    for i in number:
        total *= i

numbers_multiply(number)

# 3

text = 'function'

def text_reverse(text):
    print(text[::-1])

text_reverse(text)


# 4


x = int(input("son kiriting: "))
y = int(input("2 son kiring: "))

def XdegreeY(x, y):
    print(x**y)

XdegreeY(x, y)

# 5

a = int(input('1 son kiriting: '))

def evennoteven(a):
    if a % 2 == 0:
        print('even')
    elif a % 2 == 1:
        print('not even')

evennoteven(a)

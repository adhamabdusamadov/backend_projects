# Задание на append():


my_list = []

my_list.append(4)
my_list.append(1)
my_list.append(5)
my_list.append(7)
my_list.append(3)

print(my_list)


# Задание на index():


names = ['Александр', 'Алексей', 'Михаил', 'Роман', 'Владислав']

print(names.index('Алексей'))


# Задание на insert():


countries = ['America', 'Japan', 'Canada']

countries.insert(1, 'Russia')

print(countries)


# Задание на pop():

my_list = [4, 32, 74, 654, 67, 6]

my_list.pop()

print(my_list)


# Задание на remove():

numbers = [1, 2, 3, 2, 4, 1, 2]

numbers.remove(2)

print(numbers)


# Комбинированное задание:

second_names =  []

second_names.append("Анна")
second_names.append("Лера")
second_names.append("Наталья")
second_names.append("Екатерина")
second_names.append("Александра")

print(second_names.index("Анна"))

second_names.insert(0, "Мария")

second_names.pop(3)

second_names.remove("Анна")

print(second_names)

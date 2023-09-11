# Задание по спискам:

my_list = []

my_list.append(4)
my_list.append(1)
my_list.append(5)
my_list.append(7)
my_list.append(3)


print(sum(my_list))

# Задание на индексацию списка:

name_list = ["Саша", "Миша", "Дима", "Витя"]

name_list.pop(2)

print(name_list)

# Задание на изменение значения элемента списка:

color_list = ['красный', 'синий', 'зеленый', 'голубой', 'желтый']

color_list.pop(1)
color_list.insert(1, 'оранжевый')

print(color_list)

# Задание на кортежи:

things_list = ['портфель', 'телефон', 'деньги', 'ноутбук', 'вода']

print(things_list[3])

# Задание на объединение списков:

fnumber_list = [1, 2, 3]
snumber_list = [4, 5, 6]

fsnumber_list = fnumber_list + snumber_list

print(fsnumber_list)

# Задание на поиск элемента в списке:

num_list = [4, 3, 8, 9, 2, 1, 7, 5, 10, 6, 0]

if 7 in num_list:
    print("7 имеется в list")
else:
    print("7 не имеется в list")


# Задание на срезы списка:

second_num_list = [4, 3, 8, 9, 2, 1, 7, 5, 10, 6, 0]

print(second_num_list[0:3])
print(second_num_list[8:])

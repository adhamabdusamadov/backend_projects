# Задание на методы keys() и values():

products = {
    "яблоко": 5,
    "банан": 3
}

print(products.keys())
print(products.values())


# Задание на метод items():

countries = {
    "Узбекистан": "Ташкент",
    "Франция": "Париж"
}

print(countries.items())


# Задание на метод pop():

country = {
    "ташкент": "2 млн",
    "париж": "2.1 млн"
}

delcountry = input("введите название города: ")

if delcountry in country:
    country.pop(delcountry)
    print(country)
elif delcountry not in country:
    print('такой страны нету в списке')



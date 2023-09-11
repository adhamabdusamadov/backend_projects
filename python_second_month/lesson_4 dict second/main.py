odam = {
    'name': "Adham",
    'age': 14,
    'weight': 50,
    'cars': ['mazda', 'tayota', 'nissan']
}


# 1


# print(odam.keys()) # выводит только keys
# print(odam.values()) # выводит только values
# print(odam['cars']) # выводит values


# 2


# odam['age'] = 15
# print(odam)
# odam.update(age=15, cars='bmw')
# print(odam)


# 3


# print(odam.items())
# for i in odam.items(): # hamma elementlarni olish uchun
#     print(i)
# for i in odam.value(): # faqat valueni olish uchun
#     print(i)
# for i, j in odam.items():
#     print(f'{i} degan keyda {j} value bor')

family = {
    'ota': {
        'ismi': 'yoshi',
        'yoshi': '40'
    },
    'ona': {
        'ismi': 'yoshi',
        'yoshi': ''
    },
    'men': {
        'ismi': 'yoshi',
        'yoshi': ''
    }
}

print(family['ota']['yoshi'])
# 1

scores = {
    'Adham':4,
    'Sardor':2,
    'Ali':3,
    'Dilshod':6,
    'Tohir':3
}

question = input("Ism kiriting: ").lower()
if question == 'adham':
    print(f"Adhamda {scores['Adham']} ball bor")
elif question == 'sardor':
    print(f"Sardorda {scores['Sardor']} ball bor")
elif question == 'ali':
    print(f"Alida {scores['Ali']} ball bor")
elif question == 'dilshod':
    print(f"Dilshodda {scores['Dilshod']} ball bor")
elif question == 'ali':
    print(f"Tohirda {scores['Tohir']} ball bor")


# 2

family = {
    "Abror": {
        "bo'y": 186,
        "ism": "Abror",
        "familiya": "Toychiyev",
        "yosh": 39
    },
    "Farogat": {
        "bo'y": 169,
        "ism": "Farogat",
        "familiya": "Nazarova",
        "yosh": 38
    },
    "Adham": {
        "boy": 167,
        'ism': "Adham",
        'familiya': "Abdusamadov",
        'yosh': 14
    }
}

print(family)
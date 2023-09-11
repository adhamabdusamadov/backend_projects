# # 1

# products = {
#     'apple': 5,
#     'banana': 6,
#     'pineapple': 8,
#     'cherry': 4,
#     'orange': 6
# }

# product_name = input("meva nomini kiriting: ")

# def meva_top(name):
#     if name in products:
#         print(f"{name} soni {products[product_name]} ta")
#     elif name not in products:
#         print(f"Bunday meva yo'q")

# meva_top(product_name)


# # 2

# products = {
#     'apple': 'red',
#     'banana': 'yellow',
#     'pineapple': 'orange',
#     'cherry': 'red',
#     'orange': 'orange'
# }

# product_name = input("meva nomini kiriting: ")

# def guessthecolor(nom):
#     if nom in products:
#         print(f"{nom} ni rangi {products[nom]}")
#     else:
#         print()
# guessthecolor(product_name)


# 3

movies = {
    "Interstellar": 6,
    "The Lord of the Rings": 7,
    "Fight Club": 8,
    "Back to the Future": 8
}

rating = int(input("Reyting kirting: "))

def moviesrating():
    for i in movies.keys():
        if movies[i] > rating:
            j = movies.keys()
            i = movies[j]
            print(j)
moviesrating()
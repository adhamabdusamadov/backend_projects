# 1. Задание на словарь и условный оператор if:

products = {
    'apple': 5,
    'banana': 6,
    'pineapple': 8,
    'cherry': 4,
    'orange': 6
}

print(products)
product_name = input("enter the product name ")

if product_name in products:
    print(f"number of {product_name} {products[product_name]}")
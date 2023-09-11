# lambda function
# lambda function - bu funksiya nomi yo'q, bir qatorlik funksiya

# avzalliklari:
# 1. bir qatorlik funksiya

# 2. return qilish shart emas

# 3. parametr sifatida *args va **kwargs qabul qilishi mumkin

# 4. lambda funksiyalarda if, else, elif operatorlari ishlatilmaydi

# 5. lambda funksiyalarda list comprehension ishlatilishi mumkin
#    list comprehension - bu listni qisqacha yaratish usuli. Misol uchun: mylist = [i for i in range(10)]


# lambda

a, b, c = 10, 20, 30
result = lambda num1, num2, num3: print(num1 * num2 * num3)

print(result(a, b, c))
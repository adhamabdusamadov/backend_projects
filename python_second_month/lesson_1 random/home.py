# # 1 topshiriq

# numbers = (15, 30, 10, 5, 40, 20)

# print(min(numbers))
# print(max(numbers))

# # 2 topshiriq

# my_tuple = (1, "hello", 3.14, False)
# print(my_tuple)

# my_tuple = list(my_tuple)

# my_tuple.pop(1)
# my_tuple.insert(1, "world")

# my_tuple = tuple(my_tuple)
# print(my_tuple)

# 3 topshiriq

# tuple bu ozgartirib bolmaydigan list, tuple uchun () sintaksi ishlatiladi
# set bu ozgartirib va tartiblab bolmaydi[an list, set da element lar qaytarilmaydi agar set da 2 birhil element bolda 1 tasi chiqariladi, set uchun {} sintaksi ishlatiladi
# ular orasidagi farqi tuple ni tartiblasa boladi set ni tartiblab bolmaydi

# # 4 topshiriq

# my_set = {True, 'mars', 1, 'bir narsa', 2, 3, "salom"}
# my_set = list(my_set)

# for num in my_set:
#     if type(num) is int:
#         print(num)

# 5 topshiriq

# days = input("hafta kunini kiriting: ").lower()
# my_list = ["dushanba", "seshanba", "chorshanba", "payshanba", "juma", "shanba", "yakshanba"]

# if days == my_list[1] or days == my_list[3] or days == my_list[5]:
#     print("juft")
# elif days == my_list[0] or days == my_list[2] or days == my_list[4] or days == my_list[6]:
#     print("toq")

# # 6 topshiriq

# name = input("ism kiriting: ").lower()
# name_2 = input("ism kiriting: ").lower()
# name_set = {"0"}

# if name == name_2:
#     print("ismingiz qabul qilinmaydi")
# elif name != name_2:
#     print("ismingiz qabul qilindi")
#     name_set.add(name)
#     name_set.add(name_2)


# print(name_set)

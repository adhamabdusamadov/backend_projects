# 1

file = open('D:\pycharm projects\python_second_month\lesson_11 file handling\index.txt', 'r')
print(file.read())

# 2

write = open('D:\pycharm projects\python_second_month\lesson_11 file handling\info.txt', 'w')
add_info = input("Malumot kiriting: ")
write.write(add_info)

# 3
append = open('D:\pycharm projects\python_second_month\lesson_11 file handling\info.txt', 'a')
add_append_info = input('Malumot kiriting: ')
append.write(add_append_info)

# 4


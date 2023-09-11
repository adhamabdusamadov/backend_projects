with open('D:\pycharm projects\python_second_month\lesson_12\info.txt', 'w+') as file:
    question1 = input('ism kiriting: ')
    question2 = input('yoshingizni kiriting: ')
    question3 = input('yaxshi korgan qizingizni ismi: ')
    file.write('ism: '+question1 + '\n')
    file.write('yosh: '+question2 + '\n')
    file.write('yaxshi korgan qiz: '+question3 + '\n')
    print(file.read())



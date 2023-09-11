# 1 topshiriq

my_list = ['adham']

def listreverse():
    print(my_list[::-1])
listreverse()


# 2 topshiriq


my_second_list = ['er', 23, True]
print("""
1. add element
2.remove element
""")
question = input("1, 2: ")

def add_element():
    adding_element = input("nma soz qoshmoqchisiz: ")
    my_second_list.append(adding_element)
    print(my_second_list)
def remove_element():
    removing_element = input("nima sozni ochirmoqchisiz: ")
    my_second_list.remove(removing_element)
    print(my_second_list)

if question == '1':
    add_element()
elif question == '2':
    result = remove_element(my_second_list)
    print(result)


# 3 topshiriq

my_dict = {'AQsh': '123',
           'Russia': '456',
           'China': '789',
           'India': '1012',
           'Japan': '1314'
}


def countryinfo(country):
    ques_country = input("Davlat nomini kiriting: ")
    if ques_country in my_dict:
        return my_dict[ques_country]
    else:
        return "Bu davlat haqida ma'lumot yo'q"

result = countryinfo(my_dict)
print(result)
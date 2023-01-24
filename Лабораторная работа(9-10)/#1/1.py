from jinja2 import Template
import os.path


if os.path.isfile('#1/temp1.txt'):
    with open('#1/temp1.txt', "r", encoding='utf-8') as txt_infile:
        tm = Template(txt_infile.read())
else:
    print("Файла нет")

user_name = input("Имя: ")
time = input("Срок: ")
item = input("Предмет: ")
place = input("Место: ")

print(tm.render(u_n=user_name, t=time, i=item, p=place))
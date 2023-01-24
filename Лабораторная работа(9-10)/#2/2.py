import os.path
from jinja2 import Template
import json


class Char:
    def __init__(self, имя, тип_соревнования, характеристика, дата_соревнования):
        self.имя = имя
        self.тип_соревнования = тип_соревнования
        self.характеристика = характеристика
        self.дата_соревнования = дата_соревнования


def set_json_file(characters):
    data = {}
    data['Characters'] = []

    for char in characters:
        data['Characters'].append({
            "Имя победителя": char.имя,
            "Вид соревнования":  char.тип_соревнования,
            "Дата соревнования": char.дата_соревнования,
            "Характеристика": char.характеристика,
        })

    with open('#2/characters.json', 'w', encoding='utf-8') as json_outfile:
        json_outfile.write(json.dumps(data, ensure_ascii=False))

    pass


первый = Char(
    input("Имя: "),
    input("Вид соревнования: "),
    int(input("Характеристика: ")),
    input("Дата соревнования: ")
)

print()

второй = Char(
    input("Имя: "),
    input("Вид соревнования: "),
    int(input("Характеристика: ")),
    input("Дата соревнования: ")
)

персонажи = [первый, второй]


# Заполнение и печать шаблона
if os.path.isfile('#2/temp2.txt'):
    with open('#2/temp2.txt', "r", encoding='utf-8') as txt_infile:
        tm = Template(txt_infile.read())
else:
    print("Файла нет")

print('\n', tm.render(
    c_t=первый.тип_соревнования, char_1=первый, char_2=второй))


# Дополнительно
set_json_file(персонажи)

with open('#2/characters.json', 'r', encoding='utf-8') as json_outfile:
    print(json_outfile.read())
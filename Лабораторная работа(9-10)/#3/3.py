from jinja2 import Template
import json
import os.path


class City:
    def __init__(self, index, region_type, region, name, population):
        self.name = name

        try:
            self.population = int(population)
        except ValueError:
            self.population = 0

        self.region = region
        self.index = int(index)
        self.region_type = region_type

    def print(self):
        print("name", self.name)
        print("population", self.population)
        print("region", self.region)
        print("index", self.index)
        print("region_type", self.region_type)
        pass


# Получаем список городов из файла
cities_list = list()
with open("#3/result_cities.json", "r", encoding='utf-8') as json_infile:
    cities = json.load(json_infile)
    for city in cities['data']:
        cities_list.append(City(
            city["Индекс"], city["Тип региона"], city["Регион"], city["Город"], city["Население"]))


# Заполнение шаблона
if os.path.isfile('#3/temp3.txt'):
    with open('#3/temp3.txt', "r", encoding='utf-8') as txt_infile:
        tm = Template(txt_infile.read())
else:
    print("Файл не найден")


# Создание страницы html
with open("#3/result.html", "w", encoding='utf-8') as html_outfile:
    html_outfile.write(tm.render(cities=cities_list))

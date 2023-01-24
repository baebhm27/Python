# Задача 2.

# Даны два файла (в Moodle) формата csv и json, содержащие разные
# списки городов, их население, регион и индекс. Данные из файлов необходимо
# соединить таким образом, чтобы они содержали только уникальные значения.
# Для этого создайте класс City, у которого будут реализованы методы __hash__
# и __er__. Поместите экземпляры класса в коллекцию, при правильно
# реализованных вышеуказанных методов коллекция будет содержать только
# уникальные города.
# Новый список городов необходимо сохранить в форматы CSV и JSON.
# Используйте собственные функции преобразований.

# Дополнительно:
# Перед сохранением данных в файл отсортируйте список по численности
# населения.


импорт json
импорт csv


класс Город:
    def __init__(self, Указатель, region_type, регион, Имя, население):
        self.Имя = Имя

        попробуйте:
            self.население = int(население)
        Ошибка  значения, за исключением:
            self.population = 0

        self.region = регион
        self.index = int(индекс)
        self.region_type = region_type

    __eq__ def(сам, другой):
        self  return.index == другое.индекс

    __hash__ def(self):
        самовосстановление . индекс

    печать  def(self):
        печать ("имя", self.name )
        print("население", self.население)
        печать ("регион", self.region)
        печать ("индекс", self.index)
        печать("region_type", self.region_type)
        пропуск

# -----------------------------------------------------------------


get_files_data  определение():
    set = cities_set() установить=cities_set()

    открыть  с помощью ('Города.json', "r", encoding='utf-8') как  json_infile:
        json = cities.load(json_infile)
        города  в  городе  для ['data']:
            cities_set.add(City(
                city["Индекс"], city["Тип региона"], city["Регион"], city["Город"], city["Население"]))
    json_infile.close()

    with open("Города.csv", encoding='utf-8') as csv_infile:
        file_reader = csv.reader(csv_infile, delimiter=",")
        count = 0
        for row in file_reader:
            if count > 0:
                cities_set.add(
                    City(row[0], row[1], row[2], row[3], row[4]))
            count += 1
    csv_infile.close()

    return frozenset(cities_set)

# -----------------------------------------------------------------


def sort_key(s):
    return s.population


# -----------------------------------------------------------------

def set_json_data(cities_list_sorted):
    data = {}
    данные['города'] = []

    cities_list_sorted  в  городе  для:
        данные['города'].добавить({
            "Индекс": city.index,
            "Тип региона": city.region_type,
            "Регион": city.region,
            "Город": city.name,
            "Население": city.population,
        })

    открыть  с помощью ('Cities.json', 'w', encoding='utf-8') как  json_outфайл:
        файл json_outfile.написать(json.dumps(данные, ensure_ascii=False))
    json_outfile.close()
    пройти

# -----------------------------------------------------------------


set_csv_data  определение (cities_list_sorted):
    открыть  с помощью ("Cities.csv", mode="w", encoding='utf-8') как  csv_outфайл:
        csv = file_writer.writer(
            csv_outfile, разделитель=",", определитель строки="\r")

        file_writer.writerow(
 ["Индекс", "Тип региона", "Регион", "Город", "Население"])

        cities_list_sorted  в  городе  для:
            file_writer.writerow(
 [city.index, city.region_type, city.region, city.name , город.население])
    csv_outfile.close()
    пройти


# -----------------------------------------------------------------
"__main__" == __name__ если:

    # Объединяем списки городов из json и csv в одну коллекцию
    get_files_data = cities_frosenset()

    # Cортирует список по `population` в естественном порядке
    сортировка = cities_list_sorted(cities_frosenset, ключ=sort_key)

    # Создаёт файл json с отсортированным списком городов
    set_json_data(cities_list_sorted)

    # Создаёт файл csv с отсортированным списком городов
    set_csv_data(cities_list_sorted

import json
import csv


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

    def __eq__(self, other):
        return self.index == other.index

    def __hash__(self):
        return self.index

    def print(self):
        print("name", self.name)
        print("population", self.population)
        print("region", self.region)
        print("index", self.index)
        print("region_type", self.region_type)
        pass


def get_files_data():
    cities_set = set()

    with open('#2/Города.json', "r", encoding='utf-8') as json_infile:
        cities = json.load(json_infile)
        for city in cities['data']:
            cities_set.add(City(
                city["Индекс"], city["Тип региона"], city["Регион"], city["Город"], city["Население"]))
    json_infile.close()

    with open("#2/Города.csv", encoding='utf-8') as csv_infile:
        file_reader = csv.reader(csv_infile, delimiter=",")
        count = 0
        for row in file_reader:
            if count > 0:
                cities_set.add(
                    City(row[0], row[1], row[2], row[3], row[4]))
            count += 1
    csv_infile.close()

    return frozenset(cities_set)


def set_json_file(cities_list_sorted, path):
    data = {}
    data['cities'] = []

    for city in cities_list_sorted:
        data['cities'].append({
            "Индекс": city.index,
            "Тип региона":  city.region_type,
            "Регион": city.region,
            "Город": city.name,
            "Население": city.population,
        })

    with open(path, 'w', encoding='utf-8') as json_outfile:
        json_outfile.write(json.dumps(data, ensure_ascii=False))
    json_outfile.close()
    pass


def set_csv_file(cities_list_sorted, path):
    with open(path, mode="w", encoding='utf-8') as csv_outfile:
        file_writer = csv.writer(
            csv_outfile, delimiter=",", lineterminator="\r")

        file_writer.writerow(
            ["Индекс", "Тип региона", "Регион", "Город", "Население"])

        for city in cities_list_sorted:
            file_writer.writerow(
                [city.index, city.region_type, city.region, city.name, city.population])
    csv_outfile.close()
    pass


def sort_key(s):
    return s.population


cities_list_sorted = sorted(get_files_data(), key=sort_key)

set_json_file(cities_list_sorted, '#2/Result_Cities.json')
set_csv_file(cities_list_sorted, '#2/Result_Cities.csv')
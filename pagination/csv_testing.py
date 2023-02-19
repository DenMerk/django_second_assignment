import csv
import pprint

with open('data-398-2018-08-30.csv', encoding='UTF-8') as file:
    reader = csv.DictReader(file)
    count = 0
    name_list = []
    street_list = []
    district_list = []
    for line in reader:
        name_list.append(line['Name'])
        street_list.append(line['Street'])
        district_list.append(line['District'])

print(name_list[1000:1004], street_list[1000:1004], district_list[1000:1004])
print(len(name_list))


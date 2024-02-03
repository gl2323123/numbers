from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

pattern = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
sub_ = r'+7(\2)-\3-\4-\5 \6\7'

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
def normal_table(my_list: list):
    new_list = list()
    for a in my_list:
      full_name = " ".join(a[:3]).split(' ')
      result = [full_name[0], full_name[1], full_name[2], a[3], a[4],
                re.sub(pattern, sub_, a[5]),
                a[6]]
      new_list.append(result)
    return normal_table2(new_list)


def normal_table2(cells: list):
  for cell in cells:
    first_name = cell[0]
    last_name = cell[1]
    for new_cell in cells:
      new_first_name = new_cell[0]
      new_last_name = new_cell[1]
      if first_name == new_first_name and last_name == new_last_name:
        if cell[2] == "": cell[2] = new_cell[2]
        if cell[3] == "": cell[3] = new_cell[3]
        if cell[4] == "": cell[4] = new_cell[4]
        if cell[5] == "": cell[5] = new_cell[5]
        if cell[6] == "": cell[6] = new_cell[6]

  result_list = list()
  for i in cells:
    if i not in result_list:
      result_list.append(i)

  return result_list



# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(normal_table(contacts_list))

#Задание №1


def file_dict(file):
    with open(file, encoding="utf-8") as file_1:
        list_1 = []
        cook_book = {}
        for string in file_1:
            list_1.append(string.strip())

        for el in range(len(list_1)):
            if list_1[el].isdigit():
                val = []
                key = list_1[el - 1]
                for el_1 in range(1, int(list_1[el]) + 1):
                    ingredients = {}
                    ingredient_list = list_1[el + el_1].split(" | ")
                    ingredients['ingredient_name'] = ingredient_list[0]
                    ingredients['quantity'] = int(ingredient_list[1])
                    ingredients['measure'] = ingredient_list[2]
                    val.append(ingredients)
                cook_book[key] = val
    return cook_book


cook_book = file_dict('file_1.txt')
print(cook_book)

#Задание №2


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredients in cook_book[dish]:
            if ingredients['ingredient_name'] not in shop_list:
                shop_list[ingredients['ingredient_name']] = {
                        'measure': ingredients['measure'],
                        'quantity': ingredients['quantity'] * person_count
                }
            else:
                shop_list[ingredients['ingredient_name']]['quantity'] = (
                        shop_list[ingredients['ingredient_name']]['quantity']
                        + (ingredients['quantity'] * person_count))
    return shop_list


print(get_shop_list_by_dishes(['Запеченный картофель','Фахитос', 'Омлет'], 3))


#Задание №3


def file_list(file):
    with open(file, encoding='utf-8') as file_1:
        list_1 = file_1.readlines()
    return list_1


files_list = ['1.txt', '2.txt', '3.txt']
files_list.sort(key=file_list, reverse=True)


with open('finish.txt', 'w', encoding='utf-8') as file_finish:
    for files in files_list:
        file_finish.write(f'Название файла: {files}\n')
        file_finish.write(f'Длина файла: {str(len(file_list(files)))} стр\n')
        file_finish.write("\n")
        for string in file_list(files):
            file_finish.write(f'{string.strip()}\n')
        file_finish.write("\n")












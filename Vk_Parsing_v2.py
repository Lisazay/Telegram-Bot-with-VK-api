import vk
import json
import time
import pymysql
import os
from array import *
import numpy as np
import pandas as pd
from itertools import groupby
import sys


try:
        conn = pymysql.connect(host="localhost", user="admin",
                               passwd="123", db="tg")


except pymysql.Error as err:
        print("Connection error: {}".format(err))
        conn.close()


sql = "SELECT * FROM telegram"


try:
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute(sql)
        cur.execute('SET NAMES utf8;')  #
        cur.execute('SET CHARACTER SET utf8;')  # ДАННЫЕ СТРАОЧКИ ПОЗВОЛЯЮТ ЗАПИСЫВАТЬ В БД РУССКИЕ БУКВЫ
        cur.execute('SET character_set_connection=utf8;')  #
        data = cur.fetchall()
except pymysql.Error as err:
    print("Query error: {}".format(err))

#print(sys.stdout.encoding)
session = vk.Session('7558823275588232755882322c7538e29477558755882322f1f6e119e3ca9c2dc1dc6da')
cur.execute("SELECT COUNT(*) FROM  `telegram` ")  # Не правильно считает количество строк в БД см. на строку ниже
count_str = cur.fetchone()
colom = count_str['COUNT(*)']  # Теперь норм , главное вычесть 1
vkapi = vk.API(session)

game_over = []       #  в МАССИВ НАДО ЗАПИХНУТЬ (КОРОТКИЕ) ИМЕНА СООБЩЕСТВ ИЗ БАЗЫ ДАННЫХ
mas_pub = []

publiks = ('pub1', 'pub2','pub3', 'pub4', 'pub5', 'pub6', 'pub7', 'pub8')


cur.execute("SELECT DISTINCT `pub1`, `pub2`, `pub3`, `pub4`, `pub5`, `pub6`, `pub7`, `pub8`  FROM `telegram` ")
result_set = cur.fetchall()
for row in result_set:
    print(row)
    if row == None:
        break
    else:
        game_over.append(row)
print(colom)
for row in range(8):   # 8 потому что пабликов всего 8
    for row2 in range(colom):   # количество строк в БД
        print(game_over[row2][publiks[row]])
        if game_over[row2][publiks[row]] == None:

            mas_pub.append('https://vk.com/abstract_humour')
        else:
            mas_pub.append(game_over[row2][publiks[row]])




print(mas_pub)
#print(game_over[0]['pub1'])

try:
    import itertools
except ImportError:
    print('Библиотека не установлена')


new_sort_mas_pub = [mas_pub[0] for mas_pub in itertools.groupby(sorted(mas_pub))]
print('groupby sort:', new_sort_mas_pub)
file = open('C:/idea/group.txt',
                'w', encoding="utf-8")
file.write(str(new_sort_mas_pub))
file.close()



def groups_id(short_id):
    for item in short_id:
            try:
                getGroup_id = vkapi.groups.getById(group_ids=item[15:], v='5.95')
                path = "C:/idea/{}".format(str(item[15:]))
            except:
                getGroup_id = vkapi.groups.getById(group_ids="abstract_humour", v='5.95')
                path = "C:/idea/{}".format("abstract_humour")

            json_data = json.dumps(getGroup_id)
            parsed_json = json.loads(json_data)
            text_group = parsed_json[0]["id"]
            print(-text_group)


            try:
                os.mkdir(path)
            except :
                print("Создать директорию %s не удалось" % path)
            else:
                print("Успешно создана директория %s " % path)

            counter1 = 0  # Первый  Счетчик для циклов
            while counter1 < 1:
                counter2 = 0  # Второй Счетчик для циклов
                counter3 = 0  # Третий Счетчик для циклов
                image_number = 1  # Переменная используется для сохранения изображений в текстовый файл с номером на 1 больше чем предыдущий
                a = 0  # Что-то связанное с json
                if counter3 < 1:


                    wallText = vkapi.wall.get(owner_id=-text_group, count=21, v='5.84')

                    json_data = json.dumps(wallText)
                    parsed_json = json.loads(json_data)

                    while counter2 < 21:
                        str_image_number = str(image_number)  # Проебразуем переменную image_number в строку
                        link1 = parsed_json["items"][0 + a]["text"]

                        try:
                            link2 = parsed_json["items"][0 + a]["attachments"][0]["photo"]["sizes"][3]["url"]
                        except:
                            link2 = parsed_json["items"][0 + a]

                        try:
                            link3 = parsed_json["items"][0+a]["attachments"][0]["link"]["url"]
                            print(parsed_json)

                            print(link3)
                        except:
                            pass


                        print(link2)
                        try:
                            print(item, " ITEEEEEEEEEEEEEEEEEEEM")
                            file = open('C:/idea/' + item[15:] + '/Photo' + str_image_number + '.txt',
                                    'w', encoding="utf-8")  # Открываем/создаем на компьютере в папке текстовые файлы содержащие ссылки на изображения
                            file.write(link2)  # Записываем
                            file_post = open('C:/idea/' + item[15:] + '/Post' + str_image_number + '.txt',
                                    'w', encoding="utf-8")
                            print(link3, "LINNNNNNNNNNNNNNNK###################")
                            file_post.write(link3)
                            file.close()
                            file_post.close()
                        except:
                            print(item, "ITEMEEEEEEEEEEEEEEEEE   EXCECCCCCCCCCCCCCCCCCCCCCCEPT")
                            file_post = open('C:/idea/' + item[15:] + '/Post' + str_image_number + '.txt',
                                             'w', encoding="utf-8")
                            print(link3, "LIIIIIIIIIIIIIIIIIIIIIIIIINK@@@@@@@@@@@@ EEEEEEEEEEEEEEEEEEEXXXXXXXCPET")
                            file_post.write(link3)
                            file_post.close()

                        file = open('C:/idea/' + item[15:] + '/Text' + str_image_number + '.txt',
                                    'w', encoding="utf-8")  # Открываем/создаем на компьютере в папке текстовые файлы содержащие ссылки на изображения
                        file.write(link1)  # Записываем
                        file.close()  # Закрываем файл
                        counter2 += 1
                        a += 1
                        image_number += 1
                       # print(publics[counter1])
                    counter1 += 1
                    # print(publick_id)
                    print(counter1)

    return (-text_group)

groups_id(new_sort_mas_pub)

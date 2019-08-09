import vk
import json
import time
import pymysql
import os
from array import *
import numpy as np
import pandas as pd
import os
from itertools import groupby

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


session = vk.AuthSession(app_id=os.environ['app_id_vk'], user_login=os.environ['user_login_vk'],
                         user_password=os.environ['user_pass_vk'])

cur.execute("SELECT COUNT(*) FROM  `telegram` ")  # Не правильно считает количество строк в БД
count_str = cur.fetchone()
vkapi = vk.API(session)

game_over = []       #  в МАССИВ НАДО ЗАПИХНУТЬ (КОРОТКИЕ) ИМЕНА СООБЩЕСТВ ИЗ БАЗЫ ДАННЫХ
mas_pub = []

publikk = ('pub1', 'pub2','pub3', 'pub4', 'pub5', 'pub6', 'pub7', 'pub8')


cur.execute("SELECT DISTINCT `pub1`, `pub2`, `pub3`, `pub4`, `pub5`, `pub6`, `pub7`, `pub8`  FROM `telegram` ")
result_set = cur.fetchall()
for row in result_set:
    game_over.append(row)
    # s = "%s" % ((row["pub%s"]) % (row))
    # k = list(row)
    # game_over.append(s[k])
# for rec in range(1):    # !!!!!!!!!!!!!! Вывод название паблика !!!!!!!!!!!!!  # ЭТА СТРОЧКА МОЖЕТ БЫТЬ ПОЛЕЗНА!!!!№№№№№№№№
#         pub = result_set[1]        # ЭТА СТРОЧКА МОЖЕТ БЫТЬ ПОЛЕЗНА!!!!№№№   # !!!!!!!!!!!!!! Вывод названия паблика !!!!!!!!!!!!!
#        # print(pub)                         # ЭТА СТРОЧКА МОЖЕТ БЫТЬ ПОЛЕЗНА!!!!№№№№№№№№
#         game_over.append(pub)             # ЭТА СТРОЧКА МОЖЕТ БЫТЬ ПОЛЕЗНА!!!!№№№№№№№№
#         conn.commit()                    # ЭТА СТРОЧКА МОЖЕТ БЫТЬ ПОЛЕЗНА!!!!№№№№№№№№
for row in range(8):
    for row2 in range(count_str['COUNT(*)']):
        print(game_over[row2][publikk[row]])  # Вместо row надо поставить количество строк в базе данных
        mas_pub.append(game_over[row2][publikk[row]])

print(mas_pub)
#print(game_over[0]['pub1'])

try:
    import itertools
except ImportError:
    print('Библиотека не установлена')


# new_sort_mas_pub = set(mas_pub[0] for mas_pub in itertools.groupby(mas_pub))
# print('верно groupby no sort:', new_sort_mas_pub)

new_sort_mas_pub = [mas_pub[0] for mas_pub in itertools.groupby(sorted(mas_pub))]
print('groupby sort:', new_sort_mas_pub)


def groups_id(short_id):
    for item in short_id:
            getGroup_id = vkapi.groups.getById(group_ids=item[15:], v='5.95')
            json_data = json.dumps(getGroup_id)
            parsed_json = json.loads(json_data)
            text_group = parsed_json[0]["id"]
            print(-text_group)

            path = "C:/Bablo/{}".format(str(item[15:]))

            try:
                os.mkdir(path)
            except OSError:
                print("Создать директорию %s не удалось" % path)
            else:
                print("Успешно создана директория %s " % path)

            counter1 = 0  # Первый  Счетчик для циклов
            while counter1 < 1:
                counter2 = 0  # Второй Счетчик для циклов
                counter3 = 0  # Третий Счетчик для циклов
                image_number = 1  # Переменная используется для сохранения изображений в текстовый файл с номером на 1 больше чем предыдущий
                # publick_id = spisok_id[counter1]        # ID группы зависит от переменной counter1
                a = 0  # Что-то связанное с json
                if counter3 < 1:
                    print()
                    #  print(publick_id )
                    wallPhoto = vkapi.photos.get(owner_id=-text_group, count=21,
                                                 album_id='wall', rev='1', photo_sizes=0, v='5.95')
                    json_data = json.dumps(wallPhoto)
                    parsed_json = json.loads(json_data)
                    # print(parsed_json)
                    while counter2 < 21:
                        str_image_number = str(image_number)  # Проебразуем переменную image_number в строку
                        link = parsed_json["items"][0 + a]["sizes"][3]["url"]  # Получаем ссылку на изображене
                        print(link)
                        file = open('C:/Bablo/' + item[15:] + '/Photo' + str_image_number + '.txt',
                                    'w')  # Открываем/создаем на компьютере в папке текстовые файлы содержащие ссылки на изображения
                        file.write(link)  # Записываем
                        file.close()  # Закрываем файл
                        counter2 += 1
                        a += 1
                        image_number += 1
                       # print(publics[counter1])
                    counter1 += 1
                    # print(publick_id)
                    print(counter1)
            time.sleep(5)

    return (-text_group)


groups_id(new_sort_mas_pub)

#
#
# def comments(publick_id, count, post_id):   # Выборка комментариев под постом
#     getComm = vkapi.wall.getComments(owner_id=-publick_id, count=count, post_id=post_id, v='5.95')
#     json_data = json.dumps(getComm)
#     parsed_json = json.loads(json_data)
#     text_comm = parsed_json["items"][0]["text"]   #  ["items"][0]["text"] означает, что нулевой элемент массива items, тоесть все, что входит в первые фигурные скобки items (но это не точно))
#     print(parsed_json)
#     print(text_comm)






#
# cur.execute("SELECT DISTINCT `pub1`, `pub2`, `pub3`, `pub4`, `pub5`, `pub6`, `pub7`, `pub8`  FROM `telegram` WHERE 1 ")
# data = cur.fetchall()
# conn.commit()
#
# for i in range(0, len(data)):
#     if data[i][0]:
#         print(data([i][0]))
#
# for v in range(1, 9):
#
#     cur.execute("SELECT DISTINCT `pub%s` FROM `telegram`   " % v)
#     q = cur.fetchone()
#     print(q)
#     for row in q:
#         game_over.append('%s' % (cur.execute("SELECT DISTINCT `pub%s` FROM `telegram`   " % v)))
#         conn.commit()
# print(game_over)

#
# cur.execute(
#    "SELECT DISTINCT `pub1`, `pub2`, `pub3`, `pub4`, `pub5`, `pub6`, `pub7`, `pub8`  FROM `telegram` ")
# result_set = cur.fetchall()
# for row in  result_set:
#    game_over.append("%s, %s, %s, %s, %s, %s, %s, %s, " % (row['pub1'], row['pub2'], row['pub3'], row['pub4'], row['pub5'],
#                                                row['pub6'],row['pub7'], row['pub8'], ))
# print(game_over)







#
# for rec in q:     #q = cur.fetchone()
#          pub = q
#          print(pub)
#          game_over.append(pub)



# for v in range(1, 9):
#
#     cur.execute("SELECT DISTINCT `pub%s` FROM `telegram`   " % v)
#     q = cur.fetchone()
#     print(q)                                                         #  !!!!!!!!!!!!!!!!!!! ЧЕТ ИНТЕРЕСНОЕ !!!!!!!!!!!
#     game_over.append(q)
#     conn.commit()
#
# print(game_over)


# cur.execute(
#         "SELECT DISTINCT `pub1`, `pub2`, `pub3`, `pub4`, `pub5`, `pub6`, `pub7`, `pub8`  FROM `telegram` WHERE 1 ")
# q = cur.fetchone()  # !!!!!!!!!!!!!! Вывод названия паблика !!!!!!!!!!!!!
#
#
# for rec in q:  # !!!!!!!!!!!!!! Вывод название паблика !!!!!!!!!!!!!
#
#     pub = q[rec]  # !!!!!!!!!!!!!! Вывод названия паблика !!!!!!!!!!!!!
#     game_over.append(pub)
#
# print(game_over)
# conn.commit()


# cur.execute(
#         "SELECT DISTINCT `pub1`, `pub2`, `pub3`, `pub4`, `pub5`, `pub6`, `pub7`, `pub8`  FROM `telegram`  ")
# q = cur.fetchone()  # !!!!!!!!!!!!!! Вывод названия паблика !!!!!!!!!!!!!
# while q is not None:
#     game_over.append(q)
#     q = cur.fetchone()                   #  !!!!!!!!!!!!!!!!!!!!!!!! ЧЕТ ИНТЕРЕСНОЕ !!!!!!!!!!!!!!!!!!!!
#
# #c = ','.join(a)
#
# print(game_over) #Тип данных - список

#
# cur.execute(
#     "SELECT DISTINCT `pub1`, `pub2`, `pub3`, `pub4`, `pub5`, `pub6`, `pub7`, `pub8`  FROM `telegram` ")
# q = cur.fetchone()
# while q is not None:
#     print(q)
#     game_over.append(
#         "%s, %s, %s, %s, %s, %s, %s, %s, " % (q['pub1'], q['pub2'], q['pub3'], q['pub4'], q['pub5'],
#                                               q['pub6'], q['pub7'], q['pub8'],))
#     conn.commit()
#
# print(game_over)
# print(type(game_over))


# cur.execute(
#     "SELECT DISTINCT `pub1`, `pub2`, `pub3`, `pub4`, `pub5`, `pub6`, `pub7`, `pub8`  FROM `telegram` ")
# q = cur.fetchone()
# while q is not None:
#
#     game_over.append(
#         "%s, %s, %s, %s, %s, %s, %s, %s, " % (q['pub1'], q['pub2'], q['pub3'], q['pub4'], q['pub5'],
#                                               q['pub6'], q['pub7'], q['pub8'],))
# print(game_over[0])
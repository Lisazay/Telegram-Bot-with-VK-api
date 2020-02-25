import telebot
import random
import urllib.request as urllib2
from telebot import types
import pymysql
import os
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
    cur.execute('SET NAMES utf8;')                       #
    cur.execute('SET CHARACTER SET utf8;')                #     ДАННЫЕ СТРАОЧКИ ПОЗВОЛЯЮТ ЗАПИСЫВАТЬ В БД РУССКИЕ БУКВЫ
    cur.execute('SET character_set_connection=utf8;')      #
    data = cur.fetchall()
except pymysql.Error as err:
    print("Query error: {}".format(err))

token = os.environ['TOKEN_BOT']
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def handle_start(message):

    cur.execute("INSERT INTO  `telegram`(`id`,`next`, `advertising`,`publick`)  VALUES ('%s',1 ,12,'%s' ) ON DUPLICATE KEY UPDATE  id = id"%(message.from_user.id,message.text))
    conn.commit()


    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start')
    user_markup.row('/Паблики','/random','/Добавить Паблик')

    bot.send_message(message.from_user.id,'Welcome', reply_markup=user_markup)
    print(message.from_user.id)


file = open("C:\idea\group.txt","r+")
slime = (file.read())
random_pub = slime.split(',')#вместо запятой может бить точка, любой символ
# #(если у вас в файле дание через пробел топишем  пробел, через точку-точку)
file.close()
### Так можно сделать список из импорта данных BD

@bot.message_handler(commands=['/stop'])
def handle_start(message):
        hide_markup = telebot.types.ReplyKeyboardHide()
        bot.send_message(message.from_user.id,'...', reply_markup=hide_markup)

@bot.message_handler(commands=['random'])
def handle_start(message):
        print( cur.execute(sql))
        try:
            x = '\ '[:-1] + random.choice(random_pub)[17:-1]      # 17 потому что "/m" какой то вылезает.
            g = random.randint(1,21)
        except:
            x = "abstract_humor"
            g = random.randint(1, 21)
        y =str(g)
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)

        text_pub = write_text(x, y)
        print(text_pub)
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        text_pub = write_text(x, y)
        url = write_img(x, y)
        try:
            urllib2.urlretrieve(url, 'url_image.jpg')
            img = open('url_image.jpg', 'rb')
            bot.send_message(message.from_user.id, text_pub, disable_web_page_preview=True, reply_markup=user_markup)
            bot.send_photo(message.from_user.id, img, reply_markup=user_markup)
            img.close()
        except:
            url_post = write_post(x, y)
            bot.send_message(message.from_user.id, text_pub, disable_web_page_preview=True, reply_markup=user_markup)
            bot.send_message(message.from_user.id, url_post, reply_markup=user_markup)


@bot.message_handler(commands=['Паблики'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    for ch in [1, 2, 3, 4, 5, 6, 7, 8]:
        if cur.execute("SELECT `pub%s` FROM `telegram` WHERE `id` in ('%s')" % (ch, message.from_user.id)) == None:
            pass
        q = cur.fetchone()  # !!!!!!!!!!!!!! Вывод названия паблика !!!!!!!!!!!!!
        try:
            for rec in q:           # !!!!!!!!!!!!!! Вывод название паблика !!!!!!!!!!!!!
                pub = q[rec]  # !!!!!!!!!!!!!! Вывод названия паблика !!!!!!!!!!!!!
                print(pub)
                print(rec)
                print(ch)
                user_markup.row(pub[15:])
        except TypeError:
            user_markup.row("Пустое место под паблик")
    print("Нахожусь в 'Паблики'")
    print("Нахожусь в 'Паблики'")
   # user_markup.row(*[types.KeyboardButton(name) for name in ['{}'.format(pub[15:]), '\Борщ','\Орленок','\Пикабу']])
    user_markup.row('/Добавить Паблик', '/Удалить_Паблик','/Меню')
    bot.send_message(message.chat.id, 'Выбери пожалуйста паблик',reply_markup=user_markup)
    print(message.text)
    conn.commit()


@bot.message_handler(commands=['Далее'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    # if cur.execute("SELECT `advertising` FROM `telegram` WHERE `advertising` IN (0) AND `id` in ('%s')" % (message.from_user.id)):
    #     print("Реклаам")
    #     text = cur.execute("SELECT `text` FROM `telegram` WHERE `id` in ('%s')" % (message.from_user.id))
    #     colomn = cur.fetchone()
    #     for rec in colomn:
    #         text = colomn[rec]  # !!!!!!!!!!!!!! Вывод числа столбца !!!!!!!!!!!!!
    #
    #         print(text)
    #         conn.commit()
    #     link_adv = cur.execute("SELECT `url` FROM `telegram` WHERE `id` in ('%s')" % (message.from_user.id))
    #     colomn_two = cur.fetchone()
    #     for rec in colomn_two:
    #         link_adv = colomn_two[rec]  # !!!!!!!!!!!!!! Вывод числа столбца !!!!!!!!!!!!!
    #
    #         print(link_adv)
    #         conn.commit()
    #     bot.send_message(message.from_user.id, text, reply_markup=user_markup)
    #     print(link_adv)
    #     urllib2.urlretrieve(link_adv, 'url_image.jpg')
    #     img = open('url_image.jpg', 'rb')
    #     bot.send_photo(message.from_user.id, img, reply_markup=user_markup)
    #     img.close()
    #     cur.execute("UPDATE `telegram` SET `advertising` = 12 WHERE `id` in ('%s')" % (message.from_user.id))
    #
    # else:

    cur.execute("SELECT `next` FROM `telegram` WHERE `id` in ('%s')"%(message.from_user.id))
    k = cur.fetchone()
    for rec in k:
        next = k[rec]  # !!!!!!!!!!!!!! Вывод числа столбца !!!!!!!!!!!!!
        next = next
        print(next)
        conn.commit()
    cur.execute("SELECT `publick` FROM `telegram` WHERE `id` in ('%s')"%(message.from_user.id))
    q = cur.fetchone()      # !!!!!!!!!!!!!! Вывод названия паблика !!!!!!!!!!!!!
    for rec in q:           # !!!!!!!!!!!!!! Вывод название паблика !!!!!!!!!!!!!
        pub = q[rec]  # !!!!!!!!!!!!!! Вывод названия паблика !!!!!!!!!!!!!
        pub = pub       # !!!!!!!!!!!!!! Вывод названия паблика !!!!!!!!!!!!!
        print(pub)      # !!!!!!!!!!!!!! Вывод названия паблика !!!!!!!!!!!!!
    messageID = message.from_user.id
    print(q)
    x = '\ '[:-1]+ pub            # !!!!!!!!!!!!!!!  ТАК-КАК ПУТЬ К ФАЙЛУ ЧЕРЕЗ СЛЕШ, А В БД СЛЕШ НЕ ЗАНОСИТСЯ, ТО МЫ ДОБОВЛЯЕМ ЕГО ИСКУСТВЕНННО ПРИ ЭТОМ ПРОСТО ДОБАВИТЬ НЕЛЬЗЯЯ ПОТОМУ ЧТО ЭТО БУЛЕТ КАК КОМАНДА '\' ПЕРЕНОС НА СЛЕД СТРОКУ И ИЗ-ЗА ЭТОГО МЫ ДОБОВЛЯЕМ ПРОБЕЛ В СЛЕДСВТИИ ЧЕГО ПОТОМ МЫ ЕГО ПРОСТО ВЫРЕЗАЕМ[1:2]
    Q = Pupsen(next, messageID)
    y = str(Q)

    text_pub = write_text(x,y)
    url = write_img(x, y)
    try:
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_message(message.from_user.id, text_pub,disable_web_page_preview=True, reply_markup=user_markup)
        bot.send_photo(message.from_user.id, img, reply_markup=user_markup)
        img.close()
    except:
        url_post = write_post(x, y)
        bot.send_message(message.from_user.id, text_pub, disable_web_page_preview=True, reply_markup=user_markup)
        bot.send_message(message.from_user.id, url_post, reply_markup=user_markup)

    cur.execute("UPDATE `telegram` SET `advertising` = `advertising` -1 WHERE `id` in ('%s')" % (message.from_user.id))
    conn.commit()


@bot.message_handler(commands=['Меню'])
def handle_start(message):
        messageID = message.from_user.id
        GoToBack(message, messageID)

@bot.message_handler(commands=['Удалить_Паблик'])
def handle_start(message):

    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)

    for ch in [1, 2, 3, 4, 5, 6, 7, 8]:
        cur.execute("SELECT `pub%s` FROM `telegram` WHERE `id` in ('%s')" % (ch, message.from_user.id))  # !!!
        conn.commit()
        q = cur.fetchone()  # !!!!!!!!!!!!!! Вывод названия паблика !!!!!!!!!!!!!
        for rec in q:
            pub = q[rec]  # !!!!!!!!!!!!!! Вывод названия паблика !!!!!!!!!!!!!
            print(pub)
            print(rec)
            print(ch)
            try:
                user_markup.row(str(ch) + '.' + pub[15:])
            except TypeError:
                user_markup.row(str(ch) + '.' + "Пусто")
    user_markup.row('/Меню')
    bot.send_message(message.chat.id, 'Выбери какой паблик удалить', reply_markup=user_markup)



@bot.message_handler(content_types=['text'])
def handle_start(message):
        print(message.text + " TEXT")
        number = ["1.", "2.","3.","4.","5.","6.","7.","8.",]

        if message.text == '/Добавить Паблик':
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            bot.send_message(message.chat.id, 'Вставь ссылку на группу', reply_markup=user_markup)
            print(message.text)


        elif message.text.startswith('https://vk.com'):                     # ПРОВЕРЯЕМ НАЧИНАЕТСЯ ЛИ СООБЩЕНИЕ С ССЫЛКИ, ЕСЛИ ДА , ТО ЗАНОСИМ СООБЩНЕИЕ В БАЗУ!!!

            for v in range(1, 9):
                    cur.execute("SELECT `pub%s` FROM `telegram` WHERE `id` in ('%s')  " % (v, message.from_user.id))
                    q = cur.fetchone()  # !!!!!!!!!!!!!! Вывод названия паблика !!!!!!!!!!!!!
                    for rec in q:  # !!!!!!!!!!!!!! Вывод название паблика !!!!!!!!!!!!!
                        pub = q[rec]  # !!!!!!!!!!!!!! Вывод названия паблика !!!!!!!!!!!!!
                        print(pub)
                    vk = 'https://vk.com/'
                    if cur.execute("SELECT `pub%s` FROM `telegram` WHERE `id` in ('%s')  AND `pub%s` is NULL  OR   `pub%s` NOT like ('%s')  "
                                   % (v, message.from_user.id, v , v , "%" + str(vk) + "%")):
                        print(v)
                        #  LIKE в питоне работает
                            # только так !  like  ('%s') % "%" + str(vk) + "%"   не спрашивайте почему. Спасибо!

                        cur.execute("UPDATE `telegram` SET `pub%s` = ('%s') WHERE `id` in ('%s')"%(v, message.text,
                                                                                                message.from_user.id))
                        bot.send_message(message.from_user.id, 'Вы добавили паблик')
                        print("ADDDDDDDDDDD")
                        conn.commit()

                        break
                    else:
                        print("sorry")



        elif any(message.text.startswith(s) for s in number):
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            cur.execute("UPDATE   `telegram` SET  `pub%s` = NULL WHERE  `id` in ('%s') " % (message.text[0],
                                                                                         message.from_user.id)) # DELETE использовать не стоит
            conn.commit()
            bot.send_message(message.from_user.id, 'Группа удалена', reply_markup=user_markup)
            print("delete")

        elif message.text.startswith("П"):
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            bot.send_message(message.from_user.id, 'Нет Группы', reply_markup=user_markup)



        elif message.text  ==  message.text:
                x = '\ '[:-1]+ message.text
                print(x)
                y = '1'
                user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                url = write_img(x, y)
                try:
                    text_pub = write_text(x, y)
                except:
                    return ("Не Допустимый символ")  ### Эта штука делает так что бы рандомные символы не считывались как паблики

                try:
                    urllib2.urlretrieve(url, 'url_image.jpg')
                    img = open('url_image.jpg', 'rb')
                    bot.send_message(message.from_user.id, text_pub, disable_web_page_preview=True, reply_markup=user_markup)
                    bot.send_photo(message.from_user.id, img, reply_markup=user_markup)

                    img.close()
                    print("tryyy")
                except:
                    print("except")
                    url_post = write_post(x, y)
                    bot.send_message(message.from_user.id, text_pub, disable_web_page_preview=True , reply_markup=user_markup)
                    bot.send_message(message.from_user.id, url_post, reply_markup=user_markup)

                bot.send_chat_action(message.from_user.id, 'upload_photo')
                user_markup.row('/Далее','/Меню')
                bot.send_message(message.from_user.id, 'Продолжай',reply_markup=user_markup)
                cur.execute("UPDATE `telegram` SET `next` = 2 WHERE `id` in ('%s')"%message.from_user.id)
                cur.execute("UPDATE `telegram` SET `publick` = ('%s') WHERE `id` in ('%s')"%(message.text,message.from_user.id))
                conn.commit()




def write_img(x,y):

    try:
        if os.stat('C:\idea' + x + '\Photo' + y + '.txt').st_size == 0:
            my_file = open('C:\idea' + x[:-1] + '\Photo' + y + '.txt', encoding="utf-8")
            my_string_post = my_file.read()
            my_file.close()
            print('WRITE_IMG TRY IF')
            return (my_string_post)
        elif os.stat('C:\idea' + x + '\Photo' + y + '.txt').st_size != 0:
            my_file = open('C:\idea' + x + '\Photo' + y + '.txt', encoding="utf-8")
            my_string_post = my_file.read()
            my_file.close()
            print('WRITE_IMG TRY ELSE')
            return (my_string_post)
        else:
            my_file = open('C:\idea' + x[:-1] + '\Photo' + y + '.txt', encoding="utf-8")
            my_string_post = my_file.read()
            my_file.close()
            print('WRITE_IMG TRY ELSE')
            return (my_string_post)
    except:
        pass



def write_post(x,y):
    try:
        my_file_open = open('C:\idea' + x + '\Post' + y + '.txt', encoding="utf-8")
        my_file = my_file_open.read()
        my_file_open.close()
        print("WRITE_POST TRY")
        return (my_file)
    except:
        my_file_open = open('C:\idea' + x[:-1] + '\Post' + y + '.txt', encoding="utf-8")
        my_file = my_file_open.read()
        my_file_open.close()
        print("WRITE_POST EXCEPT")
        return (my_file)

def write_text(x,y):
    try:
        if os.stat('C:\idea' + x + '\Text' + y + '.txt').st_size == 0:
            print("erer")
            return ("Нажми 'Далее' ")
    except:
        pass
    try:
        my_file = open('C:\idea' + x[:-1] + '\Text' + y + '.txt', encoding="utf-8")
        my_string_text = my_file.read()
        my_file.close()
        print(my_file)
        return (my_string_text)
    except:
        pass

    try:
        my_file = open('C:\idea' + x + '\Text' + y + '.txt', encoding="utf-8")
        my_string_text = my_file.read()
        my_file.close()
        print(my_file)
        return (my_string_text)
    except:
        if os.stat('C:\idea' + x[:-1] + '\Text' + y + '.txt').st_size == 0:
            print("rtere")
            return ("Нажми 'Далее' ")





def Pupsen(next,messageID):
        if next <= 20:
                cur.execute("UPDATE `telegram` SET `next` = `next` + 1 WHERE `id` in ('%s')"%messageID)
                conn.commit()
        elif next ==21:
                cur.execute("UPDATE `telegram` SET `next` = 1 WHERE `id` in ('%s')"%messageID)
                conn.commit()
        return (next)
        conn.commit()


def GoToBack(message,messageID):
        cur.execute("UPDATE `telegram` SET `next` = 1 WHERE `id` in ('%s')" % messageID)
        conn.commit()
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('/Добавить Паблик')
        user_markup.row('/Паблики', '/random')
        bot.send_message(message.from_user.id, 'Меню', reply_markup=user_markup)

bot.polling(none_stop=True, interval=0)
import telebot
import random
import urllib.request as urllib2
from telebot import types
import pymysql

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


token = "token bot"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def handle_start(message):
    cur.execute("INSERT INTO  `telegram`(`id`,`next`, `advertising`,`publick`)  VALUES ('%s',1 ,1,'%s' ) ON DUPLICATE KEY UPDATE  id = id"%(message.from_user.id,message.text))
    conn.commit()
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start')
    user_markup.row('/Паблики','/random','/Добавить Паблик')
    bot.send_message(message.from_user.id,'Welcome', reply_markup=user_markup)
    print(message.from_user.id)



@bot.message_handler(commands=['/stop'])
def handle_start(message):
        hide_markup = telebot.types.ReplyKeyboardHide()
        bot.send_message(message.from_user.id,'...', reply_markup=hide_markup)

@bot.message_handler(commands=['random'])
def handle_start(message):
        print( cur.execute(sql))
        x = random.choice(['\MDK','\Орленок','\Борщ','\Пикабу'])
        g = random.randint(1,21)
        y =str(g)
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        url = write_img(x,y)
        urllib2.urlretrieve(url,'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img , reply_markup= user_markup)
        img.close()

@bot.message_handler(commands=['Паблики'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    for ch in [1, 2, 3, 4, 5, 6, 7, 8]:
        cur.execute(
        "SELECT `pub%s` FROM `telegram` WHERE `id` in ('%s')" % (ch, message.from_user.id))  # !!!
        q = cur.fetchone()  # !!!!!!!!!!!!!! Вывод названия паблика !!!!!!!!!!!!!
        for rec in q:           # !!!!!!!!!!!!!! Вывод название паблика !!!!!!!!!!!!!
                pub = q[rec]  # !!!!!!!!!!!!!! Вывод названия паблика !!!!!!!!!!!!!
                print(pub)
                print(rec)
                print(ch)
                user_markup.row(pub[15:])

    print("Нахожусь в 'Паблики'")
    user_markup.row(*[types.KeyboardButton(name) for name in ['\MDK', '\Борщ','\Орленок','\Пикабу']])
    user_markup.row('/Добавить Паблик')
    bot.send_message(message.chat.id, 'Выбери пожалуйста паблик',reply_markup=user_markup)
    print(message.text)


@bot.message_handler(commands=['Далее'])
def handle_start(message):

    cur.execute("SELECT `next` FROM `telegram` WHERE `id` in ('%s')"%(message.from_user.id))
    k = cur.fetchone()
    for rec in k:
        next = k[rec]  # !!!!!!!!!!!!!! Вывод числа столбца !!!!!!!!!!!!!
        next = next
        print(next)
        conn.commit()
    cur.execute("SELECT `publick` FROM `telegram` WHERE `id` in ('%s')"%(message.from_user.id)) #  !!!
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
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    url = write_img(x, y)
    urllib2.urlretrieve(url, 'url_image.jpg')
    img = open('url_image.jpg', 'rb')
    bot.send_chat_action(message.from_user.id, 'upload_photo')
    bot.send_photo(message.from_user.id, img, reply_markup=user_markup)
    img.close()

@bot.message_handler(commands=['Меню'])
def handle_start(message):
        messageID = message.from_user.id
        GoToBack(message, messageID)




@bot.message_handler(content_types=['text'])
def handle_start(message):
        print(message.text)

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
                        pub = pub  # !!!!!!!!!!!!!! Вывод названия паблика !!!!!!!!!!!!!
                        print(pub + "Name_public")
                    vk = 'vk.com'
                    if cur.execute("SELECT `pub%s` FROM `telegram` WHERE `id` in ('%s')  AND NOT `pub%s` like  ('%s') " % ( v, message.from_user.id, v ,"%" + str(vk) + "%" )): # Пиздец нахуй. LIKE в питоне работает только так !  like  ('%s') % "%" + str(vk) + "%"   не спрашивайте почему. Спасибо!

                        cur.execute("UPDATE `telegram` SET `pub%s` = ('%s') WHERE `id` in ('%s')"%(v, message.text, message.from_user.id))
                        bot.send_message(message.from_user.id, 'Вы добавили паблик')
                        break
                    else:
                        print("sorry")

            print(message.text)
            conn.commit()


        elif message.text == message.text:
                bot.send_message(message.chat.id,'...',parse_mode='Markdown')
                x = message.text
                y = '1'
                user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                url = write_img(x, y)
                urllib2.urlretrieve(url, 'url_image.jpg')
                img = open('url_image.jpg', 'rb')
                bot.send_chat_action(message.from_user.id, 'upload_photo')
                bot.send_photo(message.from_user.id, img, reply_markup=user_markup)
                img.close()
                user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                user_markup.row('/Далее','/Меню')
                bot.send_message(message.from_user.id, 'Продолжай', reply_markup=user_markup)
                cur.execute("UPDATE `telegram` SET `next` = 2 WHERE `id` in ('%s')"%message.from_user.id)
                cur.execute("UPDATE `telegram` SET `publick` = ('%s') WHERE `id` in ('%s')"%(message.text,message.from_user.id))
                conn.commit()



def write_img(x,y):
        my_file = open('C:\Folder' + x +  '\Photo' + y + '.txt')
        my_string = my_file.read()
        my_file.close()
        print(my_file)
        print('pizdec')
        return (my_string)



def Pupsen(next,messageID):
        if next <= 20:
                cur.execute("UPDATE `telegram` SET `next` = `next` + 1 WHERE `id` in ('%s')"%messageID)
                conn.commit()
        elif next ==21:
                cur.execute("UPDATE `telegram` SET `next` = 1 WHERE `id` in ('%s')"%messageID)
                conn.commit()
        return (next)


def GoToBack(message,messageID):
        cur.execute("UPDATE `telegram` SET `next` = 1 WHERE `id` in ('%s')" % messageID)
        conn.commit()
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('/Добавить Паблик')
        user_markup.row('/Паблики', '/random')
        bot.send_message(message.from_user.id, 'Меню', reply_markup=user_markup)

bot.polling(none_stop=True, interval=0)
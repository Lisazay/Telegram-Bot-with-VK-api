import vk
import json
session = vk.AuthSession(app_id=your application id, user_login='example@mail.ru',user_password='password')
vkapi = vk.API(session)


spisok_id = [57846937,460389,36775802,31480508]    # Список ID групп в ВК
publics = ['\MDK','\Борщ','\Орленок','\Пикабу']    # Названия Групп


counter1 = 0                                # Первый  Счетчик для циклов
while counter1 < 4:
    counter2 = 0                            # Второй Счетчик для циклов
    counter3 = 0                            # Третий Счетчик для циклов
    image_number = 1                        # Переменная используется для сохранения изображений в текстовый файл с номером на 1 больше чем предыдущий
    publick_id = spisok_id[counter1]        # ID группы зависит от переменной counter1
    a = 0                                   # Что-то связанное с json
    if counter3 < 1:

        print(publick_id )
        wallPhoto = vkapi.photos.get(owner_id=-publick_id, count=21, album_id='wall', rev='1', photo_sizes=0, v = '5.75')
        json_data = json.dumps(wallPhoto)
        parsed_json = json.loads(json_data)

        while counter2 < 21:
            str_image_number = str(image_number)  # Проебразуем переменную image_number в строку
            link = parsed_json["items"][0+a]["photo_604"]  # Получаем ссылку на изображене
            print(link)
            file = open('C:\Folder' + publics[counter1] + '\Photo' + str_image_number + '.txt', 'w')   # Открываем/создаем на компьютере в папке текстовые файлы содержащие ссылки на изображения
            file.write(link)          # Записываем
            file.close()              # Закрываем файл
            counter2 += 1
            a += 1
            image_number += 1
            print(publics[counter1])
        counter1 += 1
        print(publick_id)
        print(counter1)

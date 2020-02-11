import vk_api, random
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


token = '...'

#  авторизация
vk = vk_api.VkApi(token = token)
vk._auth_token()
#  подключение к  longpoll
longpoll = VkBotLongPoll(vk, '...')


# def read_photos(user_id, photos):
#     vk.method('photos.save',{'album_id': album_id, 'photos_list': photos_list})

# Понимание состояния бота
print('Бот запущен')

#  бесконечный цикл для приема сообщений
while True:
    #  начинаем прием сообщений. В ожидании...
    for event in longpoll.listen():
        # если приходит сообщение... новое...
        if event.type == VkBotEventType.MESSAGE_NEW:
            # преобразование текста сообщения в переменную
            mess = event.obj['text']
            # преобразование id в переменную
            peer_id = event.obj['peer_id']
            print(mess)
            print(peer_id)
            print()
        if event.type == VkBotEventType.PHOTO_NEW:
            photo = event.obj['items']
            id = event.obj['id']
            # read_photos(id, '1')

            print(id)
            print(photo)




            # Если есть новое сообщение
            if mess == 'Привет' or 'привет' or 'Приветики' or 'приветики' or 'Hi' or 'Hello':
                #vk.method('messages.send',{'peer_id': peer_id, 'message': 'Привеет!', 'random_id': random.randint(1,2147483647)})
                vk.method('messages.send',{'peer_id': peer_id, 'message': 'Привеет!', 'random_id': random.randint(1, 2147483647)})


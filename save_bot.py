
# import requests
# import urllib
# from  urllib.request import urlretrieve
# import vk_api
# import random
import cv2
import numpy
import urllib.request, urllib.error
import vk_api.longpoll

token = 'Токен'
vk_session = vk_api.VkApi(token=token)  # авторизация
vk_session._auth_token()  # в вк

vk = vk_session.get_api()
longpoll = vk_api.longpoll.VkLongPoll(vk_session) # подключение longpoll

while True:
    '''Запускаем бесконечный цикл'''
    for event in longpoll.listen():
        '''Сервер слушает и ждет новые сообщения'''
        if event.type == vk_api.longpoll.VkEventType.MESSAGE_NEW and event.to_me:
             '''Если есть новое сообщение и оно для бота'''
             msg = vk.messages.getById(message_ids=event.message_id)
             '''получаем информацию о вложение в сообщении'''
             att = event.attachments
             '''находим ссылку картинки'''
             photo_url = msg['items'][0]['attachments'][0]['photo']['sizes'][-1]['url']
             print(photo_url)
             data = urllib.request.urlretrieve(photo_url)
             print(data)

             req = urllib.request.urlopen(photo_url)
             print(req)
             arr = numpy.asarray(bytearray(req.read()), dtype=numpy.uint8)
             img = cv2.imdecode(arr, -1)
             img = cv2.bitwise_not(img)
             cv2.imwrite("/home/ivg/Рабочий стол/bot/photo/1.jpg", img)


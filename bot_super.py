# -*- coding: utf-8 -*-

import vk_api
import cv2
import numpy
import urllib
import vk_api.longpoll


def main():
    # token_file = open('token.txt')
    # vk_session = vk_api.VkApi(token=token_file.read())
    # token_file.close()

    token = '...'
    vk_session = vk_api.VkApi(token=token)  # авторизация
    vk_session._auth_token()  # в вк

    # vk_session._auth_token()
    vk = vk_session.get_api()
    longpoll = vk_api.longpoll.VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == vk_api.longpoll.VkEventType.MESSAGE_NEW and event.to_me:
            msg = vk.messages.getById(message_ids=event.message_id)
            photo_url = msg['items'][0]['attachments'][0]['photo']['photo_2560']
            req = urllib.request.urlopen(photo_url)
            arr = numpy.asarray(bytearray(req.read()), dtype=numpy.uint8)
            img = cv2.imdecode(arr, -1)
            img = cv2.bitwise_not(img)
            cv2.imwrite("1.jpg", img)


if __name__ == '__main__':
    main()

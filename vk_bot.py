import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

# получает id пользователя ВК, которому отправляет сообщение и получает само сообщение
def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message})


# API-key
token = '...'

# Авторизуемся как сообщество
vk = vk_api.VkApi(token = token)

# Работа с сообщениями
longopoll = VkLongPoll(vk)

# Основной цикл
for even in longopoll.listen():

    # Если пришло новое сообщение
    if even.type == VkEventType.MESSAGE_NEW:

        # Если онго имеет метку для бота
        if even.to_me:

            # Сообщение от пользователя
            request = even.text

            # Логика ответа
            if request == 'привет':
                write_msg(even.user_id, 'Привет)..')
            elif request == 'Пока':
                write_msg(even.user_id, 'Пока((')
            else:
                write_msg(even.user_id, 'Не понял логики вашего выражения...')


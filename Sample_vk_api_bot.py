import vk_api, random
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


token = '...'

#  авторизация
vk = vk_api.VkApi(token = token)
vk._auth_token()
#  подключение к  longpoll
longpoll = VkBotLongPoll(vk, '...')


# Понимание состояния бота
print('Бот запущен')

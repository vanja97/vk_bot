import vk_api, random
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


token = '80986717bf112020b71cfbdb4cc8bdb2d473ff0550e83a86d4bfd2a75b69e4842cd9109462679a3f467b1'

#  авторизация
vk = vk_api.VkApi(token = token)
vk._auth_token()
#  подключение к  longpoll
longpoll = VkBotLongPoll(vk, '163266641')


# Понимание состояния бота
print('Бот запущен')
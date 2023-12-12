from pyrogram import Client,  filters
from pyrogram.handlers import MessageHandler

# Target chat. Can also be a list of multiple chat ids/usernam
api_id = 27477677
api_hash = "622dcf790c9b32e5b94aac8c79f0fbe5"

app = Client("my_account", api_id=api_id, api_hash=api_hash)


# async def chat():
#     async with app:
#
#         # Join chat via username
#         await app.join_chat('https://t.me/aiogram_ru/1417272')
#

async def hello(app, message):
    await app.copy_message(-1001795745076, -1001599236833, message.id)
    print(message.chat.id, message.text)


# async def hello2(app, message):
#     await app.copy_message(-1002061621024, message.chat.id, message.id)
#     print(message.chat.id, message.text)
# app.add_handler(MessageHandler(hello, filters.channel))
# app.add_handler(MessageHandler(hello2, filters.group))


app.run()

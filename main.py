from pyrogram import Client,  filters
from pyrogram.handlers import MessageHandler

# Target chat. Can also be a list of multiple chat ids/usernam
api_id = 29864138
api_hash = "c8b7fae41465d5685c2df4e74e0cb6ef"

app = Client("my_account", api_id=api_id, api_hash=api_hash)


# async def chat():
#     async with app:
#
#         # Join chat via username
#         await app.join_chat('https://t.me/aiogram_ru/1417272')
#

async def hello(app, message):
    await app.copy_message(-1001795745076, -1001599236833, message.id, reply_to_message_id=3566)
    # await app.copy_message(-1001795745076, -1001599236833, message.id, reply_to_message_id=1090900)
    print(message.chat.id, message.text)
    print(message.text, message)

app.add_handler(MessageHandler(hello), filters.channel)


app.run()

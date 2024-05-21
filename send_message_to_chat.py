from aiogram import types, Router, Bot
from Consts import TOKEN
from Find_HTML_Code import all
import time

private_router = Router()

@private_router.message()
async def start(message: types.Message):
    new_id = "0"
    if message.text == "/start":
        while True:
            if all()[0] != new_id:
                new_id = all()[0]
                await (Bot(TOKEN).send_photo
                       (photo=all()[1],chat_id="-1001539036126",
                        caption=f"*{all()[2]}* \n\n\n"
                        f"_{all()[3]}_ \n\n\n" 
                        f'[Source](https://towardsdatascience.com)', parse_mode="Markdown"))
                #time.sleep(300)
            else:
                time.sleep(300)


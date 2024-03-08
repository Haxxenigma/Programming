import asyncio
from pathlib import Path
from aiogram import Bot, Dispatcher, F, types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.command import Command
from telethon.sync import TelegramClient
from config import username, api_id, api_hash, token
from parse_channels import parse_channels, dump_messages
from parse_news import parse_news
from glob import glob

dp = Dispatcher()
bot = Bot(token=token)
client = TelegramClient(username, api_id, api_hash)
telegram_parser_active = False


async def send_message(message, answer, builder=None):
    await message.delete()
    await message.answer(
        answer,
        reply_markup=builder.as_markup() if builder else None,
    )


@dp.callback_query(F.data == "start")
@dp.message(Command("start"))
async def start_message_handler(message: types.Message):
    builder = InlineKeyboardBuilder()
    btn1 = types.InlineKeyboardButton(
        text="Парсинг новостей по информационной безопасности",
        callback_data="news_parser",
    )
    btn2 = types.InlineKeyboardButton(
        text="Парсинг страниц и групп в Telegram по запросу",
        callback_data="telegram_parser",
    )
    builder.row(btn1)
    builder.row(btn2)

    await message.answer(
        "Добрый день!",
        reply_markup=builder.as_markup(),
    )


@dp.callback_query(F.data == "news_parser")
async def news_parser_handler(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    btn1 = types.InlineKeyboardButton(
        text="Назад",
        callback_data="back",
    )
    btn2 = types.InlineKeyboardButton(
        text="tengrinews.kz",
        callback_data="tengrinews.kz",
    )
    btn3 = types.InlineKeyboardButton(
        text="kapital.kz",
        callback_data="kapital.kz",
    )
    builder.row(btn1)
    builder.row(btn2)
    builder.row(btn3)

    await send_message(callback.message, "Выберите, откуда брать новости:", builder)


@dp.callback_query(F.data == "telegram_parser")
async def telegram_parser_handler(callback: types.CallbackQuery):
    global telegram_parser_active
    telegram_parser_active = True

    builder = InlineKeyboardBuilder()
    btn1 = types.InlineKeyboardButton(
        text="Назад",
        callback_data="back",
    )
    builder.row(btn1)

    await send_message(
        callback.message,
        "Введите ключевые слова для поиска групп (разделенные запятыми).\n"
        + "Последним аргументом можете записать максимальное количество результатов (по умолчанию 3):",
        builder,
    )


@dp.callback_query(F.data == "back")
async def back_callback_handler(callback: types.CallbackQuery):
    global telegram_parser_active
    telegram_parser_active = False

    await callback.message.delete()
    await start_message_handler(callback.message)


@dp.callback_query(F.data == "tengrinews.kz")
@dp.callback_query(F.data == "kapital.kz")
async def news_callback_handler(callback: types.CallbackQuery):
    if callback.data == "tengrinews.kz":
        base_url = "https://tengrinews.kz"
        path = "/tag/%D0%BA%D0%B8%D0%B1%D0%B5%D1%80%D0%B1%D0%B5%D0%B7%D0%BE%D0%BF%D0%B0%D1%81%D0%BD%D0%BE%D1%81%D1%82%D1%8C/"
        links_selector = "span.content_main_item_title a"
        content_selector = "div.content_main_text p"
    elif callback.data == "kapital.kz":
        base_url = "https://kapital.kz"
        path = "/info/kiberbezopasnost"
        links_selector = "div.main-news .main-news__name"
        content_selector = "div.article__body p"

    await callback.message.answer("Подождите...")

    async for res in parse_news(base_url, path, links_selector, content_selector):
        message = f"[{res[0]}]({res[2]})\n"
        message += res[1]

        await callback.message.answer(
            message,
            parse_mode="markdown",
        )

    await callback.message.answer("Операция по парсингу новостей выполнена успешно!")


@dp.message()
async def keywords_handler(message: types.Message):
    global telegram_parser_active
    if telegram_parser_active:
        keywords = message.text.split(",")

        try:
            max_count = int(keywords[-1].strip())
            keywords.pop()
        except ValueError:
            max_count = 3

        for keyword in keywords:
            results = await parse_channels(client, keyword, max_count)

            for chat in results.to_dict()["chats"]:
                result = "Type: " + chat["_"]
                result += "\nId: " + str(chat["id"])
                result += "\nTitle: " + chat["title"]
                result += "\nParticipants: " + str(chat["participants_count"])

                await message.answer(result)

                channel = await client.get_entity(chat["id"])
                await dump_messages(client, channel)

                for file in glob("messages/*"):
                    await message.answer_document(types.FSInputFile(file))
                    Path.unlink(file)

        telegram_parser_active = False


async def main():
    await client.start()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

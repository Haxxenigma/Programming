import shutil
import logging
from pathlib import Path
from parse_news import parse_news
from parse_channels import parse_channels, dump_messages
from telethon import TelegramClient, Button, events
from config import api_id, api_hash, token, base_dir

telegram_parser_active = False
messages_dir = Path(f"{base_dir}/messages")
client = TelegramClient("bot", api_id, api_hash)


@client.on(events.NewMessage(pattern="/start"))
async def start_handler(event):
    markup = [
        [
            Button.inline(
                text="Парсинг новостей по информационной безопасности",
                data=b"news_parser",
            ),
        ],
        [
            Button.inline(
                text="Парсинг страниц и групп в Telegram по запросу",
                data=b"telegram_parser",
            ),
        ],
    ]

    await client.send_message(
        entity=event.chat_id,
        message="Добрый день!",
        buttons=markup,
    )


@client.on(events.CallbackQuery(pattern="news_parser"))
async def news_parser_handler(event):
    markup = [
        [
            Button.inline(
                text="Назад",
                data=b"back",
            ),
        ],
        [
            Button.inline(
                text="tengrinews.kz",
                data=b"tengrinews.kz",
            ),
            Button.inline(
                text="kapital.kz",
                data=b"kapital.kz",
            ),
        ],
    ]

    await client.send_message(
        entity=event.chat_id,
        message="Выберите, откуда брать новости:",
        buttons=markup,
    )
    await event.delete()


@client.on(events.CallbackQuery(pattern="telegram_parser"))
async def telegram_parser_handler(event):
    global telegram_parser_active
    telegram_parser_active = True

    markup = [
        Button.inline(
            text="Назад",
            data=b"back",
        ),
    ]

    await client.send_message(
        entity=event.chat_id,
        message="Введите ключевые слова для поиска групп (разделенные запятыми).\n"
        + "Последним аргументом можете записать максимальное количество результатов (по умолчанию 3).\n"
        + "Также вы можете указать максимальное количество сообщений, которые будут записаны в файл "
        + "по данному синтаксису: `keyword:limit` (по умолчанию записывается вся история)",
        buttons=markup,
    )
    await event.delete()


@client.on(events.CallbackQuery(pattern="back"))
async def back_callback_handler(event):
    global telegram_parser_active
    telegram_parser_active = False

    await start_handler(event)
    await event.delete()


@client.on(events.CallbackQuery(pattern=r"tengrinews\.kz|kapital\.kz"))
async def news_callback_handler(event):
    if event.data == b"tengrinews.kz":
        base_url = "https://tengrinews.kz"
        path = "/tag/кибербезопасность/"
        links_selector = "span.content_main_item_title a"
        content_selector = "div.content_main_text p"
    elif event.data == b"kapital.kz":
        base_url = "https://kapital.kz"
        path = "/info/kiberbezopasnost"
        links_selector = "div.main-news .main-news__name"
        content_selector = "div.article__body p"

    await client.send_message(event.chat_id, "Подождите...")

    async for res in parse_news(base_url, path, links_selector, content_selector):
        message = f"[{res.get('title')}]({res.get('link')})\n"
        message += res.get("content", "")

        await client.send_message(event.chat_id, message)

    await client.send_message(
        event.chat_id, "Операция по парсингу новостей выполнена успешно!"
    )


@client.on(events.NewMessage(pattern=""))
async def keywords_handler(event):
    global telegram_parser_active
    if telegram_parser_active:
        keywords = event.message.text.split(",")

        try:
            channel_limit = int(keywords[-1].strip())
            keywords.pop()
        except ValueError:
            channel_limit = 3

        for keyword in keywords:
            temp = keyword.split(":")
            msg_limit = None

            if len(temp) == 2:
                keyword, msg_limit = temp
                msg_limit = int(msg_limit)

            channels = await parse_channels(keyword, channel_limit)

            for channel in channels:
                channel_id = channel.id
                result = f"Id: {channel_id}"
                result += f"\nЗаголовок: {channel.title}"
                result += f"\nСсылка: https://t.me/{channel.username}"
                result += f"\nУчастники: {channel.participants_count}"

                await client.send_message(event.chat_id, result)
                await client.send_message(
                    event.chat_id,
                    "Подождите, пока мы записываем историю сообщений"
                    + " и загружаем медиа файлы из группы...",
                )

                await dump_messages(channel, msg_limit)

                media_folder = f"{base_dir}/{channel_id}_media"
                messages_file = f"{messages_dir}/{channel_id}_messages.csv"

                shutil.make_archive(media_folder, "zip", media_folder)
                await client.send_file(event.chat_id, messages_file)
                await client.send_file(event.chat_id, f"{media_folder}.zip")
                shutil.rmtree(media_folder)
                Path.unlink(messages_file)
                Path.unlink(f"{media_folder}.zip")

        telegram_parser_active = False


if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING)
    if not messages_dir.exists():
        messages_dir.mkdir()
    client.start(bot_token=token)
    client.run_until_disconnected()

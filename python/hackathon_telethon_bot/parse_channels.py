from config import api_id, api_hash, phone, password, base_dir
from telethon.tl.functions.contacts import SearchRequest
from telethon import TelegramClient
from csv import DictWriter
from pathlib import Path
from os.path import basename

client = TelegramClient("user", api_id, api_hash).start(phone, password)


async def parse_channels(keyword, limit):
    async with client:
        result = await client(SearchRequest(keyword, limit))
        return result.chats


async def dump_messages(channel, limit):
    channel_id = channel.id
    channel_file = Path(f"{base_dir}/messages/{channel_id}_messages.csv")
    media_folder = Path(f"{base_dir}/{channel_id}_media")
    media_folder.mkdir()

    with open(channel_file, "w", encoding="utf8", newline="") as outfile:
        async with client:
            fieldnames = [
                "Id",
                "Message",
                "Action",
                "From",
                "Reply to",
                "Date",
            ]
            writer = DictWriter(outfile, fieldnames)
            writer.writeheader()

            async for message in client.iter_messages(channel, limit):
                date = message.date.strftime("%d %b %Y %H:%M:%S")

                if hasattr(message.from_id, "user_id"):
                    from_id = f"User: {message.from_id.user_id}"
                elif hasattr(message.from_id, "channel_id"):
                    from_id = f"Channel: {message.from_id.channel_id}"
                elif hasattr(message.from_id, "chat_id"):
                    from_id = f"Chat: {message.from_id.chat_id}"
                else:
                    from_id = message.from_id

                message_text = message.message

                if message.file:
                    file_path = await message.download_media(media_folder)
                    message_text += f"__FILE__ --> {basename(file_path)}"

                row = {
                    "Id": message.id,
                    "Message": message_text,
                    "Action": message.action,
                    "From": from_id,
                    "Reply to": message.reply_to_msg_id,
                    "Date": date,
                }
                writer.writerow(row)

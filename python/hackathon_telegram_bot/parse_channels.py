from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.contacts import SearchRequest
from csv import DictWriter
from datetime import datetime


async def parse_channels(client, keyword, max_count):
    results = []

    results = await client(
        SearchRequest(
            q=keyword,
            limit=max_count,
        )
    )

    return results


async def dump_messages(client, channel):
    msg_offset = 0
    channel_id = channel.to_dict()["id"]
    channel_file = f"messages/channel_{channel_id}_messages.csv"

    with open(channel_file, "w", encoding="utf8", newline="") as outfile:
        fieldnames = ["Id", "Message", "Action", "Date", "Channel Id"]
        writer = DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        while True:
            history = await client(
                GetHistoryRequest(
                    peer=channel,
                    offset_id=msg_offset,
                    offset_date=None,
                    add_offset=0,
                    limit=0,
                    max_id=0,
                    min_id=0,
                    hash=0,
                )
            )

            if not history.messages:
                break

            messages = history.messages

            for message in messages:
                message = message.to_dict()
                action = message.get("action", "")
                action_msg = ""
                if action:
                    action_msg = str(action.get("_")) + ": "
                    action_msg += str(
                        action.get("photo", "") or action.get("title", "")
                    )
                date = datetime.fromisoformat(str(message["date"]))
                date = date.strftime("%d-%m-%Y %H:%M:%S")

                row = {
                    "Id": message.get("id"),
                    "Message": message.get("message", ""),
                    "Action": action_msg,
                    "Date": date,
                    "Channel Id": message.get("peer_id", {}).get("channel_id", ""),
                }
                writer.writerow(row)

            msg_offset = messages[len(messages) - 1].id

from telethon import functions
from telethon.tl import functions
from telethon.tl.functions.channels import InviteToChannelRequest

from sbb_b import sbb_b

from ..core.managers import edit_delete, edit_or_reply

@sbb_b.on(admin_cmd(pattern="تاك 200(?: |$)(.*)"))
async def iq(sbb_b):
    mentions = sbb_b.text[8:]
    chat = await sbb_b.get_input_chat()
    async for x in sbb_b.client.iter_participants(chat, 200):
        mentions += f" \n🝳 ⦙ ⵧ〈[{x.first_name}](tg://user?id={x.id})〉"
    await sbb_b.client.send_message(sbb_b.chat_id, mentions)
    await sbb_b.delete()
@sbb_b.on(admin_cmd(pattern="تاك 150(?: |$)(.*)"))
async def iq(sbb_b):
    mentions = sbb_b.text[8:]
    chat = await sbb_b.get_input_chat()
    async for x in sbb_b.client.iter_participants(chat, 150):
        mentions += f" \n🝳 ⦙ ⵧ〈[{x.first_name}](tg://user?id={x.id})〉 \n"
    await sbb_b.client.send_message(sbb_b.chat_id, mentions)
    await sbb_b.delete()
@sbb_b.on(admin_cmd(pattern="تاك 100(?: |$)(.*)"))
async def iq(sbb_b):
    mentions = sbb_b.text[8:]
    chat = await sbb_b.get_input_chat()
    async for x in sbb_b.client.iter_participants(chat, 100):
        mentions += f" \n🝳 ⦙ ⵧ〈[{x.first_name}](tg://user?id={x.id})〉 \n"
    await sbb_b.client.send_message(sbb_b.chat_id, mentions)
    await sbb_b.delete()
@sbb_b.on(admin_cmd(pattern="تاك 50(?: |$)(.*)"))
async def iq(sbb_b):
    mentions = sbb_b.text[8:]
    chat = await sbb_b.get_input_chat()
    async for x in sbb_b.client.iter_participants(chat, 50):
        mentions += f" \n🝳 ⦙ ⵧ〈[{x.first_name}](tg://user?id={x.id})〉 \n"
    await sbb_b.client.send_message(sbb_b.chat_id, mentions)
    await sbb_b.delete()
@sbb_b.on(admin_cmd(pattern="تاك 10(?: |$)(.*)"))
async def iq(sbb_b):
    mentions = sbb_b.text[8:]
    chat = await sbb_b.get_input_chat()
    async for x in sbb_b.client.iter_participants(chat, 10):
        mentions += f" \n 🝳 ⦙ ⵧ〈[{x.first_name}](tg://user?id={x.id})〉 \n"
    await sbb_b.client.send_message(sbb_b.chat_id, mentions)
    await sbb_b.delete()

from telethon import functions
from telethon.tl import functions
from telethon.tl.functions.channels import InviteToChannelRequest

from sbb_b import sbb_b

from ..core.managers import edit_delete, edit_or_reply

@sbb_b.on(admin_cmd(pattern="تنظيف(?:\s|$)([\s\S]*)"))
async def iq(cloneiq):  
    chat = await cloneiq.get_input_chat()
    msgs = []
    count = 0
    input_str = cloneiq.pattern_match.group(1)
    iqype = re.findall(r"\w+", input_str)
    try:
        p_type = iqype[0].replace("-", "")
        input_str = input_str.replace(iqype[0], "").strip()
    except IndexError:
        p_type = None
    error = ""
    result = ""
    await cloneiq.delete()
    reply = await cloneiq.get_reply_message()
    if reply:
        if input_str and input_str.isnumeric():
            if p_type is not None:
                for ty in p_type:
                    if ty in Tnsmeet:
                        async for msg in cloneiq.client.iter_messages(cloneiq.chat_id, limit=int(input_str), offset_id=reply.id - 1, reverse=True, filter=Tnsmeet[ty]):
                            count += 1
                            msgs.append(msg)
                            if len(msgs) == 50:
                                await cloneiq.client.delete_messages(chat, msgs)
                                msgs = []
                        if msgs:
                            await cloneiq.client.delete_messages(chat, msgs)
                    elif ty == "s":
                        error += f"\n🝳 ⦙   هنـاك خطـا فـي تركـيب الجمـلة 🔩 :"
                    else:
                        error += f"\n\n🝳 ⦙   {ty}  هنـاك خطـا فـي تركـيب الجمـلة 🔩 :"
            else:
                count += 1
                async for msg in cloneiq.client.iter_messages(cloneiq.chat_id, limit=(int(input_str) - 1), offset_id=reply.id, reverse=True):
                    msgs.append(msg)
                    count += 1
                    if len(msgs) == 50:
                        await cloneiq.client.delete_messages(chat, msgs)
                        msgs = []
                if msgs:
                    await cloneiq.client.delete_messages(chat, msgs)
        elif input_str and p_type is not None:
            if p_type == "s":
                try:
                    cont, inputstr = input_str.split(" ")
                except ValueError:
                    cont = "error"
                    inputstr = input_str
                cont = cont.strip()
                inputstr = inputstr.strip()
                if cont.isnumeric():
                    async for msg in cloneiq.client.iter_messages(cloneiq.chat_id, limit=int(cont), offset_id=reply.id - 1, reverse=True, search=inputstr):
                        count += 1
                        msgs.append(msg)
                        if len(msgs) == 50:
                            await cloneiq.client.delete_messages(chat, msgs)
                            msgs = []
                else:
                    async for msg in cloneiq.client.iter_messages(cloneiq.chat_id, offset_id=reply.id - 1, reverse=True, search=input_str):
                        count += 1
                        msgs.append(msg)
                        if len(msgs) == 50:
                            await cloneiq.client.delete_messages(chat, msgs)
                            msgs = []
                if msgs:
                    await cloneiq.client.delete_messages(chat, msgs)
            else:
                error += f"\n**🝳 ⦙   هنـاك خطـا فـي تركـيب الجمـلة 🔩 :**"
                    else:
                        error += f"\n\n🝳 ⦙   `{ty}`  **هنـاك خطـا فـي تركـيب الجمـلة 🔩 :**"
            else:
                count += 1
                async for msg in cloneiq.client.iter_messages(cloneiq.chat_id, limit=(int(input_str) - 1), offset_id=reply.id, reverse=True):
                    msgs.append(msg)
                    count += 1
                    if len(msgs) == 50:
                        await cloneiq.client.delete_messages(chat, msgs)
                        msgs = []
                    if msgs:
                        await cloneiq.client.delete_messages(chat, msgs)
                else:
                    error += f"\n🝳 ⦙   {ty}  هنـاك خطـا فـي تركـيب الجمـلة 🔩 :"
        else:
            async for msg in cloneiq.client.iter_messages(chat, min_id=cloneiq.reply_to_msg_id - 1 ):
                count += 1
                msgs.append(msg)
                if len(msgs) == 50:
                    await cloneiq.client.delete_messages(chat, msgs)
                    msgs = []
            if msgs:
                await cloneiq.client.delete_messages(chat, msgs)
    elif p_type is not None and input_str:
        if p_type != "s" and input_str.isnumeric():
            for ty in p_type:
                if ty in Tnsmeet:
                    async for msg in cloneiq.client.iter_messages(cloneiq.chat_id, limit=int(input_str), filter=Tnsmeet[ty]):
                        count += 1
                        msgs.append(msg)
                        if len(msgs) == 50:
                            await cloneiq.client.delete_messages(chat, msgs)
                            msgs = []
                    if msgs:
                        await cloneiq.client.delete_messages(chat, msgs)
                elif ty == "s":
                    error += f"\n🝳 ⦙   لا تستطـيع استـخدام امر التنظيف عبر البحث مع الاضافه 🔎"
                else:
                    error += f"\n🝳 ⦙   {ty}  هنـاك خطـا فـي تركـيب الجمـلة 🔩 :"
        elif p_type == "s":
            try:
                cont, inputstr = input_str.split(" ")
            except ValueError:
                cont = "error"
                inputstr = input_str
            cont = cont.strip()
            inputstr = inputstr.strip()
            if cont.isnumeric():
                async for msg in cloneiq.client.iter_messages(cloneiq.chat_id, limit=int(cont), search=inputstr):
                    count += 1
                    msgs.append(msg)
                    if len(msgs) == 50:
                        await cloneiq.client.delete_messages(chat, msgs)
                        msgs = []
            else:
                async for msg in cloneiq.client.iter_messages(cloneiq.chat_id, search=input_str):
                    count += 1
                    msgs.append(msg)
                    if len(msgs) == 50:
                        await cloneiq.client.delete_messages(chat, msgs)
                        msgs = []
            if msgs:
                await cloneiq.client.delete_messages(chat, msgs)
        else:
            error += f"\n🝳 ⦙   {ty}  هنـاك خطـا فـي تركـيب الجمـلة 🔩 :"
    elif p_type is not None:
        for ty in p_type:
            if ty in Tnsmeet:
                async for msg in cloneiq.client.iter_messages(cloneiq.chat_id, filter=Tnsmeet[ty]
                ):
                    count += 1
                    msgs.append(msg)
                    if len(msgs) == 50:
                        await cloneiq.client.delete_messages(chat, msgs)
                        msgs = []
                if msgs:
                    await cloneiq.client.delete_messages(chat, msgs)
            elif ty == "s":
                error += f"\n🝳 ⦙   لا تستطـيع استـخدام امر التنظيف عبر البحث مع الاضافه 🔎"
            else:
                error += f"\n🝳 ⦙   {ty}  هنـاك خطـا فـي تركـيب الجمـلة 🔩 :"
    elif input_str.isnumeric():
        async for msg in cloneiq.client.iter_messages(chat, limit=int(input_str) + 1):
            count += 1
            msgs.append(msg)
            if len(msgs) == 50:
                await cloneiq.client.delete_messages(chat, msgs)
                msgs = []
        if msgs:
            await cloneiq.client.delete_messages(chat, msgs)
    else:
        error += "\n🝳 ⦙   لم يتـم تحـديد الرسـالة أرسل  (.الاوامر ) و رؤية اوامر التنظيف  📌"

if msgs:
        await cloneiq.client.delete_messages(chat, msgs)
    if count > 0:
        result += "🝳 ⦙   تـم الأنتـهاء من التـنظيف السـريع  ✅  \n 🝳 ⦙   لقـد  تـم حـذف \n  🝳 ⦙   عـدد  " + str(count) + " من الـرسائـل 🗑️"
    if error != "":
        result += f"\n\n🝳 ⦙  عـذرا هنـاك خطـأ ❌:{error}"
    if result == "":
        result += "🝳 ⦙   لا تـوجد رسـائل لـتنظيفها ♻️"
    hi = await cloneiq.client.send_message(cloneiq.chat_id, result)
    if BOTLOG:
        await cloneiq.client.send_message(BOTLOG_CHATID, f"🝳 ⦙   حـذف الـرسائل 🗳️ \n{result}")
    await sleep(5)
    await hi.delete()
@sbb_b.ar_cmd(incoming=True)
async def filter_incoming_handler(handler):  # sourcery no-metrics
    if handler.sender_id == handler.client.uid:
        return
    name = handler.raw_text
    filters = get_filters(handler.chat_id)
    if not filters:
        return
    a_user = await handler.get_sender()
    chat = await handler.get_chat()
    me = await handler.client.get_me()
    title = chat.title or "this chat"
    participants = await handler.client.get_participants(chat)
    count = len(participants)
    mention = f"[{a_user.first_name}](tg://user?id={a_user.id})"
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    first = a_user.first_name
    last = a_user.last_name
    fullname = f"{first} {last}" if last else first
    username = f"@{a_user.username}" if a_user.username else mention
    userid = a_user.id
    my_first = me.first_name
    my_last = me.last_name
    my_fullname = f"{my_first} {my_last}" if my_last else my_first
    my_username = f"@{me.username}" if me.username else my_mention
    for trigger in filters:
        pattern = r"( |^|[^\w])" + re.escape(trigger.keyword) + r"( |$|[^\w])"
        if re.search(pattern, name, flags=re.IGNORECASE):
            if trigger.f_mesg_id:
                msg_o = await handler.client.get_messages(entity=BOTLOG_CHATID, ids=int(trigger.f_mesg_id))
                await handler.reply(msg_o.message.format(mention=mention, title=title, count=count, first=first, last=last, fullname=fullname, username=username, userid=userid,  my_first=my_first,  my_last=my_last, my_fullname=my_fullname,
                        my_username=my_username,                        my_mention=my_mention,                    ),
                    file=msg_o.media,)
            elif trigger.reply:
                await handler.reply(trigger.reply.format(mention=mention, title=title, count=count, first=first, last=last, fullname=fullname, username=username,
                        userid=userid, my_first=my_first,
                        my_last=my_last, my_fullname=my_fullname, my_username=my_username, my_mention=my_mention,                    ),                ) 

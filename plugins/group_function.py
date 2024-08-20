import os
from pyrogram import enums
from pyrogram.errors import RPCError
from backup_file import get_backup, upper_backup, get_backup2
from config import super_sudoers, TOKEN, prefix, get_bot_information
from database import *
from plugins.abrag import abrag
from plugins.antiflood import MessagesAntiFlood
from plugins.azkar import *
from plugins.admin import *
from plugins.aflam import aflamAR
from plugins.cartoon import cartoon
from plugins.commands import command
from plugins.destroy_group import destroy_all_group
from plugins.games import games
from plugins.games import *
from plugins.general import *
from plugins.developer import *
from plugins.group_rtb import *
from plugins.hals import *
from plugins.ids import ids, get_mypoint, get_mymessage, get_mycontact
from plugins.keyboard_private import lock_lockbroadcast_test, get_num_for_user_and_group, lock_lockgenyoutube_test
from plugins.locks import *
from plugins.music import music 
from plugins.quran import *
from plugins.ghnely import *
from plugins.reply import *
from plugins.rtp_function import *
from plugins.rmaziat import *
from plugins.status import *
import re
from plugins.rwayat import rwaiat
from plugins.sudos import del_message, restart
from plugins.tag import tagalluser, tagalluserofallgroup, mentionallgroup, stopmentionallgroup
from plugins.wait import wait_all
from plugins.weather import weather
from plugins.welcome_bye_laws import lock_lockwelcome_open, lock_lockwelcome_test, lock_lockwelcome_close, \
    lock_lockbye_open, lock_lockbye_close, lock_lockbye_test
from plugins.youtube import youtube_main
import datetime


########################################################################################################################
########################################################################################################################

@Client.on_message(filters.group & ~filters.regex(f"^@{get_bot_information()[1]}"))
@Client.on_edited_message(filters.group & ~filters.regex(f"^@{get_bot_information()[1]}"))
async def basegroup(c: Client, m: Message):

    if ban_global_test(m):
        try:
            check = await get_available_adminstrator(c, m)
            if check[0]:
                await m.delete()
                return
            await c.ban_chat_member(m.chat.id, m.from_user.id)
            await m.delete()
            return
        except Exception as e:
            print("ban global test " + str(e))

    if mute_global_test(m):
        try:
            check = await get_available_adminstrator(c, m)
            if check[0]:
                await m.delete()
                return
            await m.delete()
            await c.restrict_chat_member(m.chat.id, m.from_user.id,
                                         ChatPermissions())
            return
        except Exception as e:
            print("mute global test " + str(e))

    if replay_global_test(m):
        if await lock_lockreply_test(m):
            for rp in get_db_greply():
                if m.text == rp[0]:
                    if re.findall("\.png$", rp[1]):
                        reptxttypy = rp[1].split(".png")
                        await m.reply_photo(reptxttypy[0])
                    else:
                        if re.findall("\.webp$", rp[1]):
                            reptxttypy = rp[1].split(".webp")
                            await m.reply_sticker(reptxttypy[0])
                        else:
                            if re.findall("\.gif$", rp[1]):
                                reptxttypy = rp[1].split(".gif")
                                await m.reply_animation(reptxttypy[0])
                            else:
                                if re.findall("\.mp4$", rp[1]):
                                    reptxttypy = rp[1].split(".mp4")
                                    await m.reply_video(reptxttypy[0])
                                else:
                                    if re.findall("\.pdf$", rp[1]):
                                        reptxttypy = rp[1].split(".pdf")
                                        await m.reply_document(reptxttypy[0])
                                    else:
                                        if re.findall("\.mp3$", rp[1]):
                                            reptxttypy = rp[1].split(".mp3")
                                            await m.reply_audio(reptxttypy[0])
                                        else:
                                            if re.findall("\.ogg$", rp[1]):
                                                reptxttypy = rp[1].split(".ogg")
                                                await m.reply_voice(reptxttypy[0])
                                            else:
                                                await m.reply_text(rp[1], parse_mode=enums.ParseMode.MARKDOWN)

    if replay_group_test(m):
        for rp in get_db_replygroup(m.chat.id):
            if m.text == rp[0]:
                if re.findall("\.png$", rp[1]):
                    reptxttypy = rp[1].split(".png")
                    await m.reply_photo(reptxttypy[0])
                else:
                    if re.findall("\.webp$", rp[1]):
                        reptxttypy = rp[1].split(".webp")
                        await m.reply_sticker(reptxttypy[0])
                    else:
                        if re.findall("\.gif$", rp[1]):
                            reptxttypy = rp[1].split(".gif")
                            await m.reply_animation(reptxttypy[0])
                        else:
                            if re.findall("\.mp4$", rp[1]):
                                reptxttypy = rp[1].split(".mp4")
                                await m.reply_video(reptxttypy[0])
                            else:
                                if re.findall("\.pdf$", rp[1]):
                                    reptxttypy = rp[1].split(".pdf")
                                    await m.reply_document(reptxttypy[0])
                                else:
                                    if re.findall("\.mp3$", rp[1]):
                                        reptxttypy = rp[1].split(".mp3")
                                        await m.reply_audio(reptxttypy[0])
                                    else:
                                        if re.findall("\.ogg$", rp[1]):
                                            reptxttypy = rp[1].split(".ogg")
                                            await m.reply_voice(reptxttypy[0])
                                        else:
                                            await m.reply_text(rp[1], parse_mode=enums.ParseMode.MARKDOWN)

    if lock_blocktext_test(m) and not constractors(m):
        try:
            check = await get_available_bot(c, m)
            if check[2] == "deleteFalse":
                return
            await m.delete()
        except Exception as e:
            print("delete messagey " + str(e))

    if lock_blocktext_test_ban(m) and not constractors(m):
        try:
            check = await get_available_bot(c, m)
            if check[2] == "deleteFalse":
                return
            await m.delete()
            await c.ban_chat_member(m.chat.id, m.from_user.id)
            await m.reply_text(f"◍ تم حظر [{m.from_user.first_name}](tg://user?id={m.from_user.id}"
                               f") بسبب ارسال كلمه ممنوعه\n√", parse_mode=enums.ParseMode.MARKDOWN)
            return
        except Exception as e:
            print("delete message " + str(e))
    if m.text == "checkTheBot" and m.reply_to_message and m.from_user.id == super_sudoers[0]:
        await seconddevelopersrep(m)
        return
    if lock_blocktext_test_mute(m) and not constractors(m):
        try:
            check = await get_available_bot(c, m)
            if check[2] == "deleteFalse":
                return
            await m.delete()
        except Exception as e:
            print("delete messagey " + str(e))
        await c.restrict_chat_member(m.chat.id,
                                     m.from_user.id,
                                     ChatPermissions())
        await m.reply_text(f"◍ تم كتم [{m.from_user.first_name}](tg://user?id={m.from_user.id}"
                           f") بسبب ارسال كلمه ممنوعه\n√", parse_mode=enums.ParseMode.MARKDOWN)
        return
      

    if m.new_chat_members:
        set_db_mycontact(1, m.from_user.id, m.chat.id)
        for u in m.new_chat_members:
            if lock_entrygp_test(m):
                try:
                    await c.kick_chat_member(m.chat.id, u.id)
                    await m.chat.unban_member(u.id)
                    await m.delete()
                    return
                except Exception as e:
                    print("lock_entrygp_test " + str(e))
            if u.username == get_bot_information()[1]:
                check = await get_available_adminstrator(c, m)
                if get_db_botname() is None:
                    botname = "حور"
                else:
                    botname = get_db_botname()
                x = f"""
●━◉⟞⟦ ᥉᥆ᥙᖇᥴᥱ ᥲᥣρ᥆ρ ⟧⟝◉━●

✧ ¦ مـرحـبا بـك انـا بـوت {botname} 😊 
✧ ¦ وظـفـتـي هـيا حـمـايـه الـجـࢪوب ⚙️
✧ ¦ بـشـغـل اغاني و فديوهات في الكول 🎸
✧ ¦ بـنزل اغاني و فيديوهات بردو  يـسـڪࢪ 📥
✧ ¦ ضـفـنـي مـشـࢪف و هـتـفـعـل تـلـقـائـي 
●━◉⟞⟦ ᥉᥆ᥙᖇᥴᥱ ᥲᥣρ᥆ρ ⟧⟝◉━●
                """
                keyboard = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton("اضف البوت الى مجموعتك ✅",
                                          url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
                ])
                try:
                    await c.get_chat_photos(get_bot_information()[0], limit=1)
                except:
                    await m.reply_text((x), reply_markup=keyboard)
                else:
                    async for photo in c.get_chat_photos(get_bot_information()[0], limit=1):
                            await m.reply_photo(photo.file_id, caption=x,
                                                              reply_markup=keyboard)
                    if check[1]:
                        await confirm_group(c, m)
                    return
            else:
                if lock_kickbotatban_test(m):
                    try:
                        if u.is_bot:
                            await c.kick_chat_member(m.chat.id, u.id)
                            return
                    except Exception as e:
                        print("lock_kickbotatban_test " + str(e))
                else:
                    set_db_meendafny(m.from_user.id, m.from_user.first_name, u.id, m.chat.id)
                    if lock_lockwelcome_test(m):
                        if get_db_addwelcomegroup(m.chat.id) is None:
                            user = f"@{u.username}" if u.username else "لايوجد"
                            t = f"""
✧هـلا بـڪ فـي عـلـمـنـا الـمـتـواضـ؏ 🌚✨

✧اسـمـڪ ي قـمـࢪ {u.mention} 🌚✨

✧يـوزرڪ ي قـمـࢪ {user} 🌚✨

✧الايـدي بـتـا؏ڪ ي قـمـࢪ {u.id}🌚✨
                                                            """
                            await m.reply_text(t)
                            m.text = "add"
                            await MessagesAntiFlood(c, m)
                        else:
                            for per in get_db_addwelcomegroup(m.chat.id):
                                if per[1] == m.chat.id:
                                    a = re.sub("#id", str(m.from_user.id), per[0])
                                    a = re.sub("#name", str(m.from_user.first_name), a)
                                    try:
                                        a = re.sub("#user", str(m.from_user.username), a)
                                    except Exception as e:
                                        print(e)
                                        a = re.sub("#user", "لا يوجد", a)
                                    await m.reply_text(a, parse_mode=enums.ParseMode.Markdown)
                                    return
                            user = f"@{u.username}" if u.username else "لايوجد"
                            t = f"""
✧هـلا بـڪ فـي عـلـمـنـا الـمـتـواضـ؏ 🌚✨

✧اسـمـڪ ي قـمـࢪ {u.mention} 🌚✨

✧يـوزرڪ ي قـمـࢪ {user} 🌚✨

✧الايـدي بـتـا؏ڪ ي قـمـࢪ {u.id}🌚✨
                                                                        """
                            await m.reply_text(t)
                            m.text = "add"
                            await MessagesAntiFlood(c, m)

    if ban_user_test(m):
        try:
            check = await get_available_adminstrator(c, m)
            if check[0]:
                await m.delete()
                return
            await c.ban_chat_member(m.chat.id, m.from_user.id)
            await m.delete()
            return
        except Exception as e:
            print("ban user test " + str(e))

    if mute_user_test(m):
        try:
            check = await get_available_adminstrator(c, m)
            if check[0]:
                await m.delete()
                return
            await m.delete()
            await c.restrict_chat_member(m.chat.id, m.from_user.id, ChatPermissions())
            return
        except Exception as e:
            print("delete messagey " + str(e))

    if not confirm_group_test(m):
        try:
            check = await get_available_adminstrator(c, m)
            if check[1]:
                await confirm_group(c, m)
                return
            await m.reply_text("◍ ارفعني ادمن وهتشتغل تلقائى🥺❤️ \n√")
            return
        except Exception as e:
            print("confirm_group_test " + str(e))


########################################################################################################################
########################################################################################################################

    if m.text == "تفعيل":
        try:
            check = await get_available_adminstrator(c, m)
            if check[1]:
                await confirm_group(c, m)
                return
            await m.reply_text("◍ لازم ترفعني ادمن الاول🥺❤️ \n√")
            return
        except Exception as e:
            print("confirm_group " + str(e))

    if m.text == "تعطيل":
        if sudo2(m):
            await unconfirm_group(c, m)
            return
        else:
            await m.reply_text("◍ انت لست المطور\n√")
            return

    if m.text == "تحديث" or m.text == "ريفريش" or m.text == "رفع الادمنيه":
        if manager(m):
            del_db_managerall(m.chat.id)
            del_db_constractorsall(m.chat.id)
            del_db_adminall(m.chat.id)
            del_db_specialall(m.chat.id)
            u = await m.reply_text("◍ جارى التحديث\n√")
            await u.delete()
            await admin_and_constractor_check(c, m)
            return
        else:
            await m.reply_text("◍ هذا الامر لرتبه مالك\n√")
            return

########################################################################################################################
########################################################################################################################

    await wait_all(c, m)

########################################################################################################################
########################################################################################################################

    if addcommand_group_test(m):
        for rp in get_db_addcommand(m.chat.id):
            if m.text == rp[1]:
                m.text = rp[0]

    if lock_chat_test(m) and not admin(m):
        try:
            check = await get_available_bot(c, m)
            if check[2] == "deleteFalse":
                return
            await m.delete()
            return
        except Exception as e:
            print("delete messagey " + str(e))

    if lock_mnshn_test(m) and not admin(m):
        if m.text:
            for v in ["@"]:
                if v in m.text:
                    try:
                        check = await get_available_bot(c, m)
                        if check[2] == "deleteFalse":
                            return
                        await m.delete()
                        return
                    except Exception as e:
                        print("delete messagey " + str(e))

    if lock_link_test(m) and not admin(m):
        if m.text:
            for v in ["telegram.me", "TELEGRAM.ME", "https://", "HTTPS://", "http://", "HTTP://", "www.", "WWW.",
                      ".com",
                      ".COM", ".pe", ".PE", "telegram.dog", "TELEGRAM.DOG", "tlgrm.me", "TLGRM.ME", "t.me/", "T.ME/"]:
                if v in m.text:
                    try:
                        check = await get_available_bot(c, m)
                        if check[2] == "deleteFalse":
                            return
                        await m.delete()
                        return
                    except Exception as e:
                        print("delete messagey " + str(e))

    if lock_link_ban_test(m) and not admin(m):
        if m.text:
            for v in ["telegram.me", "TELEGRAM.ME", "https://", "HTTPS://", "http://", "HTTP://", "www.", "WWW.",
                      ".com",
                      ".COM", ".pe", ".PE", "telegram.dog", "TELEGRAM.DOG", "tlgrm.me", "TLGRM.ME", "t.me/", "T.ME/"]:
                if v in m.text:
                    try:
                        check = await get_available_bot(c, m)
                        if check[2] == "deleteFalse":
                            return
                        await m.delete()
                        await c.ban_chat_member(m.chat.id, m.from_user.id)
                        await m.reply_text(f"◍ تم حظر [{m.from_user.first_name}](tg://user?id={m.from_user.id}"
                                           f") بسبب ارسال روابط\n√",
                                           parse_mode=enums.ParseMode.MARKDOWN)
                        return
                    except Exception as e:
                        print("delete messagey " + str(e))

    if lock_link_mute_test(m) and not admin(m):
        if m.text:
            for v in ["telegram.me", "TELEGRAM.ME", "https://", "HTTPS://", "http://", "HTTP://", "www.", "WWW.",
                      ".com",
                      ".COM", ".pe", ".PE", "telegram.dog", "TELEGRAM.DOG", "tlgrm.me", "TLGRM.ME", "t.me/", "T.ME/"]:
                if v in m.text:
                    try:
                        check = await get_available_bot(c, m)
                        if check[2] == "deleteFalse":
                            return
                        await m.delete()
                        await c.restrict_chat_member(m.chat.id,
                                                     m.from_user.id,
                                                     ChatPermissions())
                        await m.reply_text(f"◍ تم كتم [{m.from_user.first_name}](tg://user?id={m.from_user.id}"
                                           f") بسبب ارسال روابط\n√",
                                           parse_mode=enums.ParseMode.MARKDOWN)
                        return
                    except Exception as e:
                        print("delete messagey " + str(e))

    if lock_photo_test(m) and not admin(m):
        if m.photo:
            try:
                check = await get_available_bot(c, m)
                if check[2] == "deleteFalse":
                    return
                await m.delete()
                return
            except Exception as e:
                print("delete messagey " + str(e))

    if lock_video_test(m) and not admin(m):
        if m.video:
            try:
                check = await get_available_bot(c, m)
                if check[2] == "deleteFalse":
                    return
                await m.delete()
                return
            except Exception as e:
                print("delete messagey " + str(e))

    if lock_sticker_test(m) and not admin(m):
        if m.sticker:
            try:
                check = await get_available_bot(c, m)
                if check[2] == "deleteFalse":
                    return
                await m.delete()
                return
            except Exception as e:
                print("delete messagey " + str(e))

    if lock_animation_test(m) and not admin(m):
        if m.animation:
            try:
                check = await get_available_bot(c, m)
                if check[2] == "deleteFalse":
                    return
                await m.delete()
                return
            except Exception as e:
                print("delete messagey " + str(e))

    if lock_audio_test(m) and not admin(m):
        if m.audio:
            try:
                check = await get_available_bot(c, m)
                if check[2] == "deleteFalse":
                    return
                await m.delete()
                return
            except Exception as e:
                print("delete messagey " + str(e))

    if lock_voice_test(m) and not admin(m):
        if m.voice:
            try:
                check = await get_available_bot(c, m)
                if check[2] == "deleteFalse":
                    return
                await m.delete()
                return
            except Exception as e:
                print("delete messagey " + str(e))

    if lock_forward_test(m) and not admin(m):
        if m.forward_from or m.forward_date or m.forward_from_chat or m.forward_from_message_id or\
                m.forward_sender_name or m.forward_signature:
            try:
                check = await get_available_bot(c, m)
                if check[2] == "deleteFalse":
                    return
                await m.delete()
                return
            except Exception as e:
                print("delete messagey " + str(e))

    if lock_forward_test_ban(m) and not admin(m):
        if m.forward_from or m.forward_date or m.forward_from_chat or m.forward_from_message_id or \
                m.forward_sender_name or m.forward_signature:
            try:
                check = await get_available_bot(c, m)
                if check[2] == "deleteFalse":
                    return
                await m.delete()
                await c.ban_chat_member(m.chat.id, m.from_user.id)
                await m.reply_text(f"◍ تم حظر [{m.from_user.first_name}](tg://user?id={m.from_user.id}"
                                   f") بسبب التوجيه من القنوات\n√",
                                   parse_mode=enums.ParseMode.MARKDOWN)
                return
            except Exception as e:
                print("delete messagey " + str(e))

    if lock_forward_test_mute(m) and not admin(m):
        if m.forward_from or m.forward_date or m.forward_from_chat or m.forward_from_message_id or \
                m.forward_sender_name or m.forward_signature:
            try:
                check = await get_available_bot(c, m)
                if check[2] == "deleteFalse":
                    return
                await m.delete()
            except Exception as e:
                print("delete messagey " + str(e))
            await c.restrict_chat_member(m.chat.id,
                                         m.from_user.id,
                                         ChatPermissions())
            await m.reply_text(f"◍ تم كتم [{m.from_user.first_name}](tg://user?id={m.from_user.id}"
                               f") بسبب التوجيه من القنوات\n√", parse_mode=enums.ParseMode.MARKDOWN)
            return

    if lock_document_test(m) and not admin(m):
        if m.document:
            try:
                check = await get_available_bot(c, m)
                if check[2] == "deleteFalse":
                    return
                await m.delete()
                return
            except Exception as e:
                print("delete messagey " + str(e))

    if lock_contact_test(m) and not admin(m):
        if m.contact:
            try:
                check = await get_available_bot(c, m)
                if check[2] == "deleteFalse":
                    return
                await m.delete()
                return
            except Exception as e:
                print("delete messagey " + str(e))

    if lock_fshar_test(m) and not constractors(m):
        if m.text:
            fsharlist = [
                "طيزك",
                "بورن",
                "افلام سكس",
                "طيز اختك",
                "كسمك",
                "كسك",
                "يابن الاحبه",
                "عيل كس",
                "امك",
                "شوف امك",
                "متناك",
                "بتتناك",
                "عيل متناك",
                "كسم الروم",
                "كسمين امك",
                "خخخ",
                "يبن المتناكه",
                "المتناكه امك",
                "هنيك المتناكه امك",
                "شوية خولات",
                "شويه خولات",
                "ي خول",
                "وانيكك",
                "دين",
                "دينك",
                "دين امك",
                "ينعل",
                "ينعن",
                "ينعل ديكك",
                "هركب كسمك",
                "احا",
                "هفشخك",
                "عرص",
                "امك حلوه",
                "امك جامده",
                "يحكاك",
                "يشرموط",
                "يابن الشرموطه",
                "يبن الشرموطه",
                "طيزك",
                "كسمين",
                "هتتناك",
                "هفشخ كسمك",
                "زبي",
                "تعالي مص",
                "تعالي مصمص",
                "دانت قد بتاعي",
            ]
            for v in fsharlist:
                if v in m.text:
                    try:
                        check = await get_available_bot(c, m)
                        if check[2] == "deleteFalse":
                            return
                        await m.delete()
                        return
                    except Exception as e:
                        print("delete messagey " + str(e))

    if lock_fshar_test_ban(m) and not constractors(m):
        if m.text:
            fsharlist = [
                "طيزك",
                "بورن",
                "افلام سكس",
                "طيز اختك",
                "كسمك",
                "كسك",
                "يابن الاحبه",
                "عيل كس",
                "امك",
                "شوف امك",
                "متناك",
                "بتتناك",
                "عيل متناك",
                "كسم الروم",
                "كسمين امك",
                "خخخ",
                "يبن المتناكه",
                "المتناكه امك",
                "هنيك المتناكه امك",
                "شوية خولات",
                "شويه خولات",
                "ي خول",
                "وانيكك",
                "دين",
                "دينك",
                "دين امك",
                "ينعل",
                "ينعن",
                "ينعل ديكك",
                "هركب كسمك",
                "احا",
                "هفشخك",
                "عرص",
                "امك حلوه",
                "امك جامده",
                "يحكاك",
                "يشرموط",
                "يابن الشرموطه",
                "يبن الشرموطه",
                "طيزك",
                "كسمين",
                "هتتناك",
                "هفشخ كسمك",
                "زبي",
                "تعالي مص",
                "تعالي مصمص",
                "دانت قد بتاعي",
            ]
            for v in fsharlist:
                if v in m.text:
                    try:
                        check = await get_available_bot(c, m)
                        if check[2] == "deleteFalse":
                            return
                        await m.delete()
                        await c.ban_chat_member(m.chat.id, m.from_user.id)
                        await m.reply_text(f"◍ تم حظر [{m.from_user.first_name}](tg://user?id={m.from_user.id}"
                                           f") بسبب كلماته السافله\n√",
                                           parse_mode=enums.ParseMode.MARKDOWN)
                        return
                    except Exception as e:
                        print("delete messagey " + str(e))
            
    if lock_fshar_test_mute(m) and not constractors(m):
        if m.text:
            fsharlist = [
                "طيزك",
                "بورن",
                "افلام سكس",
                "طيز اختك",
                "كسمك",
                "كسك",
                "يابن الاحبه",
                "عيل كس",
                "امك",
                "شوف امك",
                "متناك",
                "بتتناك",
                "عيل متناك",
                "كسم الروم",
                "كسمين امك",
                "خخخ",
                "يبن المتناكه",
                "المتناكه امك",
                "هنيك المتناكه امك",
                "شوية خولات",
                "شويه خولات",
                "ي خول",
                "وانيكك",
                "دين",
                "دينك",
                "دين امك",
                "ينعل",
                "ينعن",
                "ينعل ديكك",
                "هركب كسمك",
                "احا",
                "هفشخك",
                "عرص",
                "امك حلوه",
                "امك جامده",
                "يحكاك",
                "يشرموط",
                "يابن الشرموطه",
                "يبن الشرموطه",
                "طيزك",
                "كسمين",
                "هتتناك",
                "هفشخ كسمك",
                "زبي",
                "تعالي مص",
                "تعالي مصمص",
                "دانت قد بتاعي",
            ]
            for v in fsharlist:
                if v in m.text:
                    try:
                        check = await get_available_bot(c, m)
                        if check[2] == "deleteFalse":
                            return
                        await m.delete()
                    except Exception as e:
                        print("delete messagey " + str(e))
            await c.restrict_chat_member(m.chat.id,
                                         m.from_user.id,
                                         ChatPermissions())
            await m.reply_text(f"◍ تم كتم [{m.from_user.first_name}](tg://user?id={m.from_user.id}"
                               f") بسبب كلماته السافله\n√", parse_mode=enums.ParseMode.MARKDOWN)
            return

    if lock_notification_test(m):
        if m.new_chat_members or m.left_chat_member:
            try:
                check = await get_available_bot(c, m)
                if check[2] == "deleteFalse":
                    return
                await m.delete()
                return
            except Exception as e:
                print("delete messagey " + str(e))

########################################################################################################################
########################################################################################################################

    if m.left_chat_member:
        if m.left_chat_member.id == get_bot_information()[0]:
            del_db_checkgroup(m.chat.id)
            del_db_managerall(m.chat.id)
            del_db_constractorsall(m.chat.id)
            del_db_adminall(m.chat.id)
            del_db_specialall(m.chat.id)
            await send_information_groups_kick(c, m)
            return
        if lock_lockbye_test(m):
            try:
                if get_db_addbyegroup(m.chat.id) is None:
                    t = f"""
✧خرجت ليه من عـلـمـنـا الـمـتـواضـ؏ 😢✨

✧اسـمـڪ ي قـمـࢪ {m.left_chat_member.mention} 🌚✨

✧حد مزعلك ي قـمـࢪ 🌚💕

✧لينڪ الجࢪوب ميتوهش ابقي اࢪجع😅💕
                         """
                    await m.reply_text(t)
                    m.text = "del"
                    await MessagesAntiFlood(c, m)
                else:
                    for per in get_db_addbyegroup(m.chat.id):
                        if per[1] == m.chat.id:
                            a = re.sub("#id", str(m.from_user.id), per[0])
                            a = re.sub("#name", str(m.from_user.first_name), a)
                            try:
                                a = re.sub("#user", str(m.from_user.username), a)
                            except Exception as e:
                                print(e)
                                a = re.sub("#user", "لا يوجد", a)
                            await m.reply_text(a, parse_mode=enums.ParseMode.MARKDOWN)
                            return
                    t = f"""
✧خرجت ليه من عـلـمـنـا الـمـتـواضـ؏ 😢✨

✧اسـمـڪ ي قـمـࢪ {m.left_chat_member.mention} 🌚✨

✧حد مزعلك ي قـمـࢪ 🌚💕

✧لينڪ الجࢪوب ميتوهش ابقي اࢪجع😅💕
                                        """
                    await m.reply_text(t)
                    m.text = "del"
                    await MessagesAntiFlood(c, m)
            except Exception as e:
                print("left_chat_member " + str(e))


########################################################################################################################
########################################################################################################################

    if m.text == "حظر عام" and m.reply_to_message:
        if secsudo(m):
            await gbanrep(c, m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if re.match("^حظر عام @(.*)$", str(m.text)):
        if secsudo(m):
            await gbanuser(c, m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return
    if re.match("^حظر عام (\\d+)$", str(m.text)):
        if secsudo(m):
            await gbanuser(c, m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "كتم عام" and m.reply_to_message:
        if secsudo(m):
            await gmuterep(c, m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if re.match("^كتم عام @(.*)$", str(m.text)):
        if secsudo(m):
            await gmuteuser(c, m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return
    if re.match("^كتم عام (\\d+)$", str(m.text)):
        if secsudo(m):
            await gmuteuser(c, m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "الغاء العام" and m.reply_to_message:
        if secsudo(m):
            await gunbanrep(c, m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if re.match("^الغاء العام @(.*)$", str(m.text)):
        if secsudo(m):
            await gunbanuser(c, m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return
    if re.match("^الغاء العام (\\d+)$", str(m.text)):
        if secsudo(m):
            await gunbanuser(c, m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "المحظورين عام":
        if sudo2(m):
            lang = get_db_gban()
            if lang is None:
                await m.reply_text("◍ لايوجد محظورين عام\n√")
            else:
                t = "\n◍ قائمة المحظورين عام \n≪━━━━━━━━━━━━━≫\n"
                for row in lang:
                    if '-' in row:
                        user_id, firstname = row.split("-")
                        t = t + f"[{firstname}](tg://user?id={user_id})\n"
                await m.reply_text(t, parse_mode=enums.ParseMode.MARKDOWN)
            return
        else:
            await m.reply_text("◍ انت لست المطور\n√")
            return

    if m.text == "حذف المحظورين عام":
        if secsudo(m):
            del_db_gbanall()
            await m.reply_text("◍ تم حذف المحظورين عام\n√")
            return
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "المكتومين عام":
        if sudo2(m):
            lang = get_db_gmute()
            if lang is None:
                await m.reply_text("◍ لا يوجد مكتومين عام\n√")
            else:
                t = "\n◍ قائمة الكتم العام \n≪━━━━━━━━━━━━━≫\n"
                for row in lang:
                    t = t + f"[{row[1]}](tg://user?id={row[0]})\n"
                await m.reply_text(t, parse_mode=enums.ParseMode.MARKDOWN)
            return
        else:
            await m.reply_text("◍ انت لست المطور\n√")
            return

    if m.text == "حذف المكتومين عام":
        if secsudo(m):
            del_db_gmuteall()
            await m.reply_text("◍ تم حذف المكتومين عام\n√")
            return
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "اضف رد عام":
        if secsudo(m):
            await addgeneralrep(m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "حذف رد عام":
        if secsudo(m):
            await delgeneralrep(m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "الردود العامه":
        if sudo2(m):
            lang = get_db_greply()
            if lang is None:
                await m.reply_text("◍ لا توجد ردود عامه")
            else:
                t = "\n◍ قائمة الردود العامه \n≪━━━━━━━━━━━━━≫\n"
                for row in lang:
                    t = t + f"({row[0]})--->({row[1]})\n"
                await m.reply_text(t)
            return
        else:
            await m.reply_text("◍ انت لست المطور\n√")
            return

    if m.text == "حذف الردود العامه":
        if secsudo(m):
            del_db_grepall()
            await m.reply_text("◍ تم حذف الردود العامه\n√")
            return
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

########################################################################################################################
########################################################################################################################

    if m.text == "رفع مطور" and m.reply_to_message:
        if secsudo(m):
            await developersrep(m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return
    if re.match("^رفع مطور @(.*)$", str(m.text)) or re.match("^رفع مطور (\\d+)$", str(m.text)):
        if secsudo(m):
            await developersuser(c, m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "تنزيل مطور" and m.reply_to_message:
        if secsudo(m):
            await undevelopersrep(m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return
    if re.match("^تنزيل مطور @(.*)$", str(m.text)) or re.match("^تنزيل مطور (\\d+)$", str(m.text)):
        if secsudo(m):
            await undeveloperuser(c, m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "المطورين":
        if sudo2(m):
            try:
                lang = get_db_general_rtb("developer")
                n = await c.get_users(sudoers[0])
                if lang is None:
                    await m.reply_text(f"◍ [．ᥲ ᥣ ρ ᥆ ρ ¹𖥻 ．](tg://user?id={super_sudoers[0]})\n" +
                                       f"◍ [{n.first_name}](tg://user?id={sudoers[0]})\n\n"
                                       "لا يوجد مطورين مرفوعين\n√",
                                       parse_mode=enums.ParseMode.MARKDOWN)
                else:
                    t = "\n◍ قائمة المطورين \n≪━━━━━━━━━━━━━≫\n" + f"◍ [．ᥲ ᥣ ρ ᥆ ρ ¹𖥻 ．](tg://user?id={super_sudoers[0]})\n" + \
                        f"◍ [{n.first_name}](tg://user?id={sudoers[0]})\n\n√"
                    for row in lang:
                        t = t + f"[{row[1]}](tg://user?id={row[0]})\n"
                    await m.reply_text(t, parse_mode=enums.ParseMode.MARKDOWN)
            except Exception as e:
                print("developer " + str(e))

        else:
            await m.reply_text("◍ انت لست المطور\n√")
            return

    if m.text == "حذف المطورين":
        if secsudo(m):
            del_db_general_rtball("developer")
            developer.clear()
            await m.reply_text("◍ تم حذف المطورين\n√")
            return
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "رفع مطور ثانوي" and m.reply_to_message:
        if sudo(m):
            await seconddevelopersrep(m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return
    if re.match("^رفع مطور ثانوي @(.*)$", str(m.text)) or re.match("^رفع مطور ثانوي (\\d+)$", str(m.text)):
        if sudo(m):
            await seconddevelopersuser(c, m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "تنزيل مطور ثانوي" and m.reply_to_message:
        if sudo(m):
            await secondundevelopersrep(m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return
    if re.match("^تنزيل مطور ثانوي @(.*)$", str(m.text)) or re.match("^تنزيل مطور ثانوي (\\d+)$", str(m.text)):
        if sudo(m):
            await secondundeveloperuser(c, m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "المطورين الثانويين" or m.text == "المطورين الثانوين":
        if sudo2(m):
            try:
                lang = get_db_general_rtb("secdeveloper")
                n = await c.get_users(sudoers[0])
                if lang is None:
                    await m.reply_text(f"◍ [．ᥲ ᥣ ρ ᥆ ρ ¹𖥻 ．](tg://user?id={super_sudoers[0]})\n" +
                                       f"◍ [{n.first_name}](tg://user?id={sudoers[0]})\n"
                                       "لا يوجد مطورين ثانويين مرفوعين\n√",
                                       parse_mode=enums.ParseMode.MARKDOWN)
                else:
                    t = "\n◍ قائمة المطورين الثانويين \n≪━━━━━━━━━━━━━≫\n" + f"◍ [．ᥲ ᥣ ρ ᥆ ρ ¹𖥻 ．](tg://user?id={super_sudoers[0]})\n" + f"◍ [{n.first_name}](tg://user?id={sudoers[0]})\n\n√"
                    for row in lang:
                        t = t + f"[{row[1]}](tg://user?id={row[0]})\n"
                    await m.reply_text(t, parse_mode=enums.ParseMode.MARKDOWN)
            except Exception as e:
                print("second developer " + str(e))

        else:
            await m.reply_text("◍ انت لست المطور\n√")
            return

    if m.text == "حذف المطورين الثانويين" or m.text == "حذف المطورين الثانوين" or m.text == "حذف الثانوين":
        if sudo(m):
            del_db_general_rtball("secdeveloper")
            developer.clear()
            await m.reply_text("◍ تم حذف المطورين الثانويين\n√")
            return
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "رفع مميز عام" and m.reply_to_message:
        if secsudo(m):
            await genspecialrep(m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return
    if re.match("^رفع مميز عام @(.*)$", str(m.text)) or re.match("^رفع مميز عام (\\d+)$", str(m.text)):
        if secsudo(m):
            await genspecialuser(c, m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "تنزيل مميز عام" and m.reply_to_message:
        if secsudo(m):
            await ungenspecialrep(m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return
    if re.match("^تنزيل مميز عام @(.*)$", str(m.text)) or re.match("^تنزيل مميز عام (\\d+)$", str(m.text)):
        if secsudo(m):
            await ungenspecialuser(c, m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "المميزين عام":
        if sudo2(m):
            lang = get_db_general_rtb("genspecial")
            if lang is None:
                await m.reply_text("◍ لا يوجد مميزين عام مرفوعين\n√", parse_mode=enums.ParseMode.MARKDOWN)
            else:
                t = "\n◍ قائمة المميزين عام \n≪━━━━━━━━━━━━━≫\n"
                for row in lang:
                    t = t + f"[{row[1]}](tg://user?id={row[0]})\n"
                await m.reply_text(t, parse_mode=enums.ParseMode.MARKDOWN)
                return
        else:
            await m.reply_text("◍ انت لست المطور\n√")
            return

    if m.text == "حذف المميزين عام":
        if secsudo(m):
            del_db_general_rtball("genspecial")
            await m.reply_text("◍ تم حذف المميزين عام\n√")
            return
        else:
            await m.reply_text("◍ انت لست المميزين عام\n√")
            return

########################################################################################################################
########################################################################################################################

    if m.text == "رفع مالك" and m.reply_to_message:
        if sudo2(m):
            await managerrep(m)
            return
        else:
            await m.reply_text("◍ انت لست المطور\n√")
            return
    if re.match("^رفع مالك @(.*)$", str(m.text)) or re.match("^رفع مالك (\\d+)$", str(m.text)):
        if sudo2(m):
            await manageruser(c, m)
            return
        else:
            await m.reply_text("◍ انت لست المطور\n√")
            return

    if m.text == "تنزيل مالك" and m.reply_to_message:
        if sudo2(m):
            await undmanagersrep(m)
            return
        else:
            await m.reply_text("◍ انت لست المطور\n√")
            return

    if re.match("^تنزيل مالك @(.*)$", str(m.text)) or re.match("^تنزيل مالك (\\d+)$", str(m.text)):
        if sudo2(m):
            await undmanagersuser(c, m)
            return
        else:
            await m.reply_text("◍ انت لست المطور\n√")
            return

    if m.text == "المالكين" or m.text == "المالك" or m.text == "المنشئ":
        lang = get_db_manager(m.chat.id)
        if lang is None:
            await m.reply_text("◍ لا يوجد مالكين\n√")
        else:
            t = "\n◍ قائمة المالكين \n≪━━━━━━━━━━━━━≫\n"
            for row in lang:
                t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
            await m.reply_text(t, parse_mode=enums.ParseMode.MARKDOWN)
        return

    if m.text == "حذف المالكين":
        if sudo2(m):
            del_db_managerall(m.chat.id)
            await m.reply_text("◍ تم حذف المالكين\n√")
            return
        else:
            await m.reply_text("◍ انت لست المطور\n√")
            return

    if m.text == "رفع مشرف" and m.reply_to_message:
        if manager(m):
            await addadmingrouprep(c, m)
        else:
            await m.reply_text("◍ يجب ان تكون مالك حتى تستطيع رفع مشرف\n√")
            return

    if re.match("^رفع مشرف @(.*)$", str(m.text)) or re.match("^رفع مشرف (\\d+)$", str(m.text)):
        if manager(m):
            await addadmingroupuser(c, m)
        else:
            await m.reply_text("◍ يجب ان تكون مالك حتى تستطيع رفع مشرف\n√")
            return

    if m.text == "تنزيل مشرف" and m.reply_to_message:
        if manager(m):
            await unadmingroiprep(c, m)
        else:
            await m.reply_text("◍ يجب ان تكون مالك حتى تستطيع تنزيل مشرف\n√")
            return

    if re.match("^تنزيل مشرف @(.*)$", str(m.text)) or re.match("^تنزيل مشرف (\\d+)$", str(m.text)):
        if manager(m):
            await unadmingroipuser(c, m)
        else:
            await m.reply_text("◍ يجب ان تكون مالك حتى تستطيع رفع مشرف\n√")
            return

    if m.text == "رفع منشئ" and m.reply_to_message:
        if manager(m):
            await addconstractorrep(m)
        else:
            await m.reply_text("◍ يجب ان تكون مالك حتى تستطيع رفع منشئ\n√")
            return

    if re.match("^رفع منشئ @(.*)$", str(m.text)) or re.match("^رفع منشئ (\\d+)$", str(m.text)):
        if manager(m):
            await addconstractoruser(c, m)
        else:
            await m.reply_text("◍ يجب ان تكون مالك حتى تستطيع رفع منشئ\n√")
            return

    if m.text == "تنزيل منشئ" and m.reply_to_message:
        if manager(m):
            await unconstractorrep(m)
        else:
            await m.reply_text("◍ يجب ان تكون مالك حتى تستطيع تنزيل منشئ\n√")
            return

    if re.match("^تنزيل منشئ @(.*)$", str(m.text)) or re.match("^تنزيل منشئ (\\d+)$", str(m.text)):
        if manager(m):
            await unconstractoruser(c, m)
        else:
            await m.reply_text("◍ يجب ان تكون مالك حتى تستطيع رفع منشئ\n√")
            return

    if m.text == "المنشئين":
        lang = get_db_constractors(m.chat.id)
        if lang is None:
            await m.reply_text("◍ لا يوجد منشئين\n√")
        else:
            t = "\n◍ قائمة المنشئين \n≪━━━━━━━━━━━━━≫\n"
            for row in lang:
                t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
            await m.reply_text(t, parse_mode=enums.ParseMode.MARKDOWN)
        return

    if m.text == "حذف المنشئين":
        if manager(m):
            del_db_constractorsall(m.chat.id)
            await m.reply_text("◍ تم حذف المنشئين\n√")
            return
        else:
            await m.reply_text("◍ يجب ان تكون مالك حتى تستطيع حذف المنشئين\n√")
            return

    if m.text == "رفع ادمن" and m.reply_to_message:
        if constractors(m):
            await addadminrep(m)
        else:
            await m.reply_text("◍ يجب ان تكون منشئ على الاقل لكى تستطيع رفع ادمن\n√")
            return

    if re.match("^رفع ادمن @(.*)$", str(m.text)) or re.match("^رفع ادمن (\\d+)$", str(m.text)):
        if constractors(m):
            await addadminuser(c, m)
        else:
            await m.reply_text("◍ يجب ان تكون منشئ على الاقل لكى تستطيع رفع ادمن\n√")
            return

    if m.text == "تنزيل ادمن" and m.reply_to_message:
        if constractors(m):
            await unadminrep(m)
        else:
            await m.reply_text("◍ يجب ان تكون منشئ على الاقل لكى تستطيع تنزيل ادمن\n√")
            return

    if re.match("^تنزيل ادمن @(.*)$", str(m.text)) or re.match("^تنزيل ادمن (\\d+)$", str(m.text)):
        if constractors(m):
            await unadminuser(c, m)
        else:
            await m.reply_text("◍ يجب ان تكون منشئ على الاقل لكى تستطيع تنزيل ادمن\n√")
            return

    if m.text == "الادمنيه":
        lang = get_db_admin(m.chat.id)
        if lang is None:
            await m.reply_text("◍ لا يوجد ادمنيه\n√")
        else:
            t = "\n◍ قائمة الادمنيه \n≪━━━━━━━━━━━━━≫\n"
            for row in lang:
                t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
            await m.reply_text(t, parse_mode=enums.ParseMode.MARKDOWN)
        return

    if m.text == "حذف الادمنيه":
        if constractors(m):
            del_db_adminall(m.chat.id)
            await m.reply_text("◍ تم حذف الادمنيه\n√")
            return
        else:
            await m.reply_text("◍ يجب ان تكون منشئ على الاقل لكى تستطيع تنزيل ادمن\n√")
            return

    if m.text == "رفع مميز" and m.reply_to_message:
        if admin(m):
            await addspecialrep(m)
        else:
            await m.reply_text("◍ يجب ان تكون ادمن على الاقل لكى تستطيع رفع مميز\n√")
            return

    if re.match("^رفع مميز @(.*)$", str(m.text)) or re.match("^رفع مميز (\\d+)$", str(m.text)):
        if admin(m):
            await addspecialuser(c, m)
        else:
            await m.reply_text("◍ يجب ان تكون ادمن على الاقل لكى تستطيع رفع مميز\n√")
            return

    if m.text == "تنزيل مميز" and m.reply_to_message:
        if admin(m):
            await unspecialrep(m)
        else:
            await m.reply_text("◍ يجب ان تكون ادمن على الاقل لكى تستطيع تنزيل مميز\n√")
            return

    if re.match("^تنزيل مميز @(.*)$", str(m.text)) or re.match("^تنزيل مميز (\\d+)$", str(m.text)):
        if admin(m):
            await unspecialuser(c, m)
        else:
            await m.reply_text("◍ يجب ان تكون ادمن على الاقل لكى تستطيع تنزيل مميز\n√")
            return

    if m.text == "المميزين":
        lang = get_db_special(m.chat.id)
        if lang is None:
            await m.reply_text("◍ لا يوجد مميزين\n√")
        else:
            t = "\n◍ قائمة المميزين \n≪━━━━━━━━━━━━━≫\n"
            for row in lang:
                t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
            await m.reply_text(t, parse_mode=enums.ParseMode.MARKDOWN)
        return

    if m.text == "حذف المميزين":
        if admin(m):
            del_db_specialall(m.chat.id)
            await m.reply_text("◍ تم حذف المميزين\n√")
            return
        else:
            await m.reply_text("◍ يجب ان تكون ادمن على الاقل لكى تستطيع حذف المميزين\n√")
            return

########################################################################################################################
########################################################################################################################

    if m.text == "حظر" or m.text == "ban" or m.text == "Ban" or m.text == "/ban" and m.reply_to_message:
        if admin(m):
            await banrep(c, m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع حظر العضو\n√")
            return
    if re.match("^حظر @(.*)$", str(m.text)) or re.match("^حظر (\\d+)$", str(m.text)):
        if admin(m):
            await banuser(c, m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع حظر العضو\n√")
            return

    if m.text == "الغاء حظر" or m.text =="الغاء الحظر" or m.text == "unban" or m.text == "Unban" or m.text == "/unban" and m.reply_to_message:
        if admin(m):
            await unbanrep(c, m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع الغاء حظر العضو\n√")
            return
    if re.match("^الغاء حظر @(.*)$", str(m.text)) or re.match("^الغاء حظر (\\d+)$", str(m.text)):
        if admin(m):
            await unbanuser(c, m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع الغاء حظر العضو\n√")
            return

    if m.text == "المحظورين":
        if special(m):
            lang = get_db_ban(m.chat.id)
            if lang is None:
                await m.reply_text("لا يوجد محظورين\n√", parse_mode=enums.ParseMode.MARKDOWN)
            else:
                t = "\n◍ قائمة المحظورين \n≪━━━━━━━━━━━━━≫\n"
                for row in lang:
                    t = t + f"[{row[1]}](tg://user?id={row[0]})\n"
                await m.reply_text(t, parse_mode=enums.ParseMode.MARKDOWN)
            return
        else:
            await m.reply_text("◍ تحتاج الى اى رتبه لاستخدام هذا الامر\n√")
            return

    if m.text == "حذف المحظورين" or m.text == "مسح المحظورين":
        if constractors(m):
            if get_db_ban(m.chat.id) is None:
                await m.reply_text("◍ لايوجد محظورين\n√")
                return
            for row in get_db_ban(m.chat.id):
                try:
                    await m.chat.unban_member(row[0])
                except Exception as e:
                    print("delete all ban" + str(e))
                    continue
            del_db_banall(m.chat.id)
            await m.reply_text("◍ تم حذف المحظورين\n√")
            return
        else:
            await m.reply_text("◍ يجب ان تكون منشئ لاستخدام هذا الامر\n√")
            return

    if m.text == "كتم" or m.text == "mute" or m.text == "Mute" or m.text == "/mute" and m.reply_to_message:
        if admin(m):
            await muterep(c, m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع كتم العضو\n√")
            return
    if re.match("^كتم @(.*)$", str(m.text)) or re.match("^كتم (\\d+)$", str(m.text)):
        if admin(m):
            await muteuser(c, m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع كتم العضو\n√")
            return

    if m.text == "الغاء كتم" or m.text == "unmute" or m.text == "Unmute" or m.text == "/unmute" and m.reply_to_message:
        if admin(m):
            await unmuterep(c, m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع الغاء كتم العضو\n√")
            return
    if re.match("^الغاء كتم @(.*)$", str(m.text)) or re.match("^الغاء كتم (\\d+)$", str(m.text)):
        if admin(m):
            await unmuteuser(c, m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع الغاء كتم العضو\n√")
            return

    if m.text == "المكتومين":
        if special(m):
            lang = get_db_mute(m.chat.id)
            if lang is None:
                await m.reply_text("لا يوجد مكتومين\n√", parse_mode=enums.ParseMode.MARKDOWN)
            else:
                t = "\n◍ قائمة المكتومين \n≪━━━━━━━━━━━━━≫\n"
                for row in lang:
                    t = t + f"[{row[1]}](tg://user?id={row[0]})\n"
                await m.reply_text(t, parse_mode=enums.ParseMode.MARKDOWN)
            return
        else:
            await m.reply_text("◍ تحتاج الى اى رتبه لاستخدام هذا الامر\n√")
            return

    if m.text == "حذف المكتومين" or m.text == "مسح المكتومين":
        if constractors(m):
            if get_db_mute(m.chat.id) is None:
                await m.reply_text("◍ لا يوجد لمكتومين\n√")
                return
            for row in get_db_mute(m.chat.id):
                try:
                    await m.chat.unban_member(row[0])
                except Exception as e:
                    print("delete all mute" + str(e))
                    continue
            del_db_muteall(m.chat.id)
            await m.reply_text("◍ تم حذف المكتومين\n√")
            return
        else:
            await m.reply_text("◍ يجب ان تكون منشئ لاستخدام هذا الامر\n√")
            return

    if re.match("^حظر لمده (.*)$", str(m.text)) and m.reply_to_message:
        if admin(m):
            await tban(c, m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع حظر العضو\n√")
            return

    if re.match("^كتم لمده (.*)$", str(m.text)) and m.reply_to_message:
        if admin(m):
            await tmute(c, m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع كتم العضو\n√")
            return

    if m.text == "طرد" and m.reply_to_message:
        if admin(m):
            await kickrep(c, m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع طرد العضو")
            return
    if re.match("^طرد @(.*)$", str(m.text)) or re.match("^طرد (\\d+)$", str(m.text)):
        if admin(m):
            await kickuser(c, m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع طرد العضو")
            return

    if m.text == "تثبيت" and not m.reply_to_message:
        if admin(m):
            await m.reply_text("◍ من فضلك قم بعمل ريبلاى على الماسج المراد تثبيتها...")
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع تثبيت رساله")

    if m.text == "تثبيت" and m.reply_to_message:
        if admin(m):
            await pin(c, m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع تثبيت رساله")
            return
    if m.text == "تثبيت بدون اشعار" and m.reply_to_message:
        if admin(m):
            await pinloud(c, m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع تثبيت رساله")
            return

    if m.text == "الغاء تثبيت" and m.reply_to_message:
        if admin(m):
            await unpin(c, m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع الغاء تثبيت الرساله")
            return
    if m.text == "الغاء تثبيت الكل" and m.reply_to_message:
        if admin(m):
            await unpinall(c, m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع الغاء تثبيت الرسائل")
            return

    if m.text == "تطهير":
        if admin(m):
            await purge(c, m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع تطهير الرسائل")
            return

########################################################################################################################
########################################################################################################################

    if m.text == "فتح الدردشه":
        if constractors(m):
            await lock_chat_open(m)
        else:
            await m.reply_text("◍ هذا الامر لرتبه منشئ فما فوق")
            return

    if m.text == "قفل الدردشه":
        if constractors(m):
            check = await get_available_bot(c, m)
            if check[2] == "deleteFalse":
                await m.reply_text("◍ ليس لدي صلاحيه قفل الدردشه فى الجروب\n√")
                return
            await lock_chat_close(m)
        else:
            await m.reply_text("◍ هذا الامر لرتبه منشئ فما فوق")
            return

    if m.text == "فتح المعرفات":
        if admin(m):
            await lock_mnshn_open(m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع فتح المنشن")
            return

    if m.text == "قفل المعرفات":
        if admin(m):
            await lock_mnshn_close(m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع قفل المنشن")
            return

    if m.text == "فتح الروابط":
        if admin(m):
            await lock_link_open(m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع فتح الروابط")
            return

    if m.text == "قفل الروابط":
        if admin(m):
            await lock_link_close(m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع قفل الروابط")
            return

    if m.text == "فتح الصور":
        if admin(m):
            await lock_photo_open(m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع فتح الصور")
            return

    if m.text == "قفل الصور":
        if admin(m):
            await lock_photo_close(m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع قفل الصور")
            return

    if m.text == "فتح الفديوهات" or m.text == "فتح الفيديوهات":
        if admin(m):
            await lock_video_open(m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع فتح الفديوهات")
            return

    if m.text == "قفل الفديوهات" or m.text == "قفل الفيديوهات":
        if admin(m):
            await lock_video_close(m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع قفل الفديوهات")
            return

    if m.text == "فتح الاستيكر" or m.text == "فتح الملصقات":
        if admin(m):
            await lock_sticker_open(m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع فتح الاستيكرات")
            return

    if m.text == "قفل الاستيكر" or m.text == "قفل الملصقات":
        if admin(m):
            await lock_sticker_close(m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع قفل الاستيكرات")
            return

    if m.text == "فتح المتحركه":
        if admin(m):
            await lock_animation_open(m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع فتح المتحركه")
            return

    if m.text == "قفل المتحركه":
        if admin(m):
            await lock_animation_close(m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع قفل المتحركه")
            return

    if m.text == "فتح الريكورد" or m.text == "فتح الريك":
        if admin(m):
            await lock_voice_open(m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع فتح الريكورد")
            return

    if m.text == "قفل الريكورد" or m.text == "قفل الريك":
        if admin(m):
            await lock_voice_close(m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع قفل الريكورد")
            return

    if m.text == "فتح الصوت":
        if admin(m):
            await lock_audio_open(m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع فتح الريكورد")
            return

    if m.text == "قفل الصوت":
        if admin(m):
            await lock_audio_close(m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع قفل الريكورد")
            return

    if m.text == "فتح التوجيه":
        if constractors(m):
            await lock_forward_open(m)
        else:
            await m.reply_text("◍ هذا الامر لرتبه منشئ او اعلى")
            return

    if m.text == "قفل التوجيه":
        if constractors(m):
            await lock_forward_close(m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع قفل التوجيه")
            return

    if m.text == "فتح الملفات":
        if admin(m):
            await lock_document_open(m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع فتح الملفات")
            return

    if m.text == "قفل الملفات":
        if admin(m):
            await lock_document_close(m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع قفل الملفات")
            return

    if m.text == "فتح الجهات":
        if admin(m):
            await lock_contact_open(m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع فتح الجهات")
            return

    if m.text == "قفل الجهات":
        if admin(m):
            await lock_contact_close(m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع قفل الجهات")
            return

    if m.text == "فتح الفشار":
        if admin(m):
            await lock_fshar_open(m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه ادمن على الاقل لكى تستطيع فتح الفشار")
            return

    if m.text == "قفل الفشار":
        if admin(m):
            await lock_fshar_close(m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه ادمن على الاقل لكى تستطيع قفل الفشار")
            return

    if re.match("^منع (.*)$", str(m.text)):
        if constractors(m):
            if get_db_blocktext(m.chat.id) is None:
                set_db_blocktext(m.text[4:], m.chat.id)
                await m.reply_text("◍ تم منع الكلمه بنجاح\n√")
                return
            else:
                for cons in get_db_blocktext(m.chat.id):
                    if m.text[4:] == cons[0]:
                        await m.reply_text("◍ الكلمه ممنوعه بالفعل\n√")
                        return
                set_db_blocktext(m.text[4:], m.chat.id)
                await m.reply_text("◍ تم منع الكلمه بنجاح\n√")
        else:
            await m.reply_text("◍ يجب ان تكون منشئ لاستخدام هذا الامر\n√")
            return

    if re.match("^الغاء منع (.*)$", str(m.text)):
        if constractors(m):
            if get_db_blocktext(m.chat.id) is None:
                await m.reply_text("◍ الكلمه غير ممنوعه اصلا\n√")
                return
            else:
                for dv in get_db_blocktext(m.chat.id):
                    if m.text[10:] == dv[0]:
                        del_db_blocktext(m.text[10:], m.chat.id)
                        await m.reply_text("◍ تم الغاء منع الكلمه بنجاح\n√")
                        return
                await m.reply_text("◍ الكلمه غير ممنوعه اصلا\n√")
        else:
            await m.reply_text("◍ يجب ان تكون منشئ لاستخدام هذا الامر\n√")
            return

    if m.text == "الكلمات الممنوعه":
        lang = get_db_blocktext(m.chat.id)
        if lang is None:
            await m.reply_text("◍ لا توجد كلمات ممنوعه\n√")
        else:
            t = "\n◍ قائمة الكلمات الممنوعه \n≪━━━━━━━━━━━━━≫\n"
            for row in lang:
                t = t + f"{row[0]}\n"
            await m.reply_text(t, parse_mode=enums.ParseMode.MARKDOWN)
        return

    if m.text == "حذف الكلمات الممنوعه" or m.text == "مسح الكلمات الممنوعه":
        if constractors(m):
            del_db_blocktextall(m.chat.id)
            await m.reply_text("◍ تم حذف الكلمات الممنوعه\n√")
            return
        else:
            await m.reply_text("◍ يجب ان تكون منشئ لاستخدام هذا الامر\n√")
            return

    if m.text == "اضف رد":
        if constractors(m):
            set_db_wait("addreplygroup", m.from_user.id, m.chat.id)
            await m.reply_text("◍ ارسل لى الكلمه الان\n√")
        else:
            await m.reply_text("◍ هذا الامر لرتبه المنشئ والمالك فقط\n√")
            return

    if m.text == "حذف رد":
        if constractors(m):
            set_db_wait("delreplygroup", m.from_user.id, m.chat.id)
            await m.reply_text("◍ ارسل لى الكلمه التى ترغب فى حذفها\n√")
        else:
            await m.reply_text("◍ هذا الامر لرتبه المنشئ والمالك فقط\n√")
            return

    if m.text == "الردود":
        if constractors(m):
            lang = get_db_replygroup(m.chat.id)
            if lang is None:
                await m.reply_text("◍ لا توجد ردود")
            else:
                t = "\n◍ قائمة الردود\n≪━━━━━━━━━━━━━≫\n"
                for row in lang:
                    t = t + f"({row[0]})--->({row[1]})\n"
                await m.reply_text(t)
            return
        else:
            await m.reply_text("◍ هذا الامر لرتبه المنشئ والمالك فقط\n√")
            return

    if m.text == "حذف الردود":
        if constractors(m):
            del_db_repgroupall(m.chat.id)
            await m.reply_text("◍ تم حذف الردود\n√")
            return
        else:
            await m.reply_text("◍ هذا الامر لرتبه المنشئ والمالك فقط\n√")
            return

    if m.text == "فتح الاشعارات":
        if constractors(m):
            await lock_notification_open(m)
        else:
            await m.reply_text("◍ هذا الامر لرتبه منشئ او اعلى")
            return

    if m.text == "قفل الاشعارات":
        if constractors(m):
            await lock_notification_close(m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع قفل التوجيه")
            return

    if m.text == "الحمايه" or m.text == "الاعدادات":
        if special(m):
            await lock_all_test(m)
        else:
            await m.reply_text("◍ يجب ان تكون مميز على الاقل لاستخدام هذا الامر\n√")
            return

########################################################################################################################
########################################################################################################################

    if m.text == "اذاعه بالمجموعات":
        if secsudo(m):
            set_db_wait("gbroadcast", m.from_user.id, m.chat.id)
            await m.reply_text("◍ ارسل لى الاذاعه الان\n√")
            return
        if sudo2(m):
            if await lock_lockbroadcast_test():
                set_db_wait("gbroadcast", m.from_user.id, m.chat.id)
                await m.reply_text("◍ ارسل لى الاذاعه الان\n√")
                return
            else:
                await m.reply_text("◍ الاذاعه مقفوله من قبل المطور الاساسي\n√")
                return
        else:
            await m.reply_text("◍ هذا الامر للمطورين فقط\n√")
            return

    if m.text == "اذاعه خاص":
        if secsudo(m):
            set_db_wait("ubroadcast", m.from_user.id, m.chat.id)
            await m.reply_text("◍ ارسل لى الاذاعه الان\n√")
            return
        if sudo2(m):
            if await lock_lockbroadcast_test():
                set_db_wait("ubroadcast", m.from_user.id, m.chat.id)
                await m.reply_text("◍ ارسل لى الاذاعه الان\n√")
                return
            else:
                await m.reply_text("◍ الاذاعه مقفوله من قبل المطور الاساسي\n√")
                return
        else:
            await m.reply_text("◍ هذا الامر للمطورين فقط\n√")
            return

    if m.text == "اذاعه بالتوجيه للمجموعات" or m.text == "اذاعه بالتوجيه للجروبات":
        if secsudo(m):
            set_db_wait("gforwardbroadcast", m.from_user.id, m.chat.id)
            await m.reply_text("◍ ارسل لى الاذاعه الان\n√")
            return
        if sudo2(m):
            if await lock_lockbroadcast_test():
                set_db_wait("gforwardbroadcast", m.from_user.id, m.chat.id)
                await m.reply_text("◍ ارسل لى الاذاعه الان\n√")
                return
            else:
                await m.reply_text("◍ الاذاعه مقفوله من قبل المطور الاساسي\n√")
                return
        else:
            await m.reply_text("◍ هذا الامر للمطورين فقط\n√")
            return

    if m.text == "اذاعه بالتوجيه خاص":
        if secsudo(m):
            set_db_wait("uforwardbroadcast", m.from_user.id, m.chat.id)
            await m.reply_text("◍ ارسل لى الاذاعه الان\n√")
            return
        if sudo2(m):
            if await lock_lockbroadcast_test():
                set_db_wait("uforwardbroadcast", m.from_user.id, m.chat.id)
                await m.reply_text("◍ ارسل لى الاذاعه الان\n√")
                return
            else:
                await m.reply_text("◍ الاذاعه مقفوله من قبل المطور الاساسي\n√")
                return
        else:
            await m.reply_text("◍ هذا الامر للمطورين فقط\n√")
            return

    if m.text == "اذاعه بالتثبيت":
        if secsudo(m):
            set_db_wait("gpinbroadcast", m.from_user.id, m.chat.id)
            await m.reply_text("◍ ارسل لى الاذاعه الان\n√")
            return
        if sudo2(m):
            if await lock_lockbroadcast_test():
                set_db_wait("gpinbroadcast", m.from_user.id, m.chat.id)
                await m.reply_text("◍ ارسل لى الاذاعه الان\n√")
                return
            else:
                await m.reply_text("◍ الاذاعه مقفوله من قبل المطور الاساسي\n√")
                return
        else:
            await m.reply_text("◍ هذا الامر للمطورين فقط\n√")
            return

    if m.text == "اذاعه موجهه بالتثبيت":
        if secsudo(m):
            set_db_wait("uforwardpinbroadcast", m.from_user.id, m.chat.id)
            await m.reply_text("◍ ارسل لى الاذاعه الان\n√")
            return
        if sudo2(m):
            if await lock_lockbroadcast_test():
                set_db_wait("uforwardpinbroadcast", m.from_user.id, m.chat.id)
                await m.reply_text("◍ ارسل لى الاذاعه الان\n√")
                return
            else:
                await m.reply_text("◍ الاذاعه مقفوله من قبل المطور الاساسي\n√")
                return
        else:
            await m.reply_text("◍ هذا الامر للمطورين فقط\n√")
            return

    if m.text == "جلب نسخه احتياطيه":
        if secsudo(m):
            await get_backup(c, m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return
           
    if m.text == "جلب نسخه الردود" or m.text == "جلب الردود":
        if secsudo(m):
            await get_backup2(m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "رفع نسخه احتياطيه" and m.reply_to_message:
        if secsudo(m):
            if m.reply_to_message.document:
                await upper_backup(c, m)
            else:
                await m.reply_text("◍ ◍ من فضلك قم باختيار الملف اولا\n√")
                return
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "الاحصائيات":
        if sudo2(m):
            await get_num_for_user_and_group(m)
        else:
            await m.reply_text("◍ انت لست المطور\n√")
            return

########################################################################################################################
########################################################################################################################

    if m.text == "ضع اسم للبوت":
        if secsudo(m):
            await namebot(m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "بوت" or m.text == "البوت":
        if sudo2(m):
            await m.reply_text("◍ نعم حبيبى المطور 🥺❤️\n√")
        else:
            if manager(m):
                await m.reply_text("◍ نعم حبيبي المالك 🥺❤️\n√")
            else:
                if constractors(m):
                    await m.reply_text("◍ نعم حبيبى المنشئ 🥺❤️\n√")
                else:
                    if admin(m):
                        await m.reply_text("◍ نعم حبيبى الادمن 🥺❤️\n√")
                    else:
                        if special(m):
                            await m.reply_text("◍ نعم حبيبى المميز 🥺❤️\n√")
                        else:
                            if get_db_botname() is None:
                                botname = "حور"
                            else:
                                botname = get_db_botname()
                            await m.reply_text("اسمى " + botname + " ياحب 🙄❤️")

    if m.text == (get_db_botname() or "حور"):
        texting = ["اؤمر " + (get_db_botname() or "حور") + " شتريد؟❤️🥺",
                   "اى يقلب " + (get_db_botname() or "حور") + "❤️",
                   "موجود عايز اى بوشك ده😒",
                   "موجود عاوز اى 😒",
                   "مالك حبيبى🥺",
                   "شفلك كلبه❤️😂",
                   "مبكلمكش🥺",
                   "شبيك لبيك❤️😂",
                   "ثانيه واحده بتشقط وجى🙄",
                   "قلبى بينادى على " + (get_db_botname() or "حور") + "😘",
                   "نعسان محدش يصحينى🙄"
                   ]
        await m.reply_text(random.choice(texting))
        return

    if m.text == "بوت غادر" or m.text == (get_db_botname() or "حور") + " غادر":
        if secsudo(m):
            try:
                await m.reply_text("◍ تم المغادره من الجروب حبيبى المطور❤️🥺\n√")
                del_db_checkgroup(m.chat.id)
                del_db_managerall(m.chat.id)
                del_db_constractorsall(m.chat.id)
                del_db_adminall(m.chat.id)
                del_db_specialall(m.chat.id)
                await c.leave_chat(m.chat.id)
            except RPCError as e:
                await m.reply_text(str(e) + "\n\n" +
                                   "فى حاله ظهور لك مثلا هذه الرساله تواصل مع المطور -> "
                                   "[Marcelo](tg://user?id=super_sudoers[0])", parse_mode=enums.ParseMode.MARKDOWN)
                return
        else:
            await m.reply_text("◍ انت لست المطور\n√")
            return


    if m.text == "حساب العمر":
        await omrk(m)

########################################################################################################################
########################################################################################################################

    if m.text == "تاك للاعضاء" or m.text == "تاك" or m.text == \
            "تاج" or m.text == "تاج للاعضاء":
        if manager(m):
            await tagalluser(c, m)
            return
        if not lock_tag_test(m):
            await tagalluser(c, m)
            return
        else:
            await m.reply_text("◍ التاج مقفول اطلب من الادمن فتحه\n√")

    if m.text == "تاك للكل" or m.text == "تاج للكل":
        if manager(m):
            await tagalluserofallgroup(c, m)
            return
        if not lock_tag_test(m):
            await tagalluserofallgroup(c, m)
            return
        else:
            await m.reply_text("◍ التاج مقفول اطلب من المالك فتحه\n√")
    if m.text == "all" or m.text == "@all" or m.text == "#all":
        if manager(m):
            await mentionallgroup(c, m, "\n")
            return
        if not lock_tag_test(m):
            if constractors(m):
                await mentionallgroup(c, m, "\n")
                return
            else:
                await m.reply_text("◍ هذا الامر لرتبه منشئ او اعلى\n√")
                return
        else:
            await m.reply_text("◍ التاج مقفول اطلب من المالك فتحه\n√")
    if re.match("^@all (.*)$", str(m.text)):
        m.text = m.text.split("@all", 1)
        if manager(m):
            await mentionallgroup(c, m, m.text[1] + "\n")
            return
        if not lock_tag_test(m):
            if constractors(m):
                await mentionallgroup(c, m, m.text[1] + "\n")
                return
            else:
                await m.reply_text("◍ هذا الامر لرتبه منشئ او اعلى\n√")
                return
        else:
            await m.reply_text("◍ التاج مقفول اطلب من المالك فتحه\n√")

    if m.text == "stop" or m.text == "الغاء" or m.text == "الغاء المنشن"\
            or m.text == "ايقاف المنشن":
        if constractors(m):
            await stopmentionallgroup(m)
            return

    if m.text == "فتح التاج" or m.text == "فتح التاك":
        if manager(m):
            await lock_tag_open(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه مالك لاستخدام هذا الامر\n√")
            return

    if m.text == "قفل التاج" or m.text == "قفل التاك":
        if manager(m):
            await lock_tag_close(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه مالك لاستخدام هذا الامر\n√")
            return

    if m.text == "تدمير المجموعه":
        if sudo(m):
            await destroy_all_group(c, m)

    if m.text == "السورس" or m.text == "سورس" or m.text == "يا سورس":
        Shadoow = await c.get_users(super_sudoers[1])
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(
                             Shadoow.first_name, user_id=super_sudoers[1]
            )
            ], 
            [ InlineKeyboardButton ( "᥉᥆ᥙᖇᥴᥱ حسنين", url=f"https://t.me/sssess1s" )], 
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅",
                              url=f"https://t.me/{get_bot_information () [1]}?startgroup=new")],
        ])
        await m.reply_text("""
╭──── • ◈ • ────╮
么 [᥉᥆ᥙᖇᥴᥱ عبود](t.me/sssess1s)
么 [ꪔᥡ ꪀᥱᥱძ](https://t.me/rxrpp)
╰──── • ◈ • ────╯

⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼
        """, reply_markup=keyboard, parse_mode=enums.ParseMode.MARKDOWN)

    if m.text == "مطور" or m.text == "المطور" or m.text == "مطور البوت":
        s = await c.get_users(super_sudoers[1])
        n = await c.get_users(sudoers[0])
        sender_name = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
        name_chat = m.chat.title
        id_chat = m.chat.id
        if m.chat.type == enums.ChatType.SUPERGROUP:
            if m.chat.username is not None:
                chat_link = "https://t.me/" + m.chat.username + '/' + str(m.id)
            else:
                chat_link = "https://t.me/c/" + str(id_chat).replace('-100','') + '/' + str(m.id)
        else:
            chat_link = "https://t.me/" + m.chat.username + '/' + str(m.id)
        message_link = chat_link
        cloc = await get_time_and_date()
        clock = cloc[1]
        toda = await get_time_and_date()
        today = toda[0]
        num_member = await c.get_chat_members_count(id_chat)
        if m.chat.username:
            link_group = "https://t.me/" + m.chat.username
        else:
            try:
                link_group = await c.export_chat_invite_link(id_chat)
            except Exception as e:
                link_group = "لايوجد"
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(f"{s.first_name}", user_id=super_sudoers[1])],
            [InlineKeyboardButton(f"{n.first_name}", user_id=sudoers[0])],
            [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅",
                                  url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
        ])
        try:
            await c.get_chat_photos(sudoers[0], limit=1).__anext__()
        except:
            await m.reply_text("◍ الاول: هو مطور السورس \n◍ الثاني: هو صاحب البوت\n√", reply_markup=keyboard),
            await c.send_message(sudoers[0], f"❤️╖ نداء لك ايها المطور\n📟╢ بواسطة {sender_name}\n📆╢ يوم *{today}*\n🕑╢ الساعه *{clock}*\n💌╢ اسم الجروب {name_chat}\n🔰╢ ايدي الجروب *{id_chat}*\n⚙️╢ عدد اعضاء الجروب *{num_member}*\n⛓╢ رابط المسج {message_link}\n🔍╜ الرابط {link_group}", parse_mode=enums.ParseMode.MARKDOWN)
        else:
            async for photo in c.get_chat_photos(sudoers[0], limit=1):
                    await m.reply_photo(photo.file_id, caption="◍ الاول: هو مطور السورس \n◍ الثاني: هو صاحب البوت\n√", reply_markup=keyboard),
                    await c.send_message(sudoers[0], f"❤️╖ نداء لك ايها المطور\n📟╢ بواسطة {sender_name}\n📆╢ يوم *{today}*\n🕑╢ الساعه *{clock}*\n💌╢ اسم الجروب {name_chat}\n🔰╢ ايدي الجروب *{id_chat}*\n⚙️╢ عدد اعضاء الجروب *{num_member}*\n⛓╢ رابط المسج {message_link}\n🔍╜ الرابط {link_group}", parse_mode=enums.ParseMode.MARKDOWN)
        return

    if m.text == "طه" or m.text == "طه":
        s = await c.get_users("7200230058")
        ss = (await c.get_chat("7200230058")).bio
        sender_name = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
        name_chat = m.chat.title
        id_chat = m.chat.id
        if m.chat.type == enums.ChatType.SUPERGROUP:
            if m.chat.username is not None:
                chat_link = "https://t.me/" + m.chat.username + '/' + str(m.id)
            else:
                chat_link = "https://t.me/c/" + str(id_chat).replace('-100','') + '/' + str(m.id)
        else:
            chat_link = "https://t.me/" + m.chat.username + '/' + str(m.id)
        message_link = chat_link
        cloc = await get_time_and_date()
        clock = cloc[1]
        toda = await get_time_and_date()
        today = toda[0]
        num_member = await c.get_chat_members_count(id_chat)
        if m.chat.username:
            link_group = "https://t.me/" + m.chat.username
        else:
            try:
                link_group = await c.export_chat_invite_link(id_chat)
            except Exception as e:
                link_group = "لايوجد"
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(f"{s.first_name}", user_id=1970797144)],
        ])
        try:
            await c.get_chat_photos("7200230058", limit=1).__anext__()
        except:
            await m.reply_text(f"{ss}", reply_markup=keyboard),
            await c.send_message("7200230058", f"❤️╖ نداء لك ايها المبرمج\n📟╢ بواسطة {sender_name}\n📆╢ يوم *{today}*\n🕑╢ الساعه *{clock}*\n💌╢ اسم الجروب {name_chat}\n🔰╢ ايدي الجروب *{id_chat}*\n⚙️╢ عدد اعضاء الجروب *{num_member}*\n⛓╢ رابط المسج {message_link}\n🔍╜ الرابط {link_group}", parse_mode=enums.ParseMode.MARKDOWN)
        else:
            async for photo in c.get_chat_photos("7200230058", limit=1):
                    await m.reply_photo(photo.file_id, caption=f"{ss}", reply_markup=keyboard),
                    await c.send_message("7200230058", f"❤️╖ نداء لك ايها المبرمج\n📟╢ بواسطة {sender_name}\n📆╢ يوم *{today}*\n🕑╢ الساعه *{clock}*\n💌╢ اسم الجروب {name_chat}\n🔰╢ ايدي الجروب *{id_chat}*\n⚙️╢ عدد اعضاء الجروب *{num_member}*\n⛓╢ رابط المسج {message_link}\n🔍╜ الرابط {link_group}", parse_mode=enums.ParseMode.MARKDOWN)
        return

    if m.text == "تغيير المطور الاساسي" or m.text == "تغير المطور الاساسي":
        if sudo(m):
            set_db_wait("changesudo", m.from_user.id, m.chat.id)
            await m.reply_text("◍ ارسل لى ايدي المطور\n√")
            return
        else:
            await m.reply_text("◍ هذا الامر للمطور الاساسي فقط\n√")
            return

    if m.text == "فتح الرابط":
        if admin(m):
            await lock_linggroup_open(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    if m.text  ==  "قفل الرابط" :
        if admin(m):
            await lock_linggroup_close(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    if m.text == "الرابط" or m.text == "انشاء رابط":
        if lock_linggroup_test(m):
            await m.reply_text("◍ الرابط مقفول اطلب من الادمن \n√")
            return
        if get_db_addlinkgroup(m.chat.id) is None:
            if m.chat.username:
                link_group = "https://t.me/" + m.chat.username
                await m.reply_text(
                    "◍ رابط الجروب -> " + link_group + "\n√")
            else:
                try:
                    link_group = await c.export_chat_invite_link(m.chat.id)
                    await m.reply_text(
                        "◍ هذا الرابط مؤقت غير دائم ارسل اضف رابط لوضع رابط دائم\n◍ رابط الجروب -> "
                        + str(link_group) + "\n√")

                except Exception as e:
                    print("link group: \n" + str(e))
                    link_group = "لايوجد"
                    await m.reply_text(link_group)
        else:
            for per in get_db_addlinkgroup(m.chat.id):
                if per[1] == m.chat.id:
                    await m.reply_text(per[0])
                    return
            if m.chat.username:
                link_group = "https://t.me/" + m.chat.username
                await m.reply_text(
                    "◍ رابط الجروب -> " + link_group + "\n√")
            else:
                try:
                    link_group = await c.export_chat_invite_link(m.chat.id)
                    await m.reply_text(
                        "◍ هذا الرابط مؤقت غير دائم ارسل اضف رابط لوضع رابط دائم\n رابط الجروب -> "
                        + str(link_group) + "\n√")

                except Exception as e:
                    print("link group: \n" + str(e))
                    link_group = "لايوجد"
                    await m.reply_text(link_group)

    if m.text == "اضف رابط" or m.text == "ضع رابط" or m.text == "وضع رابط":
        if manager(m):
            set_db_wait("addlinkgroup", m.from_user.id, m.chat.id)
            await m.reply_text("◍ ارسل لى الرابط الان\n√")
        else:
            await m.reply_text("◍ هذا الامر للمالك فقط\n√")
            return

    if m.text == "حذف الرابط" or m.text == "مسح الرابط":
        if manager(m):
            del_db_addlinkgroup(m.chat.id)
            await m.reply_text("◍ تم حذف الرابط بنجاح\n√")
        else:
            await m.reply_text("◍ هذا الامر للمالك فقط\n√")
            return

    if m.text == "فتح صورتي":
        if admin(m):
            await lock_myphoto_open(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    if m.text == "قفل صورتي":
        if admin(m):
            await lock_myphoto_close(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    if m.text == "صورتى" or m.text == "صورتي":
        if lock_myphoto_test(m):
            await m.reply_text("◍ صورتي مقفوله اطلب من الادمن فتحها\n√")
            return
        v = await c.get_chat_photos_count(m.from_user.id)
        async for photo in c.get_chat_photos(m.from_user.id, limit=1):
                            await m.reply_photo(photo.file_id, caption="◍ عدد صورك هو ~⪼ " + str(v))

    if m.text == "اسمي" or m.text == "اسمى":
        if m.from_user.first_name:
            first_name = "◍ اسمك الاول » {`" + m.from_user.first_name + "`}"
        else:
            first_name = ""
        if m.from_user.last_name:
            last_name = "◍ اسمك الثاني » {`" + m.from_user.last_name + "`}"
        else:
            last_name = ""
        await m.reply_text(first_name + "\n" + last_name, parse_mode=enums.ParseMode.MARKDOWN)
        return

    if m.text == "فتح الايدي":
        if admin(m):
            await lock_idgroup_open(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    if m.text == "قفل الايدي":
        if admin(m):
            await lock_idgroup_close(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return
           

    if m.text == "فتح الايدي بالصوره":
        if admin(m):
            await lock_idgroup2_open(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    if m.text == "قفل الايدي بالصوره":
        if admin(m):
            await lock_idgroup2_close(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    if m.text == "id" or m.text == "ايدي" or m.text == "ايدى" or m.text == "الايدي" or m.text == "الايدى"\
            or m.text == "ايديه":
        if lock_idgroup_test(m):
            await m.reply_text("◍ الايدي مقفول اطلب من الادمن \n√")
            return
        await ids(c, m)
        return

    if m.text == "تعيين الايدي" or m.text == "تعين الايدي":
        if constractors(m):
            medooid = """
◍ ارسل الان النص
◍ يمكنك اضافه :
◍ `#rdphoto` ~⪼ تعليق الصوره
◍ `#fname` ~⪼ الاسم الاول 
◍ `#lname` ~⪼ الاسم الاخير 
◍ `#id` ~⪼ ايدي 
◍ `#user` ~⪼ المعرف 
◍ `#mention` ~⪼ اسم الشخص بمنشن 
◍ `#game` ~⪼ نقاطك 
◍ `#msgs` ~⪼ رسائلك 
◍ `#contact` ~⪼ جهاتك 
◍ `#auto` ~⪼ تفاعلك 
◍ `#brank` ~⪼ رتبتك فى البوت 
◍ `#grank` ~⪼ رتبتك فى الجروب 
◍ `#gmsgs` ~⪼ عدد رسائل الجروب 
            """
            set_db_wait("addcustomid", m.from_user.id, m.chat.id)
            await m.reply_text(medooid, parse_mode=enums.ParseMode.MARKDOWN)
            return
        else:
            await m.reply_text("◍ هذا الامر لرتبه منشئ او اعلى\n√")
            return

    if m.text == 'حذف الايدي' or m.text == 'مسح الايدي':
        if constractors(m):
            del_db_addcustomid(m.chat.id)
            await m.reply_text("◍ تم حذف كليشه الايدي\n√")
            return
        else:
            await m.reply_text("◍ هذا الامر لرتبه منشئ او اعلى\n√")
            return

    if m.text == "رتبتي" or m.text == "رتبتى":
        await m.reply_text("◍ رتبتك في البوت » " + await get_Rank(m))
        return

    if m.text == "الرتبه" and m.reply_to_message:
        await m.reply_text(f"◍ العضو » [{m.reply_to_message.from_user.first_name}]"
                           f"(tg://user?id={m.reply_to_message.from_user.id}) \n"
                           f" ◍ الرتبه » {await get_Rankkk(m.reply_to_message.from_user.id, m)}", parse_mode=enums.ParseMode.MARKDOWN)
        return

    if m.text == "كشف" and m.reply_to_message:
        if special(m):
            if m.reply_to_message.from_user.username is None:
                username = "لايوجد"
            else:
                username = f"@{m.reply_to_message.from_user.username}"
            textmessage = f"""
◍ الاسم »  [{m.reply_to_message.from_user.first_name}](tg://user?id={m.reply_to_message.from_user.id})
◍ الايدي »  `{m.reply_to_message.from_user.id}`
◍ المعرف »  {username}
◍ الرتبه »  {await get_Rankkk(m.reply_to_message.from_user.id, m)}
◍ نوع الكشف »  كشف بالرد
◍ سعر الكشف »  
ههه بهزر معاك من غير فلوس طبعا ❤️😂
            """
            await m.reply_text(textmessage, parse_mode=enums.ParseMode.MARKDOWN)
        else:
            await m.reply_text("◍ يجب ان تكون مميز على الاقل لاستخدام هذا الامر\n√")
            return

    if re.match("^كشف @(.*)$", str(m.text)) or re.match("^كشف (\\d+)$", str(m.text)):
        if special(m):
            m.text = m.text[4:]
            result = await check_username(m, c)
            chat_id_foruser = result[0]
            chat_name_foruser = result[1]
            chat_username_foruser = result[2]
            textmessage = f"""
        ◍ الاسم »  [{chat_name_foruser}](tg://user?id={chat_id_foruser})
        ◍ الايدي »  `{chat_id_foruser}`
        ◍ المعرف »  {chat_username_foruser}
        ◍ الرتبه »  {await get_Rankkk(chat_id_foruser,m)}
        ◍ نوع الكشف »  كشف بالمعرف
        ◍ سعر الكشف »  
        ههه بهزر معاك من غير فلوس طبعا ❤️😂
                    """
            await m.reply_text(textmessage, parse_mode=enums.ParseMode.MARKDOWN)
        else:
            await m.reply_text("◍ يجب ان تكون مميز على الاقل لاستخدام هذا الامر\n√")
            return

    if m.text == "كشف القيود" and m.reply_to_message:
        if admin(m):
            if ban_global_test(m.reply_to_message):
                gen_ban = "محظور عام"
            else:
                gen_ban = "غير محظور عام"
            if mute_global_test(m.reply_to_message):
                gen_mute = "مكتوم عام"
            else:
                gen_mute = "غير مكتوم عام"
            if ban_user_test(m.reply_to_message):
                gp_ban = "محظور"
            else:
                gp_ban = "غير محظور"
            if mute_user_test(m.reply_to_message):
                gp_mute = "مكتوم"
            else:
                gp_mute = "غير مكتوم"

            await m.reply_text(f"◍ الحظر العام: {gen_ban}\n◍ الكتم العام: {gen_mute}\n"
                               f"◍ الحظر: {gp_ban}\n◍ الكتم: {gp_mute}\n√")
        else:
            await m.reply_text("◍ هذا الامر لرتبه منشئ او اعلى\n√")
            return
    if re.match("^كشف القيود @(.*)$", str(m.text)) or re.match("^كشف القيود (\\d+)$", str(m.text)):
        if admin(m):
            m.text = m.text[11:]
            result = await check_username(m, c)
            chat_id_foruser = result[0]
            if ban_global_test_byuser(chat_id_foruser):
                gen_ban = "محظور عام"
            else:
                gen_ban = "غير محظور عام"
            if mute_global_test_byuser(chat_id_foruser):
                gen_mute = "مكتوم عام"
            else:
                gen_mute = "غير مكتوم عام"
            if ban_user_test_byuser(m, chat_id_foruser):
                gp_ban = "محظور"
            else:
                gp_ban = "غير محظور"
            if mute_user_test_byuser(m, chat_id_foruser):
                gp_mute = "مكتوم"
            else:
                gp_mute = "غير مكتوم"

            await m.reply_text(f"◍ الحظر العام: {gen_ban}\n◍ الكتم العام: {gen_mute}\n"
                               f"◍ الحظر: {gp_ban}\n◍ الكتم: {gp_mute}\n√")
        else:
            await m.reply_text("◍ هذا الامر لرتبه منشئ او اعلى\n√")
            return

    if m.text == "قفل الترحيب":
        if admin(m):
            await lock_lockwelcome_close(m)
        else:
            await m.reply_text("◍ هذا الامر لرتبه منشئ او اعلى\n√")
            return

    if m.text == "فتح الترحيب":
        if admin(m):
            await lock_lockwelcome_open(m)
        else:
            await m.reply_text("◍ هذا الامر لرتبه منشئ او اعلى\n√")
            return

    if m.text == "اضف ترحيب" or m.text == "ضع ترحيب" or m.text == "وضع ترحيب":
        if constractors(m):
            set_db_wait("addwelcomegroup", m.from_user.id, m.chat.id)
            await m.reply_text("◍ ارسل لى الترحيب الان \n◍ تستطيع اضافة مايلي !\n◍ دالة عرض الاسم » #name \n"
                               "◍ دالة عرض المعرف » #user \n◍ دالة عرض الايدي » #id \n√")
        else:
            await m.reply_text("◍ هذا الامر لرتبه منشئ او اعلى\n√")
            return

    if m.text == "حذف الترحيب" or m.text == "مسح الترحيب":
        if constractors(m):
            del_db_addwelcomegroup(m.chat.id)
            await m.reply_text("◍ تم مسح الترحيب\n√")
        else:
            await m.reply_text("◍ هذا الامر لرتبه منشئ او اعلى\n√")
            return

    if m.text == "الترحيب":
        if admin(m):
            if get_db_addwelcomegroup(m.chat.id) is None:
                user = f"@{m.from_user.username}" if m.from_user.username else "لايوجد"
                t = f"""
✧هـلا بـڪ فـي عـلـمـنـا الـمـتـواضـ؏ 🌚✨

✧اسـمـڪ ي قـمـࢪ {m.from_user.mention} 🌚✨

✧يـوزرڪ ي قـمـࢪ {user} 🌚✨

✧الايـدي بـتـا؏ڪ ي قـمـࢪ {m.from_user.id}🌚✨
                """
                await m.reply_text(t)
            else:
                for per in get_db_addwelcomegroup(m.chat.id):
                    if per[1] == m.chat.id:
                        await m.reply_text(per[0], parse_mode=enums.ParseMode.MARKDOWN)
                        return
                user = f"@{m.from_user.username}" if m.from_user.username else "لايوجد"
                t = f"""
✧هـلا بـڪ فـي عـلـمـنـا الـمـتـواضـ؏ 🌚✨

✧اسـمـڪ ي قـمـࢪ {m.from_user.mention} 🌚✨

✧يـوزرڪ ي قـمـࢪ {user} 🌚✨

✧الايـدي بـتـا؏ڪ ي قـمـࢪ {m.from_user.id}🌚✨
                """
                await m.reply_text(t)
        else:
            await m.reply_text("◍ يجب ان تكون ادمن على الاقل لاستخام هذا الامر\n√")
            return

    if m.text == "فتح المغادره":
        if admin(m):
            await lock_lockbye_open(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    if m.text == "قفل المغادره":
        if admin(m):
            await lock_lockbye_close(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    if m.text == "اضف رساله مغادره" or m.text == "اضف مغادره" or m.text == "وضع مغادره":
        if admin(m):
            set_db_wait("addbyegroup", m.from_user.id, m.chat.id)
            await m.reply_text("◍ ارسل لى رساله المغادره الان \n◍ تستطيع اضافة مايلي !\n◍ دالة عرض الاسم » #name \n"
                               "◍ دالة عرض المعرف » #user \n◍ دالة عرض الايدي » #id \n√")
        else:
            await m.reply_text("◍ يجب ان تكون ادمن على الاقل لكى تستطيع وضع رساله مغادره")
            return

    if m.text == "حذف المغادره" or m.text == "مسح المغادره":
        if admin(m):
            del_db_addbyegroup(m.chat.id)
            await m.reply_text("◍ تم مسح رساله المغادره\n√")
        else:
            await m.reply_text("◍ يجب ان تكون ادمن على الاقل لكى تستطيع مسح رساله المغادره")
            return

    if m.text == "المغادره" or m.text == "رساله المغادره":
        if admin(m):
            if get_db_addbyegroup(m.chat.id) is None:
                t = f"""
• انت مش جدع يا {m.from_user.mention} 🥺
❬ حد يكون فى روم زى ده ويخرج ❭ 🙄️
❬ ده حتى كلنا اخوات واصحاب ❭ 🥺️ √
❬ يلا بالسلامات ❭ ❤️😂
                        """
                await m.reply_text(t, parse_mode=enums.ParseMode.MARKDOWN)
            else:
                for per in get_db_addbyegroup(m.chat.id):
                    if per[1] == m.chat.id:
                        await m.reply_text(per[0])
                        return
                t = f"""
• انت مش جدع يا {m.from_user.mention} 🥺
❬ حد يكون فى روم زى ده ويخرج ❭ 🙄️
❬ ده حتى كلنا اخوات واصحاب ❭ 🥺️ √
❬ يلا بالسلامات ❭ ❤️😂
                            """
                await m.reply_text(t)
        else:
            await m.reply_text("◍ يجب ان تكون ادمن على الاقل لاستخام هذا الامر\n√")
            return

    if m.text == "اى رايك فيه" or m.text == "رد انت يابوت":
        texting = ["قليل الادب بتاع بنات 😂🥺", " طب اركنلى على جمب وانا هرد 😶", "هجيبو راكع لحد عندك 😾😹"]
        await m.reply_text(random.choice(texting))
        return

    if m.text == "اى رايك يابوت" or m.text == "بوت اى رايك":
        texting = ["جامده اوى يابوى🤕😹", "من رأى انك تسكت خلاص☹️😾", "حقيره ومنتكبره 😶😂", "مدخلنيش فى الموضوع 😔😒"]
        await m.reply_text(random.choice(texting))
        return

    if m.text == "هينو" or m.text == "هينها" or m.text == "هينه" or m.text == "دايقو" or m.text == "دايقها":
        texting = ["ياعم بقولك اى انا مش ناقصكو انتو الاتنين اتخرصو بقا 🙄😑",
                   "شكرا ي صحبي او ياللي كنت فاكرك 😏 صحبي", "لو جيت جمبه هزعلك مني فل!! ", "سيبنى محدش يمسكني 😎",
                   "سيبك منو ده عيل جربوع 😂💔", "ده واطى وندل فكك منو 😂💔", "اتقل عليه هعمل منو بطاطس محمره 😂💔"]
        await m.reply_text(random.choice(texting))
        return

    if m.text == "بوسو" or m.text == "بوسه" or m.text == "بوسها":
        texting = ["امووووووووواحح😘💕", "استغفر الله فاسق 😒", "الوجه ميساعد 😐✋", "ببوس حريم بس😌😹", "خدك نضيف!؟ 😂",
                   "تدفع كام! 🌝", "اوه ياه 🙊😂", "كل شويه بوسه بوسه 😏", "مش بايس حد انا فل!! ",
                   "امموووواه لعيونك ي جميل 💎💗😹"]
        await m.reply_text(random.choice(texting))
        return

    if m.text == "بتحب دي" or m.text == "بتحب دى" or m.text == "بوت بتحب دي" or m.text == \
            "بوت بتحب دى" or m.text == "بوت بتحب البت دى" or m.text == "بوت بتحب البت دي":
        texting = ["اه يسطا قلبى ده 😊❤️", "بقا القمر ده حد يكرهو 🙈❤️",
                   "ده انا قلبى استوي تعبان ومليش دواا ودايب فى حبو ااه 😹💔", "بكرهها من كل قلبى 🙂",
                   "محبش حد مش سالك 🥺😔", "دى تقول للقمر قوم وانا اقعد مكانك 🔥🖤",
                   "ولا اعرفها 🤔! ", "مش تبعي لأ 😏", "واحبها لي يعني 🙄😎", "لأ طبعاً",
                   "دي قطعه من قلبي 💎♥️", "اموت انا واعيد السنه 🙈😻", "بنت قلبي💗", "الحتهه الشماال 💖😂"]
        await m.reply_text(random.choice(texting))
        return

    if m.text == "بتحب ده" or m.text == "بتحب الواد ده" or m.text == "بوت بتحب الواد ده" or m.text == "بوت بتحب ده":
        texting = ["اخويا وصحبي وكفاءة 😂 ", " اللي مشرف دوله 🔥 ", " ابن قلبي ♥️💪",
                   " اخويا الجدع ال مافيش منه مرتجع❤️😂", "قلباااي😂💗 ", "انت مين انت العب بعيد ي حبيبي",
                   "مسمعتش الاسم ده قبل كدة 🙄", " محصليش الشرف😏", "بدى ارجع يعع 💔😂"]
        await m.reply_text(random.choice(texting))
        return
       

    if m.text == "بحبك" or m.text == "بحبك يابوت" or m.text == "يابوت بحبك":
        await m.reply_text(f"وانا كمان بعشقك يا [{m.from_user.first_name}](tg://user?id={m.from_user.id})💋🥰", parse_mode=enums.ParseMode.MARKDOWN)

    if m.text == "رابط الحذف" or m.text == "رابط حذف" or m.text == "بوت حذف" or m.text == "بوت الحذف":
        if lock_deletelink_test(m):
            texting = """
رابط الحذف في جميع مواقع التواصل ✸
فكر قبل لا تتسرع وتروح
ٴ≪━━━━━alpop━━━━━≫ٴ
◍ بوت حذف [Telegram](t.me/SD88BOT) √
◍ رابط حذف [Telegram](https://my.telegram.org/auth?to=delete) √
◍ رابط حذف [instagram](https://www.instagram.com/accounts/login/?next=/accounts/remove/request/permanent/) √
◍ رابط حذف [Facebook](https://www.facebook.com/help/deleteaccount) √
◍ رابط حذف [Snspchat](https://accounts.snapchat.com/accounts/login?continue=https%3A%2F%2Faccounts.snapchat.com%2Faccounts%2Fdeleteaccount) √   
            """
            await m.reply_text(texting, parse_mode=enums.ParseMode.MARKDOWN)
            return
        else:
            await m.reply_text("◍ رابط الحذف مغلق اطلب من الادمن فتحه\n√")
            return

    if m.text == "قفل رابط الحذف":
        if admin(m):
            await lock_deletelink_open(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    if m.text == "فتح رابط الحذف":
        if admin(m):
            await lock_deletelink_close(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    if m.text == "الاوامر" or m.text == "اوامر" or m.text == "م1" or m.text == "m1" or m.text == "م2"\
            or m.text == "m2" or m.text == "م3" or m.text == "m3" or m.text == "م4" or m.text == "m4"\
            or m.text == "م5" or m.text == "m5" or m.text == "m6" or m.text == "م6":
        await command(c, m)
        return

    if m.text == "مسح" or m.text == "حذف" and m.reply_to_message:
        if admin(m):
            await del_message(c, m)
            return

    if re.match("^مسح (\\d+)$", str(m.text)) or re.match("^حذف (\\d+)$", str(m.text))\
            or re.match("^تنظيف (\\d+)$", str(m.text)):
        num = int(m.text[4:])
        message_id = m.id
        if constractors(m):
            if num > 1000:
                await m.reply_text("◍ تستطيع التنظيف ل 1000 رساله كحد اقصى\n√")
            else:
                for i in range(num):
                    await c.delete_messages(m.chat.id, message_id)
                    message_id = message_id - 1
                await m.reply_text(f"◍ تم حذف {num} من الرسايل\n√")
        else:
            await m.reply_text("◍ هذا الامر لرتبه منشئ او اعلى\n√")

    if m.text == "اطردني" or m.text == "احظرني":
        if lock_kickme_test(m):
            try:
                if m.from_user.id == super_sudoers[0]:
                    await m.reply_animation("https://t.me/UUSDI55/36",
                                                                caption=f"◍ لايمكننى طرد مبرمج السورس\n√", parse_mode=enums.ParseMode.MARKDOWN)
                    return
                elif m.from_user.id == super_sudoers[1]:
                    await m.reply_animation("https://t.me/UUSDI55/36",
                                                                caption=f"◍ لايمكننى طرد مطور السورس\n√", parse_mode=enums.ParseMode.MARKDOWN)
                    return
                elif secsudo(m):
                    await m.reply_animation("https://t.me/UUSDI55/36",
                                                                caption=f"◍ لايمكننى طرد المطور الاساسي\n√", parse_mode=enums.ParseMode.MARKDOWN)
                    return
                elif sudo2(m):
                    await m.reply_animation("https://t.me/UUSDI55/36",
                                                                caption=f"◍ لايمكننى طرد المطور\n√", parse_mode=enums.ParseMode.MARKDOWN)
                    return
                elif special(m):
                    await m.reply_animation("https://t.me/UUSDI55/36",
                                                                caption=f"◍ لايمكننى طردك بسبب رتبتك\n√", parse_mode=enums.ParseMode.MARKDOWN)
                    return
                else:
                    check = await get_available_adminstrator(c, m)
                    if check[0]:
                        await m.reply_text("◍ انت ادمن فى الجروب انزل من الادمنيه الاول\n√")
                        return
                await m.reply_animation("https://t.me/UUSDI55/37",
                                                            caption=f"◍ تم طردك\n√", parse_mode=enums.ParseMode.MARKDOWN)
                await c.ban_chat_member(m.chat.id, m.from_user.id)
                await m.chat.unban_member(m.from_user.id)
            except Exception as e:
                await m.reply_text(str(e) + "\n\n" +
                                   "فى حاله ظهور لك مثلا هذه الرساله تواصل مع المطور -> "
                                   "[Marcelo](tg://user?id=super_sudoers[0])", parse_mode=enums.ParseMode.MARKDOWN)
                return
        else:
            await m.reply_text("◍ تم تعطيل امر اطردني اترزع هنا مفيش خروج\n√")
        return

    if m.text == "اكتمني":
        if lock_kickme_test(m):
            try:
                if m.from_user.id == super_sudoers[0]:
                    await m.reply_animation("https://t.me/UUSDI55/38",
                                                                caption=f"◍ لايمكننى كتم مبرمج السورس\n√", parse_mode=enums.ParseMode.MARKDOWN)
                    return
                elif m.from_user.id == super_sudoers[1]:
                    await m.reply_animation("https://t.me/UUSDI55/38",
                                                                caption=f"◍ لايمكننى كتم مطور السورس\n√", parse_mode=enums.ParseMode.MARKDOWN)
                    return
                elif secsudo(m):
                    await m.reply_animation("https://t.me/UUSDI55/38",
                                                                caption=f"◍ لايمكننى كتم المطور الاساسي\n√", parse_mode=enums.ParseMode.MARKDOWN)
                    return
                elif sudo2(m):
                    await m.reply_animation("https://t.me/UUSDI55/38",
                                                                caption=f"◍ لايمكننى كتم المطور\n√", parse_mode=enums.ParseMode.MARKDOWN)
                    return
                elif special(m):
                    await m.reply_animation("https://t.me/UUSDI55/38",
                                                                caption=f"◍ لايمكننى كتمك بسبب رتبتك\n√", parse_mode=enums.ParseMode.MARKDOWN)
                    return
                else:
                    check = await get_available_adminstrator(c, m)
                    if check[0]:
                        await m.reply_text("◍ انت ادمن فى الجروب انزل من الادمنيه الاول\n√")
                        return
                await m.reply_animation("https://t.me/UUSDI55/39",
                                                            caption=f"◍ تم كتمك\n√", parse_mode=enums.ParseMode.MARKDOWN)
                await c.restrict_chat_member(m.chat.id,
                                             m.from_user.id,
                                             ChatPermissions())
            except Exception as e:
                await m.reply_text(str(e) + "\n\n" +
                                   "فى حاله ظهور لك مثلا هذه الرساله تواصل مع المطور -> "
                                   "[Marcelo](tg://user?id=super_sudoers[0])", parse_mode=enums.ParseMode.MARKDOWN)
                return

        else:
            await m.reply_text("◍ تم تعطيل امر اكتمني اترزع هنا مفيش خروج\n√")
        return

    if m.text == "قفل اطردني" or m.text == "قفل اطردنى" or m.text == "قفل اكتمني" or m.text == "قفل اكتمنى":
        if admin(m):
            await lock_kickme_open(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    if m.text == "فتح اطردني" or m.text == "فتح اطردنى" or m.text == "فتح اكتمني" or m.text == "فتح اكتمنى":
        if admin(m):
            await lock_kickme_close(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    if m.text == "انا مين":
        await m.reply_text(await get_Rank_ana_meen(m), parse_mode=enums.ParseMode.MARKDOWN)
        return

    if m.text == "انا فين":
        await m.reply_text(await get_Rank_ana_feen(m, c), parse_mode=enums.ParseMode.MARKDOWN)
        return

    if m.text == "مين ضافني" or m.text == "مين ضافنى":
        if not lock_meendafny_test(m):
            if manager(m):
                await m.reply_text("◍ انت منشئ الجروب محدش ضافك\n√")
            else:
                meendafny = "◍ انت دخلت من اللينك ياصحبي بطل صياح بقا\n√"
                if get_db_meendafny(m.from_user.id, m.chat.id) is None:
                    meendafny = "◍ انت دخلت من اللينك ياصحبي بطل صياح بقا\n√"
                else:
                    for row in get_db_meendafny(m.from_user.id, m.chat.id):
                        if row[2] == m.from_user.id:
                            meendafny = f"◍ الشخص الذى قام باضافتك هو [{row[1]}](tg://user?id={row[0]})\n√"

                await m.reply_text(meendafny, parse_mode=enums.ParseMode.MARKDOWN)
                return
        else:
            await m.reply_text("◍ مين ضافني معطله يرجى تفعيلها اولا\n√")

    if m.text == "فتح مين ضافني":
        if admin(m):
            await lock_meendafny_open(m)
        else:
            await m.reply_text("◍ هذا الامر لرتبه ادمن فما فوق")
            return

    if m.text == "قفل مين ضافني":
        if admin(m):
            await lock_meendafny_close(m)
        else:
            await m.reply_text("◍ هذا الامر لرتبه ادمن فما فوق")
            return

    if m.text == "جهاتي" or m.text == "جهاتى":
        await m.reply_text(f"◍ عدد جهاتك هى {get_mycontact(m)}\n√")
        return

    if m.text == "حذف جهاتي" or m.text == "مسح جهاتى":
        del_db_mycontact(m.from_user.id, m.chat.id)
        await m.reply_text("◍ تم حذف جهاتك بنجاح\n√")
        return

    if m.text == "نقاطي" or m.text == "نقاطى":
        await m.reply_text(f"◍ عدد نقاطك هى {get_mypoint(m)}\n√")
        return

    if m.text == "حذف نقاطي" or m.text == "مسح نقاطي":
        del_db_mypointgame(m.from_user.id, m.chat.id)
        await m.reply_text("◍ تم حذف نقاطك بنجاح\n√")
        return

    if m.text == "بيع نقاطي":
        set_db_wait("sellmypoint", m.from_user.id, m.chat.id)
        await m.reply_text("◍ ارسل لى عدد النقاط التى ترغب فى بيعها\n√")
        return

    if re.match("^اضف نقاط (\\d+)$", str(m.text)) and m.reply_to_message:
        if manager(m):
            set_db_mypointgame(int(m.text[9:]), m.reply_to_message.from_user.id, m.chat.id)
            await m.reply_text(f"◍ تم اضافه *{m.text[9:]}* نقطه له\n√")
            return
        else:
            await m.reply_text("◍ انت لست المالك\n√")
            return

    if m.text == "رسائلي" or m.text == "رسائلى":
        await m.reply_text(f"◍ عدد رسائلك هى {get_mymessage(m)}\n√")
        return

    if m.text == "حذف رسائلي" or m.text == "مسح رسائلي":
        del_db_mymessage(m.from_user.id, m.chat.id)
        await m.reply_text("◍ تم حذف رسائلك بنجاح\n√")
        return

    if m.text == "صلاحياتي" or m.text == "صلاحياتى":
        s = requests.get("https://api.telegram.org/bot" + TOKEN + "/getChatMember?chat_id=" + str(m.chat.id) +
                         "&user_id=" + str(m.from_user.id))
        sl = s.json()
        if sl["ok"] is True:
            if sl["result"]["status"] == "creator":
                await m.reply_text("◍ انت مالك الجروب\n√")
                return
            if sl["result"]["status"] == "member":
                await m.reply_text("◍ مجرد عضو هنا\n√")
                return
            if sl["result"]["status"] == "left":
                await m.reply_text("◍ الشخص غير موجود هنا\n√")
                return
            if sl["result"]["status"] == "administrator":
                if sl["result"]["can_change_info"] is True:
                    info = '√'
                else:
                    info = '✘'
                if sl["result"]["can_delete_messages"] is True:
                    delete = '√'
                else:
                    delete = '✘'
                if sl["result"]["can_invite_users"] is True:
                    invite = '√'
                else:
                    invite = '✘'
                if sl["result"]["can_pin_messages"] is True:
                    pinmessage = '√'
                else:
                    pinmessage = '✘'
                if sl["result"]["can_restrict_members"] is True:
                    restrict = '√'
                else:
                    restrict = '✘'
                if sl["result"]["can_promote_members"] is True:
                    promote = '√'
                else:
                    promote = '✘'
                await m.reply_text(f"\n◍ الرتبة : مشرف  "
                                   f"\n◍ والصلاحيات هي ↓ \nٴ━━━━━━━━━━\n◍ تغيير معلومات الجروب ↞ ❴ {info} ❵\n"
                                   f"◍ حذف الرسائل ↞ ❴ {delete} ❵\n◍ حظر المستخدمين ↞ ❴ {restrict} ❵\n"
                                   f"◍ دعوة مستخدمين ↞ ❴ {invite} ❵\n◍ تثبيت الرسائل ↞ ❴ {pinmessage} ❵\n"
                                   f"◍ اضافة مشرفين جدد ↞ ❴ {promote} ❵")
    if m.text == "اضف امر":
        if manager(m):
            del_db_wait("addnewcommand")
            del_db_wait("addnewcommand2")
            set_db_wait("addnewcommand", m.from_user.id, m.chat.id)
            await m.reply_text("◍ ارسل الامر القديم\n√")
            return
        else:
            await m.reply_text("◍ يجب ان تكون برتبه مالك لاستخدام هذا الامر\n√")
            return

    if m.text == "حذف امر":
        if manager(m):
            set_db_wait("dellnewcommand", m.from_user.id, m.chat.id)
            await m.reply_text("◍ ارسل الامر الذي قمت بوضعه بدلا عن القديم\n√")
            return
        else:
            await m.reply_text("◍ انت لست المالك\n√")
            return

    if m.text == "الاوامر المضافه":
        if manager(m):
            lang = get_db_addcommand(m.chat.id)
            if lang is None:
                await m.reply_text("◍ لا توجد اوامر مضافه")
            else:
                t = "\n◍ قائمة الاوامر المضافه \n≪━━━━━━━━━━━━━≫\n"
                for row in lang:
                    t = t + f"({row[0]})--->({row[1]})\n"
                await m.reply_text(t)
            return
        else:
            await m.reply_text("◍ انت لست المالك\n√")
            return

    if m.text == "حذف الاوامر المضافه":
        if manager(m):
            del_db_addcommandall(m.chat.id)
            await m.reply_text("◍ تم حذف الاوامر المضافه\n√")
            return
        else:
            await m.reply_text("◍ انت لست المالك\n√")
            return

    if m.text == "كشف البوتات":
        if admin(m):
            a = "◍ قائمة البوتات 🕹️\n≪━━━━━━━━━━━━━≫"
            b = "\n├ "
            count = 0
            async for x in c.get_chat_members(m.chat.id, filter=enums.ChatMembersFilter.BOTS):
                count += 1
                if x.status == enums.ChatMemberStatus.ADMINISTRATOR:
                    a += b + f"[@{x.user.username}](tg://user?id={x.user.id}) ✬"
                else:
                    a += b + f"[@{x.user.username}](tg://user?id={x.user.id})"
            await m.reply_text(a + f"\n\n◍ علامه ✬ تعني ان البوت ادمن\n◍ عدد البوتات في الجروب {count} بوت\n√", parse_mode=enums.ParseMode.MARKDOWN)
            return
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    if m.text == "طرد البوتات":
        if constractors(m):
            async for x in c.get_chat_members(m.chat.id, filter=enums.ChatMembersFilter.BOTS):
                try:
                    await c.ban_chat_member(m.chat.id, x.user.id)
                    await m.chat.unban_member(x.user.id)
                except Exception as e:
                    print("kick all bots: \n" + str(e))
                    continue
            await m.reply_text("◍ تم طرد البوتات اللى مش مرفوعه ادمن\n√", parse_mode=enums.ParseMode.MARKDOWN)
            return
        else:
            await m.reply_text("◍ هذا الامر لرتبه منشئ او اعلى\n√")
            return

    if m.text == "فتح البوتات بالطرد":
        if constractors(m):
            await lock_kickbotatban_open(m)
            return
        else:
            await m.reply_text("◍ هذا الامر لرتبه منشئ او اعلى\n√")
            return

    if m.text == "قفل البوتات بالطرد":
        if constractors(m):
            await lock_kickbotatban_close(m)
            return
        else:
            await m.reply_text("◍ هذا الامر لرتبه منشئ او اعلى\n√")
            return

    if m.text == "تحويل" and m.reply_to_message:
        if m.reply_to_message.photo:
            await c.download_media(m.reply_to_message, file_name="./sticker.webp")
            await m.reply_sticker("sticker.webp")
            os.remove("sticker.webp")
            return
        if m.reply_to_message.sticker:
            await c.download_media(m.reply_to_message, file_name="./photo.jpg")
            await m.reply_photo("photo.jpg", caption=f"تم تحويل الملصق الى صوره بواسطه:\n @{get_bot_information()[1]}")
            os.remove("photo.jpg")
            return
        if m.reply_to_message.audio:
            await c.download_media(m.reply_to_message, file_name="./voice.ogg")
            await m.reply_voice("voice.ogg")
            os.remove("voice.ogg")
            return
        if m.reply_to_message.voice:
            await c.download_media(m.reply_to_message, file_name="./audio.mp3")
            await m.reply_audio("audio.mp3")
            os.remove("audio.mp3")
            return
        if m.reply_to_message.video:
            await c.download_media(m.reply_to_message, file_name="./animation.gif")
            await m.reply_animation("animation.gif")
            os.remove("animation.gif")
            return


########################################################################################################################
########################################################################################################################
   
    if m.text == "استوري" or m.text == "ستوري":
        await status(c, m)
        return  
 
    if m.text == "رمزيات" or m.text == "رمزيه":
        await rmaziat(c, m)
        return    
        
    if m.text == "غنيلي" or m.text == "غنيلى":
        await ghnely(c, m)
        return     

    if m.text == "قرءان" or m.text == "قران" or m.text == "قرآن" or m.text == "القرآن" or m.text == "القرءان":
        await quran(c, m)
        return

    if m.text == "اغانى" or m.text == "اغاني" or m.text == "الاغاني" or m.text == "الاغانى":
        if await lock_music_test(m) and not constractors(m):
            await m.reply_text("◍ الاغاني مقفوله اطلب من الادمن فتحها\n√")
            return
        else:
            await music(c, m)
            return

    if m.text == "فتح الاغانى" or m.text == "فتح الاغاني":
        if admin(m):
            await lock_music_open(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    if m.text == "قفل الاغانى" or m.text == "قفل الاغاني":
        if admin(m):
            await lock_music_close(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    if m.text == "زخرفه" or m.text == "زخرفة" or m.text == "الزخرفه":
        if await lock_zhrafa_test(m) and not constractors(m):
            await m.reply_text("◍ الزخرفه مقفوله اطلب من الادمن فتحها")
            return
        else:
            await m.reply_text("◍ حسننا , الان يمكنك ارسال الاسم ليتم زخرفته بالعربى او بالنجليزى 🙄")
            set_db_wait("zhrfa", m.from_user.id, m.chat.id)
            return

    if m.text == "فتح الزخرفه" or m.text == "فتح الزخرفة":
        if admin(m):
            await lock_zhrafa_open(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    if m.text == "قفل الزخرفه" or m.text == "قفل الزخرفة":
        if admin(m):
            await lock_zhrafa_close(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    if m.text == "الافلام" or m.text == "افلام" or m.text == "أفلام" or m.text == "فيلم" or m.text == "افلامي"\
            or m.text == "مسلسلات" or m.text == "المسلسلات" or m.text == "مسرحيه" or m.text == "مسرحيات"\
            or m.text == "مسلسل":
        if await lock_aflam_test(m) and not constractors(m):
            await m.reply_text("◍ الافلام مقفوله اطلب من الادمن فتحها")
            return
        else:
            await aflamAR(c, m)
            return

    if m.text == "كارتون" or m.text == "الكارتون" or m.text == "كرتون":
        if await lock_aflam_test(m) and not constractors(m):
            await m.reply_text("◍ الافلام مقفوله اطلب من الادمن فتحها")
            return
        else:
            await cartoon(c, m)
            return

    if m.text == "فتح الافلام":
        if admin(m):
            await lock_aflam_open(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    if m.text == "قفل الافلام":
        if admin(m):
            await lock_aflam_close(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    if m.text == "يوتيوب" or m.text == "اليوتيوب":
        if await lock_youtube_test(m) and not constractors(m):
            await m.reply_text("◍ اليوتيوب مقفول اطلب من الادمن فتحه")
            return
        else:
            if await lock_lockgenyoutube_test():
                await youtube_main(c, m)
                return
            else:
                await m.reply_text("◍ عذراا اليوتوب فى الصيانه حاليا⚠️\n√")
                return

    if m.text == "فتح اليوتيوب":
        if admin(m):
            await lock_youtube_open(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    if m.text == "قفل اليوتيوب":
        if admin(m):
            await lock_youtube_close(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    if m.text == "فتح الترجمه":
        if admin(m):
            await lock_translate_open(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    if m.text == "قفل الترجمه":
        if admin(m):
            await lock_translate_close(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    if m.text == "فتح الرفع":
        if admin(m):
            await lock_upp_open(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    if m.text == "قفل الرفع":
        if admin(m):
            await lock_upp_close(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    if m.text == "فتح الاذكار":
        if admin(m):
            await lock_azkar_open(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    if m.text == "قفل الاذكار":
        if admin(m):
            await lock_azkar_close(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    if m.text == "فتح الالعاب":
        if admin(m):
            await lock_games_open(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    if m.text == "قفل الالعاب":
        if admin(m):
            await lock_games_close(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    await games(c, m)

    if m.text == "روايات" or m.text == "الروايات" or m.text == "روايه" or m.text == "كتب"\
            or m.text == "كتاب" or m.text == "روايات عربيه" or m.text == "روايات عالميه":
        if lock_rwayat_test(m):
            await m.reply_text("◍ الروايات مقفوله اطلب من الادمن فتحها")
            return
        else:
            await rwaiat(c, m)
            return

    if m.text == "فتح الروايات":
        if admin(m):
            await lock_rwayat_open(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    if m.text == "قفل الروايات":
        if admin(m):
            await lock_rwayat_close(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    if re.match("^معني (.*)$", str(m.text)) or re.match("^معنى (.*)$", str(m.text)):
        if lock_namemeaning_test(m):
            await m.reply_text("◍ معاني الاسماء مقفوله اطلب من الادمن فتحها")
            return
        else:
            r = requests.get("https://leadermedo.herokuapp.com/name.php?leomedo=" + m.text[5:])
            rj = r.json()
            await m.reply_text(rj["meaning"])
            return

    if m.text == "فتح معاني الاسماء":
        if admin(m):
            await lock_namemeaning_open(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    if m.text == "قفل معاني الاسماء":
        if admin(m):
            await lock_namemeaning_close(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    if m.text == "الابراج" or m.text == "ابراج":
        if lock_abrag_test(m):
            await m.reply_text("◍ الابراج مقفوله اطلب من الادمن فتحها")
            return
        else:
            await abrag(c, m)
            return

    if m.text == "فتح الابراج":
        if admin(m):
            await lock_abrag_open(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    if m.text == "قفل الابراج":
        if admin(m):
            await lock_abrag_close(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

########################################################################################################################
########################################################################################################################

    await hals_func_all(m)

########################################################################################################################
########################################################################################################################

    if m.text == "اضف اسم" or m.text == "ضع اسم":
        if manager(m):
            set_db_wait("addnamegroup", m.from_user.id, m.chat.id)
            await m.reply_text("◍ ارسل لى الاسم الان\n√")
            return
        else:
            await m.reply_text("◍ هذا الامر للمالك فقط\n√")
            return

    if m.text == "اضف صوره" or m.text == "ضع صوره":
        if manager(m):
            set_db_wait("addphotogroup", m.from_user.id, m.chat.id)
            await m.reply_text("◍ ارسل لى الصوره الان\n√")
            return
        else:
            await m.reply_text("◍ هذا الامر للمالك فقط\n√")
            return

    if m.text == "اضف وصف" or m.text == "ضع وصف":
        if manager(m):
            set_db_wait("adddescreptiongroup", m.from_user.id, m.chat.id)
            await m.reply_text("◍ ارسل لى الوصف الان\n√")
            return
        else:
            await m.reply_text("◍ هذا الامر للمالك فقط\n√")
            return

    if re.match("^طقس (.*)$", str(m.text)):
        await weather(c, m)
        return

########################################################################################################################
########################################################################################################################

    if m.text == "فتح الروابط بالطرد":
        if constractors(m):
            await lock_link_ban_open(m)
        else:
            await m.reply_text("◍ هذا الامر لرتبه منشئ او اعلى\n√")
            return

    if m.text == "قفل الروابط بالطرد":
        if constractors(m):
            await lock_link_close_ban(m)
        else:
            await m.reply_text("◍ هذا الامر لرتبه منشئ او اعلى\n√")
            return

    if m.text == "فتح الروابط بالكتم":
        if constractors(m):
            await lock_link_mute_open(m)
        else:
            await m.reply_text("◍ هذا الامر لرتبه منشئ او اعلى\n√")
            return

    if m.text == "قفل الروابط بالكتم":
        if constractors(m):
            await lock_link_close_mute(m)
        else:
            await m.reply_text("◍ هذا الامر لرتبه منشئ او اعلى\n√")
            return

    if m.text == "فتح التوجيه بالطرد":
        if constractors(m):
            await lock_forward_open_ban(m)
        else:
            await m.reply_text("◍ هذا الامر لرتبه منشئ او اعلى\n√")
            return

    if m.text == "قفل التوجيه بالطرد":
        if constractors(m):
            await lock_forward_close_ban(m)
        else:
            await m.reply_text("◍ يجب ان تكون معك رتبه على الاقل لكى تستطيع قفل التوجيه\n√")
            return

    if m.text == "فتح التوجيه بالكتم":
        if constractors(m):
            await lock_forward_open_mute(m)
        else:
            await m.reply_text("◍ هذا الامر لرتبه منشئ او اعلى\n√")
            return

    if m.text == "قفل التوجيه بالكتم":
        if constractors(m):
            await lock_forward_close_mute(m)
        else:
            await m.reply_text("◍ هذا الامر لرتبه منشئ او اعلى\n√")
            return

    if m.text == "فتح الفشار بالطرد":
        if constractors(m):
            await lock_fshar_open_ban(m)
        else:
            await m.reply_text("◍ هذا الامر لرتبه منشئ او اعلى\n√")
            return

    if m.text == "قفل الفشار بالطرد":
        if constractors(m):
            await lock_fshar_close_ban(m)
        else:
            await m.reply_text("◍ هذا الامر لرتبه منشئ او اعلى\n√")
            return

    if m.text == "فتح الفشار بالكتم":
        if constractors(m):
            await lock_fshar_open_mute(m)
        else:
            await m.reply_text("◍ هذا الامر لرتبه منشئ او اعلى\n√")
            return

    if m.text == "قفل الفشار بالكتم":
        if constractors(m):
            await lock_fshar_close_mute(m)
        else:
            await m.reply_text("◍ هذا الامر لرتبه منشئ او اعلى\n√")
            return

    if m.text == "فتح الممنوعه بالطرد":
        if constractors(m):
            await lock_blocktext_open_ban(m)
        else:
            await m.reply_text("◍ هذا الامر لرتبه منشئ او اعلى\n√")
            return

    if m.text == "قفل الممنوعه بالطرد":
        if constractors(m):
            await lock_blocktext_close_ban(m)
        else:
            await m.reply_text("◍ هذا الامر لرتبه منشئ او اعلى\n√")
            return

    if m.text == "فتح الممنوعه بالكتم":
        if constractors(m):
            await lock_blocktext_open_mute(m)
        else:
            await m.reply_text("◍ هذا الامر لرتبه منشئ او اعلى\n√")
            return

    if m.text == "قفل الممنوعه بالكتم":
        if constractors(m):
            await lock_blocktext_close_mute(m)
        else:
            await m.reply_text("◍ هذا الامر لرتبه منشئ او اعلى\n√")
            return

    if m.text == "فتح الدخول":
        if manager(m):
            await lock_entrygp_open(m)
        else:
            await m.reply_text("◍ هذا الامر للمالك فقط\n√")
            return

    if m.text == "قفل الدخول":
        if manager(m):
            await lock_entrygp_close(m)
        else:
            await m.reply_text("◍ هذا الامر للمالك فقط\n√")
            return

    if m.text == "فتح الكل":
        if manager(m):
            await lock_openall(m)
        else:
            await m.reply_text("◍ هذا الامر للمالك فقط\n√")
            return

    if m.text == "قفل الكل":
        if manager(m):
            await lock_closeall(m)
        else:
            await m.reply_text("◍ هذا الامر للمالك فقط\n√")
            return


########################################################################################################################
########################################################################################################################

    if m.text == "حذف النسخه الاحتياطيه الاخري":
        if sudo(m):
            try:
                await c.download_media("BQACAgQAAx0CTEOqYQACLP5g3GJA8BY14SzGR8jeZkrDYrftVgACMQgAArDn4VLEaUk7DR2B7x4E",
                                       file_name="./leomedo2.db")
                os.chmod('leomedo2.db', 0o644)
                await m.reply_text("◍ تم حذف النسخه الاحتياطيه الاخري\n√")
                await restart(c, m)
            except Exception as e:
                await m.reply_text(str(e) + "\n\n" +
                                   "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى", parse_mode=enums.ParseMode.MARKDOWN)
                return

        else:
            await m.reply_text("◍ هذا الامر للمطور الاساسي فقط\n√")
            return

    if m.text == "حذف داتابيز المحظورين":
        if sudo(m):
            del_db_banallall()
            await m.reply_text("◍ تم حذف الجدول الخاص بالمحظورين\n√")
        else:
            await m.reply_text("◍ هذا الامر للمطور الاساسي فقط\n√")
            return

    if m.text == "حذف داتابيز المكتومين":
        if sudo(m):
            del_db_muteallall()
            await m.reply_text("◍ تم حذف الجدول الخاص بالمكتومين\n√")
        else:
            await m.reply_text("◍ هذا الامر للمطور الاساسي فقط\n√")
            return

    if m.text == "حذف داتابيز مين ضافني":
        if sudo(m):
            del_db_meendafnyallall()
            await m.reply_text("◍ تم حذف الجدول الخاص بمين ضافني\n√")
        else:
            await m.reply_text("◍ هذا الامر للمطور الاساسي فقط\n√")
            return

    if m.text == "حذف داتابيز جهاتي":
        if sudo(m):
            del_db_mycontactallall()
            await m.reply_text("◍ تم حذف الجدول الخاص بالجهات\n√")
        else:
            await m.reply_text("◍ هذا الامر للمطور الاساسي فقط\n√")
            return

    if m.text == "حذف داتابيز النقاط":
        if sudo(m):
            del_db_mypointgameallall()
            await m.reply_text("◍ تم حذف الجدول الخاص بالنقاط\n√")
        else:
            await m.reply_text("◍ هذا الامر للمطور الاساسي فقط\n√")
            return

    if m.text == "حذف داتابيز رسائلي":
        if sudo(m):
            del_db_mymessageallall()
            await m.reply_text("◍ تم حذف الجدول الخاص برسائلي\n√")
        else:
            await m.reply_text("◍ هذا الامر للمطور الاساسي فقط\n√")
            return

    if m.text == "حذف داتابيز ردود الجروب":
        if sudo(m):
            drop_db_replygroup()
            await m.reply_text("◍ تم حذف الجدول الخاص بردود الجروبات\n√")
        else:
            await m.reply_text("◍ هذا الامر للمطور الاساسي فقط\n√")
            return

    if m.text == "حذف داتابيز قفل الدردشه":
        if sudo(m):
            drop_db_locktext()
            await m.reply_text("◍ تم حذف الجدول الخاص بالدردشه\n√")
        else:
            await m.reply_text("◍ هذا الامر للمطور الاساسي فقط\n√")
            return

    if m.text == "حذف داتابيز الانتظار":
        if sudo(m):
            drop_db_wait()
            drop_db_waitq()
            await m.reply_text("◍ تم حذف الجدول الخاص بالانتظار\n√")
        else:
            await m.reply_text("◍ هذا الامر للمطور الاساسي فقط\n√")
            return


########################################################################################################################
########################################################################################################################

    if re.match("^قول (.*)$", str(m.text)):
        await echo_text(m)
        return

    if re.match("^انطق (.*)$", str(m.text)):
        await say_text(m)
        return

    if m.text == "فتح الردود":
        if admin(m):
            await lock_lockreply_open(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    if m.text == "قفل الردود":
        if admin(m):
            await lock_lockreply_close(m)
        else:
            await m.reply_text("◍ يجب ان تكون برتبه ادمن على الاقل لاستخدام هذا الامر\n√")
            return

    if await lock_lockreply_test(m):
        await allreply_for_bot(c, m)
        return


########################################################################################################################
########################################################################################################################

from pyrogram import enums
from pyrogram.types import Message
from database import *


########################################################################################################################
########################################################################################################################
from plugins.welcome_bye_laws import lock_lockwelcome_test, lock_lockbye_test


async def lock_chat_open(m: Message):
    del_db_locktext(m.chat.id)
    await m.reply_text("◍ تم فتح الدردشه\n√")


async def lock_chat_close(m: Message):
    if get_db_locktext(m.chat.id) is None:
        set_db_locktext("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الدردشه\n√")
        return
    else:
        for per in get_db_locktext(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ الدردشه مقفوله بالفعل\n√")
                return
        set_db_locktext("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الدردشه\n√")
        return


def lock_chat_test(m: Message):
    leader = False
    if get_db_locktext(m.chat.id) is None:
        leader = False
    else:
        for per in get_db_locktext(m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def lock_mnshn_open(m: Message):
    del_db_lockmnshn(m.chat.id)
    await m.reply_text("◍ تم فتح المنشن فى الروم\n√")


async def lock_mnshn_close(m: Message):
    if get_db_lockmnshn(m.chat.id) is None:
        set_db_lockmnshn("yes", m.chat.id)
        await m.reply_text("◍ تم قفل المنشن فى الروم\n√")
        return
    else:
        for per in get_db_lockmnshn(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ المنشن مقفول بالفعل\n√")
                return
        set_db_lockmnshn("yes", m.chat.id)
        await m.reply_text("◍ تم قفل المنشن فى الروم\n√")
        return


def lock_mnshn_test(m: Message):
    leader = False
    if get_db_lockmnshn(m.chat.id) is None:
        leader = False
    else:
        for per in get_db_lockmnshn(m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def lock_link_open(m: Message):
    del_db_locklink(m.chat.id)
    await m.reply_text("◍ تم فتح الروابط فى الروم\n√")


async def lock_link_close(m: Message):
    if get_db_locklink(m.chat.id) is None:
        set_db_locklink("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الروابط فى الروم\n√")
        return
    else:
        for per in get_db_locklink(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ الروابط مقفوله بالفعل\n√")
                return
        set_db_locklink("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الروابط فى الروم\n√")
        return


def lock_link_test(m: Message):
    leader = False
    if get_db_locklink(m.chat.id) is None:
        leader = False
    else:
        for per in get_db_locklink(m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


async def lock_link_ban_open(m: Message):
    del_db_locklink_ban(m.chat.id)
    await m.reply_text("◍ تم فتح الروابط بالطرد فى الروم\n√")


async def lock_link_close_ban(m: Message):
    if get_db_locklink_ban(m.chat.id) is None:
        set_db_locklink_ban("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الروابط بالطرد فى الروم\n√")
        return
    else:
        for per in get_db_locklink_ban(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ الروابط بالطرد مقفوله بالفعل")
                return
        set_db_locklink_ban("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الروابط بالطرد فى الروم\n√")
        return


def lock_link_ban_test(m: Message):
    leader = False
    if get_db_locklink_ban(m.chat.id) is None:
        leader = False
    else:
        for per in get_db_locklink_ban(m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


async def lock_link_mute_open(m: Message):
    del_db_locklink_mute(m.chat.id)
    await m.reply_text("◍ تم فتح الروابط بالكتم فى الروم\n√")


async def lock_link_close_mute(m: Message):
    if get_db_locklink_mute(m.chat.id) is None:
        set_db_locklink_mute("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الروابط بالكتم فى الروم\n√")
        return
    else:
        for per in get_db_locklink_mute(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ الروابط بالكتم مقفوله بالفعل")
                return
        set_db_locklink_mute("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الروابط بالكتم فى الروم\n√")
        return


def lock_link_mute_test(m: Message):
    leader = False
    if get_db_locklink_mute(m.chat.id) is None:
        leader = False
    else:
        for per in get_db_locklink_mute(m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def lock_photo_open(m: Message):
    del_db_lockphoto(m.chat.id)
    await m.reply_text("◍ تم فتح الصور فى الروم\n√")


async def lock_photo_close(m: Message):
    if get_db_lockphoto(m.chat.id) is None:
        set_db_lockphoto("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الصور فى الروم\n√")
        return
    else:
        for per in get_db_lockphoto(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ الصور مقفوله بالفعل\n√")
                return
        set_db_lockphoto("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الصور فى الروم\n√")
        return


def lock_photo_test(m: Message):
    leader = False
    if get_db_lockphoto(m.chat.id) is None:
        leader = False
    else:
        for per in get_db_lockphoto(m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def lock_video_open(m: Message):
    del_db_lockvideo(m.chat.id)
    await m.reply_text("◍ تم فتح الفديوهات فى الروم\n√")


async def lock_video_close(m: Message):
    if get_db_lockvideo(m.chat.id) is None:
        set_db_lockvideo("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الفديوهات فى الروم\n√")
        return
    else:
        for per in get_db_lockvideo(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ الفديوهات مقفوله بالفعل\n√")
                return
        set_db_lockvideo("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الفديوهات فى الروم\n√")
        return


def lock_video_test(m: Message):
    leader = False
    if get_db_lockvideo(m.chat.id) is None:
        leader = False
    else:
        for per in get_db_lockvideo(m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def lock_sticker_open(m: Message):
    del_db_locksticker(m.chat.id)
    await m.reply_text("◍ تم فتح الاستيكر فى الروم\n√")


async def lock_sticker_close(m: Message):
    if get_db_locksticker(m.chat.id) is None:
        set_db_locksticker("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الاستيكر فى الروم\n√")
        return
    else:
        for per in get_db_locksticker(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ الاستيكر مقفوله بالفعل\n√")
                return
        set_db_locksticker("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الاستيكر فى الروم\n√")
        return


def lock_sticker_test(m: Message):
    leader = False
    if get_db_locksticker(m.chat.id) is None:
        leader = False
    else:
        for per in get_db_locksticker(m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def lock_animation_open(m: Message):
    del_db_lockanimation(m.chat.id)
    await m.reply_text("◍ تم فتح الاستيكر فى الروم\n√")


async def lock_animation_close(m: Message):
    if get_db_lockanimation(m.chat.id) is None:
        set_db_lockanimation("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الاستيكر فى الروم\n√")
        return
    else:
        for per in get_db_lockanimation(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ الاستيكر مقفوله بالفعل\n√")
                return
        set_db_lockanimation("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الاستيكر فى الروم\n√")
        return


def lock_animation_test(m: Message):
    leader = False
    if get_db_lockanimation(m.chat.id) is None:
        leader = False
    else:
        for per in get_db_lockanimation(m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def lock_audio_open(m: Message):
    del_db_lockaudio(m.chat.id)
    await m.reply_text("◍ تم فتح الصوت فى الروم\n√")


async def lock_audio_close(m: Message):
    if get_db_lockaudio(m.chat.id) is None:
        set_db_lockaudio("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الصوت فى الروم\n√")
        return
    else:
        for per in get_db_lockaudio(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ الصوت مقفوله بالفعل\n√")
                return
        set_db_lockaudio("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الصوت فى الروم\n√")
        return


def lock_audio_test(m: Message):
    leader = False
    if get_db_lockaudio(m.chat.id) is None:
        leader = False
    else:
        for per in get_db_lockaudio(m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def lock_voice_open(m: Message):
    del_db_lockvoice(m.chat.id)
    await m.reply_text("◍ تم فتح الريكوردات فى الروم\n√")


async def lock_voice_close(m: Message):
    if get_db_lockvoice(m.chat.id) is None:
        set_db_lockvoice("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الريكوردات فى الروم\n√")
        return
    else:
        for per in get_db_lockvoice(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ الريكورد مقفول بالفعل\n√")
                return
        set_db_lockvoice("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الريكوردات فى الروم\n√")
        return


def lock_voice_test(m: Message):
    leader = False
    if get_db_lockvoice(m.chat.id) is None:
        leader = False
    else:
        for per in get_db_lockvoice(m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def lock_forward_open(m: Message):
    del_db_lockforward(m.chat.id)
    await m.reply_text("◍ تم فتح التوجيه فى الروم\n√")


async def lock_forward_close(m: Message):
    if get_db_lockforward(m.chat.id) is None:
        set_db_lockforward("yes", m.chat.id)
        await m.reply_text("◍ تم قفل التوجيه فى الروم\n√")
        return
    else:
        for per in get_db_lockforward(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ التوجيه مقفول بالفعل\n√")
                return
        set_db_lockforward("yes", m.chat.id)
        await m.reply_text("◍ تم قفل التوجيه فى الروم\n√")
        return


def lock_forward_test(m: Message):
    leader = False
    if get_db_lockforward(m.chat.id) is None:
        leader = False
    else:
        for per in get_db_lockforward(m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


async def lock_forward_open_ban(m: Message):
    del_db_lockforward_ban(m.chat.id)
    await m.reply_text("◍ تم فتح التوجيه بالطرد فى الروم\n√")


async def lock_forward_close_ban(m: Message):
    if get_db_lockforward_ban(m.chat.id) is None:
        set_db_lockforward_ban("yes", m.chat.id)
        await m.reply_text("◍ تم قفل التوجيه بالطرد فى الروم\n√")
        return
    else:
        for per in get_db_lockforward_ban(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ التوجيه بالطرد مقفول بالفعل\n√")
                return
        set_db_lockforward_ban("yes", m.chat.id)
        await m.reply_text("◍ تم قفل التوجيه بالطرد فى الروم\n√")
        return


def lock_forward_test_ban(m: Message):
    leader = False
    if get_db_lockforward_ban(m.chat.id) is None:
        leader = False
    else:
        for per in get_db_lockforward_ban(m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


async def lock_forward_open_mute(m: Message):
    del_db_lockforward_mute(m.chat.id)
    await m.reply_text("◍ تم فتح التوجيه بالكتم فى الروم\n√")


async def lock_forward_close_mute(m: Message):
    if get_db_lockforward_mute(m.chat.id) is None:
        set_db_lockforward_mute("yes", m.chat.id)
        await m.reply_text("◍ تم قفل التوجيه بالكتم فى الروم\n√")
        return
    else:
        for per in get_db_lockforward_mute(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ التوجيه بالكتم مقفول بالفعل\n√")
                return
        set_db_lockforward_mute("yes", m.chat.id)
        await m.reply_text("◍ تم قفل التوجيه بالكتم فى الروم\n√")
        return


def lock_forward_test_mute(m: Message):
    leader = False
    if get_db_lockforward_mute(m.chat.id) is None:
        leader = False
    else:
        for per in get_db_lockforward_mute(m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def lock_document_open(m: Message):
    del_db_lockdocument(m.chat.id)
    await m.reply_text("◍ تم فتح الملفات فى الروم\n√")


async def lock_document_close(m: Message):
    if get_db_lockdocument(m.chat.id) is None:
        set_db_lockdocument("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الملفات فى الروم\n√")
        return
    else:
        for per in get_db_lockdocument(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ الملفات مقفول بالفعل\n√")
                return
        set_db_lockdocument("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الملفات فى الروم\n√")
        return


def lock_document_test(m: Message):
    leader = False
    if get_db_lockdocument(m.chat.id) is None:
        leader = False
    else:
        for per in get_db_lockdocument(m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def lock_contact_open(m: Message):
    del_db_lockcontact(m.chat.id)
    await m.reply_text("◍ تم فتح جهات الاتصال فى الروم\n√")


async def lock_contact_close(m: Message):
    if get_db_lockcontact(m.chat.id) is None:
        set_db_lockcontact("yes", m.chat.id)
        await m.reply_text("◍ تم قفل جهات الاتصال فى الروم\n√")
        return
    else:
        for per in get_db_lockcontact(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ جهات الاتصال مقفوله بالفعل\n√")
                return
        set_db_lockcontact("yes", m.chat.id)
        await m.reply_text("◍ تم قفل جهات الاتصال فى الروم\n√")
        return


def lock_contact_test(m: Message):
    leader = False
    if get_db_lockcontact(m.chat.id) is None:
        leader = False
    else:
        for per in get_db_lockcontact(m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def lock_fshar_open(m: Message):
    del_db_lockfshar(m.chat.id)
    await m.reply_text("◍ تم فتح الفشار فى الروم\n√")


async def lock_fshar_close(m: Message):
    if get_db_lockfshar(m.chat.id) is None:
        set_db_lockfshar("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الفشار فى الروم\n√")
        return
    else:
        for per in get_db_lockfshar(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ الفشار مقفول بالفعل\n√")
                return
        set_db_lockfshar("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الفشار فى الروم\n√")
        return


def lock_fshar_test(m: Message):
    leader = False
    if get_db_lockfshar(m.chat.id) is None:
        leader = False
    else:
        for per in get_db_lockfshar(m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


async def lock_fshar_open_ban(m: Message):
    del_db_lockfshar_ban(m.chat.id)
    await m.reply_text("◍ تم فتح الفشار بالطرد فى الروم\n√")


async def lock_fshar_close_ban(m: Message):
    if get_db_lockfshar_ban(m.chat.id) is None:
        set_db_lockfshar_ban("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الفشار بالطرد فى الروم\n√")
        return
    else:
        for per in get_db_lockfshar_ban(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ الفشار بالطرد مقفول بالفعل\n√")
                return
        set_db_lockfshar_ban("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الفشار بالطرد فى الروم\n√")
        return


def lock_fshar_test_ban(m: Message):
    leader = False
    if get_db_lockfshar_ban(m.chat.id) is None:
        leader = False
    else:
        for per in get_db_lockfshar_ban(m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


async def lock_fshar_open_mute(m: Message):
    del_db_lockfshar_mute(m.chat.id)
    await m.reply_text("◍ تم فتح الفشار بالكتم فى الروم\n√")


async def lock_fshar_close_mute(m: Message):
    if get_db_lockfshar_mute(m.chat.id) is None:
        set_db_lockfshar_mute("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الفشار بالكتم فى الروم\n√")
        return
    else:
        for per in get_db_lockfshar_mute(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ الفشار بالكتم مقفول بالفعل\n√")
                return
        set_db_lockfshar_mute("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الفشار بالكتم فى الروم\n√")
        return


def lock_fshar_test_mute(m: Message):
    leader = False
    if get_db_lockfshar_mute(m.chat.id) is None:
        leader = False
    else:
        for per in get_db_lockfshar_mute(m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def lock_zhrafa_open(m: Message):
    del_db_lockzhrafa(m.chat.id)
    await m.reply_text("◍ تم فتح الزخرفه فى الروم\n√")


async def lock_zhrafa_close(m: Message):
    if get_db_lockzhrafa(m.chat.id) is None:
        set_db_lockzhrafa("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الزخرفه فى الروم\n√")
        return
    else:
        for per in get_db_lockzhrafa(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ الزخرفه مقفوله بالفعل\n√")
                return
        set_db_lockzhrafa("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الزخرفه فى الروم\n√")
        return


async def lock_zhrafa_test(m: Message):
    leader = False
    if get_db_lockzhrafa(m.chat.id) is None:
        leader = False
    else:
        for per in get_db_lockzhrafa(m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def lock_music_open(m: Message):
    del_db_lockmusic(m.chat.id)
    await m.reply_text("◍ تم فتح الاغاني فى الروم\n√")


async def lock_music_close(m: Message):
    if get_db_lockmusic(m.chat.id) is None:
        set_db_lockmusic("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الاغاني فى الروم\n√")
        return
    else:
        for per in get_db_lockmusic(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ الاغاني مقفوله بالفعل\n√")
                return
        set_db_lockmusic("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الاغاني فى الروم\n√")
        return


async def lock_music_test(m: Message):
    leader = False
    if get_db_lockmusic(m.chat.id) is None:
        leader = False
    else:
        for per in get_db_lockmusic(m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def lock_aflam_open(m: Message):
    del_db_lockaflam(m.chat.id)
    await m.reply_text("◍ تم فتح الافلام فى الروم\n√")


async def lock_aflam_close(m: Message):
    if get_db_lockaflam(m.chat.id) is None:
        set_db_lockaflam("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الافلام فى الروم\n√")
        return
    else:
        for per in get_db_lockaflam(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ الافلام مقفوله بالفعل\n√")
                return
        set_db_lockaflam("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الافلام فى الروم\n√")
        return


async def lock_aflam_test(m: Message):
    leader = False
    if get_db_lockaflam(m.chat.id) is None:
        leader = False
    else:
        for per in get_db_lockaflam(m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def lock_youtube_open(m: Message):
    del_db_lockyoutube(m.chat.id)
    await m.reply_text("◍ تم فتح اليوتيوب فى الروم\n√")


async def lock_youtube_close(m: Message):
    if get_db_lockyoutube(m.chat.id) is None:
        set_db_lockyoutube("yes", m.chat.id)
        await m.reply_text("◍ تم قفل اليوتيوب فى الروم\n√")
        return
    else:
        for per in get_db_lockyoutube(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ اليوتيوب مقفول بالفعل\n√")
                return
        set_db_lockyoutube("yes", m.chat.id)
        await m.reply_text("◍ تم قفل اليوتيوب فى الروم\n√")
        return


async def lock_youtube_test(m: Message):
    leader = False
    if get_db_lockyoutube(m.chat.id) is None:
        leader = False
    else:
        for per in get_db_lockyoutube(m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################


async def lock_translate_open(m: Message):
    del_db_locktranslate(m.chat.id)
    await m.reply_text("◍ تم فتح الترجمه فى الروم\n√")


async def lock_translate_close(m: Message):
    if get_db_locktranslate(m.chat.id) is None:
        set_db_locktranslate("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الترجمه فى الروم\n√")
        return
    else:
        for per in get_db_locktranslate(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ الترجمه مقفوله بالفعل\n√")
                return
        set_db_locktranslate("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الترجمه فى الروم\n√")
        return


async def lock_translate_test(m: Message):
    leader = False
    if get_db_locktranslate(m.chat.id) is None:
        leader = False
    else:
        for per in get_db_locktranslate(m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################

def lock_blocktext_test(m):
    leader = False
    if get_db_blocktext(m.chat.id) is None:
        leader = False
    else:
        for rp in get_db_blocktext(m.chat.id):
            if m.new_chat_members or m.left_chat_member:
                leader = False
            else:
                if m.text:
                    if rp[0] in m.text:
                        leader = True
                else:
                    leader = False
    return leader


async def lock_blocktext_open_ban(m: Message):
    del_db_blocktext_ban(m.chat.id)
    await m.reply_text("◍ تم فتح الكلمات الممنوعه بالطرد فى الروم\n√")


async def lock_blocktext_close_ban(m: Message):
    if get_db_blocktext_ban(m.chat.id) is None:
        set_db_blocktext_ban("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الكلمات الممنوعه بالطرد فى الروم\n√")
        return
    else:
        for per in get_db_blocktext_ban(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ الكلمات الممنوعه مقفوله بالطرد بالفعل\n√")
                return
        set_db_blocktext_ban("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الكلمات الممنوعه بالطرد فى الروم\n√")
        return


def lock_blocktext_test_ban(m):
    leader = False
    if get_db_blocktext(m.chat.id) is None:
        leader = False
    else:
        if get_db_blocktext_ban(m.chat.id) is None:
            leader = False
        else:
            for per in get_db_blocktext_ban(m.chat.id):
                if per[0] == "yes":
                    for rp in get_db_blocktext(m.chat.id):
                        if m.new_chat_members or m.left_chat_member:
                            leader = False
                        else:
                            if rp[0] in m.text:
                                leader = True
    return leader


async def lock_blocktext_open_mute(m: Message):
    del_db_blocktext_mute(m.chat.id)
    await m.reply_text("◍ تم فتح الكلمات الممنوعه بالكتم فى الروم\n√")


async def lock_blocktext_close_mute(m: Message):
    if get_db_blocktext_mute(m.chat.id) is None:
        set_db_blocktext_mute("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الكلمات الممنوعه بالكتم فى الروم\n√")
        return
    else:
        for per in get_db_blocktext_mute(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ الكلمات الممنوعه مقفوله بالكتم بالفعل\n√")
                return
        set_db_blocktext_mute("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الكلمات الممنوعه بالكتم فى الروم\n√")
        return


def lock_blocktext_test_mute(m):
    leader = False
    if get_db_blocktext(m.chat.id) is None:
        leader = False
    else:
        if get_db_blocktext_mute(m.chat.id) is None:
            leader = False
        else:
            for per in get_db_blocktext_mute(m.chat.id):
                if per[0] == "yes":
                    for rp in get_db_blocktext(m.chat.id):
                        if m.new_chat_members or m.left_chat_member:
                            leader = False
                        else:
                            if rp[0] in m.text:
                                leader = True
    return leader


########################################################################################################################
########################################################################################################################

async def lock_notification_open(m: Message):
    del_db_locknotification(m.chat.id)
    await m.reply_text("◍ تم فتح الاشعارات فى الروم\n√")


async def lock_notification_close(m: Message):
    if get_db_locknotification(m.chat.id) is None:
        set_db_locknotification("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الاشعارات فى الروم\n√")
        return
    else:
        for per in get_db_locknotification(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ الاشعارات مقفوله بالفعل\n√")
                return
        set_db_locknotification("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الاشعارات فى الروم\n√")
        return


def lock_notification_test(m: Message):
    leader = False
    if get_db_locknotification(m.chat.id) is None:
        leader = False
    else:
        for per in get_db_locknotification(m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def lock_upp_open(m: Message):
    del_db_lockupper(m.chat.id)
    await m.reply_text("◍ تم فتح الرفع فى الروم\n√")


async def lock_upp_close(m: Message):
    if get_db_lockupper(m.chat.id) is None:
        set_db_lockupper("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الرفع فى الروم\n√")
        return
    else:
        for per in get_db_lockupper(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ الرفع مقفول بالفعل\n√")
                return
        set_db_lockupper("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الرفع فى الروم\n√")
        return


def lock_upp_test(m: Message):
    leader = False
    if get_db_lockupper(m.chat.id) is None:
        leader = False
    else:
        for per in get_db_lockupper(m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def lock_azkar_open(m: Message):
    del_db_lock("lockazkar", m.chat.id)
    await m.reply_text("◍ تم فتح الاذكار فى الروم\n√")


async def lock_azkar_close(m: Message):
    if get_db_lock("lockazkar", m.chat.id) is None:
        set_db_lock("lockazkar", "yes", m.chat.id)
        await m.reply_text("◍ تم قفل الاذكار فى الروم\n√")
        return
    else:
        for per in get_db_lock("lockazkar", m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ الاذكار مقفوله بالفعل\n√")
                return
        set_db_lock("lockazkar", "yes", m.chat.id)
        await m.reply_text("◍ تم قفل الاذكار فى الروم\n√")
        return


def lock_azkar_test(m: Message):
    leader = False
    if get_db_lock("lockazkar", m.chat.id) is None:
        leader = False
    else:
        for per in get_db_lock("lockazkar", m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


async def lock_azkar2_open(m: Message):
    del_db_lock("lockazkar2", m.chat.id)


async def lock_azkar2_close(m: Message):
    if get_db_lock("lockazkar2", m.chat.id) is None:
        set_db_lock("lockazkar2", "yes", m.chat.id)
    else:
        for per in get_db_lock("lockazkar2", m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ الاذكار مقفوله بالفعل\n√")
                return
        set_db_lock("lockazkar2", "yes", m.chat.id)


def lock_azkar2_test(m: Message):
    leader = False
    if get_db_lock("lockazkar2", m.chat.id) is None:
        leader = False
    else:
        for per in get_db_lock("lockazkar2", m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def lock_games_open(m: Message):
    if not get_db_lockgames(m.chat.id):
        await m.reply_text("◍ الالعاب مفتوحه بالفعل\n√")
    else:
        del_db_lockgames(m.chat.id)
        await m.reply_text("◍ تم فتح الالعاب فى الروم\n√")
        return


async def lock_games_close(m: Message):
    if get_db_lockgames(m.chat.id):
        await m.reply_text("◍ الالعاب مقفوله بالفعل\n√")
    else:
        set_db_lockgames("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الالعاب فى الروم\n√")
        return


def lock_games_test(m: Message):
    leader = False
    if not get_db_lockgames(m.chat.id):
        leader = False
    else:
        leader = True
    return leader


########################################################################################################################
########################################################################################################################

async def lock_tag_open(m: Message):
    del_db_locktag(m.chat.id)
    await m.reply_text("◍ تم فتح التاج فى الروم\n√")


async def lock_tag_close(m: Message):
    if get_db_locktag(m.chat.id) is None:
        set_db_locktag("yes", m.chat.id)
        await m.reply_text("◍ تم قفل التاج فى الروم\n√")
        return
    else:
        for per in get_db_locktag(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ التاج مقفول بالفعل\n√")
                return
        set_db_locktag("yes", m.chat.id)
        await m.reply_text("◍ تم قفل التاج فى الروم\n√")
        return


def lock_tag_test(m: Message):
    leader = False
    if get_db_locktag(m.chat.id) is None:
        leader = False
    else:
        for per in get_db_locktag(m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def lock_meendafny_open(m: Message):
    del_db_lockmeendafny(m.chat.id)
    await m.reply_text("◍ تم فتح مين ضافني\n√")


async def lock_meendafny_close(m: Message):
    if get_db_lockmeendafny(m.chat.id) is None:
        set_db_lockmeendafny("yes", m.chat.id)
        await m.reply_text("◍ تم قفل مين ضافني\n√")
        return
    else:
        for per in get_db_lockmeendafny(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ مين ضافني مقفوله بالفعل\n√")
                return
        set_db_lockmeendafny("yes", m.chat.id)
        await m.reply_text("◍ تم قفل مين ضافني\n√")
        return


def lock_meendafny_test(m: Message):
    leader = False
    if get_db_lockmeendafny(m.chat.id) is None:
        leader = False
    else:
        for per in get_db_lockmeendafny(m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def lock_rwayat_open(m: Message):
    del_db_lockrwayat(m.chat.id)
    await m.reply_text("◍ تم فتح الروايات فى الروم\n√")


async def lock_rwayat_close(m: Message):
    if get_db_lockrwayat(m.chat.id) is None:
        set_db_lockrwayat("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الروايات فى الروم\n√")
        return
    else:
        for per in get_db_lockrwayat(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ الروايات مقفوله بالفعل\n√")
                return
        set_db_lockrwayat("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الروايات فى الروم\n√")
        return


def lock_rwayat_test(m: Message):
    leader = False
    if get_db_lockrwayat(m.chat.id) is None:
        leader = False
    else:
        for per in get_db_lockrwayat(m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def lock_namemeaning_open(m: Message):
    del_db_lock("namemeaning", m.chat.id)
    await m.reply_text("◍ تم فتح معاني الاسماء فى الروم\n√")


async def lock_namemeaning_close(m: Message):
    if get_db_lock("namemeaning", m.chat.id) is None:
        set_db_lock("namemeaning", "yes", m.chat.id)
        await m.reply_text("◍ تم قفل معاني الاسماء فى الروم\n√")
        return
    else:
        for per in get_db_lock("namemeaning", m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ معاني الاسماء مقفوله بالفعل\n√")
                return
        set_db_lock("namemeaning", "yes", m.chat.id)
        await m.reply_text("◍ تم قفل معاني الاسماء فى الروم\n√")
        return


def lock_namemeaning_test(m: Message):
    leader = False
    if get_db_lock("namemeaning", m.chat.id) is None:
        leader = False
    else:
        for per in get_db_lock("namemeaning", m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def lock_abrag_open(m: Message):
    del_db_lock("abrag", m.chat.id)
    await m.reply_text("◍ تم فتح الابراج فى الروم\n√")


async def lock_abrag_close(m: Message):
    if get_db_lock("abrag", m.chat.id) is None:
        set_db_lock("abrag", "yes", m.chat.id)
        await m.reply_text("◍ تم قفل الابراج فى الروم\n√")
        return
    else:
        for per in get_db_lock("abrag", m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ الابراج مقفوله بالفعل\n√")
                return
        set_db_lock("abrag", "yes", m.chat.id)
        await m.reply_text("◍ تم قفل الابراج فى الروم\n√")
        return


def lock_abrag_test(m: Message):
    leader = False
    if get_db_lock("abrag", m.chat.id) is None:
        leader = False
    else:
        for per in get_db_lock("abrag", m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def lock_linggroup_open(m: Message):
    del_db_lock("locklinggroup", m.chat.id)
    await m.reply_text("◍ تم فتح الرابط فى الروم\n√")


async def lock_linggroup_close(m: Message):
    if get_db_lock("locklinggroup", m.chat.id) is None:
        set_db_lock("locklinggroup", "yes", m.chat.id)
        await m.reply_text("◍ تم قفل الرابط فى الروم\n√")
        return
    else:
        for per in get_db_lock("locklinggroup", m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ الرابط مقفول بالفعل\n√")
                return
        set_db_lock("locklinggroup", "yes", m.chat.id)
        await m.reply_text("◍ تم قفل الرابط فى الروم\n√")
        return


def lock_linggroup_test(m: Message):
    leader = False
    if get_db_lock("locklinggroup", m.chat.id) is None:
        leader = False
    else:
        for per in get_db_lock("locklinggroup", m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def lock_idgroup_open(m: Message):
    del_db_lock("idgroup", m.chat.id)
    await m.reply_text("◍ تم فتح الايدي فى الروم\n√")


async def lock_idgroup_close(m: Message):
    if get_db_lock("idgroup", m.chat.id) is None:
        set_db_lock("idgroup", "yes", m.chat.id)
        await m.reply_text("◍ تم قفل الايدي فى الروم\n√")
        return
    else:
        for per in get_db_lock("idgroup", m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ الايدي مقفول بالفعل\n√")
                return
        set_db_lock("idgroup", "yes", m.chat.id)
        await m.reply_text("◍ تم قفل الايدي فى الروم\n√")
        return


def lock_idgroup_test(m: Message):
    leader = False
    if get_db_lock("idgroup", m.chat.id) is None:
        leader = False
    else:
        for per in get_db_lock("idgroup", m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def lock_idgroup2_open(m: Message):
    del_db_lock("idgroup2", m.chat.id)
    await m.reply_text("◍ تم فتح الايدي بالصوره فى الروم\n√")


async def lock_idgroup2_close(m: Message):
    if get_db_lock("idgroup2", m.chat.id) is None:
        set_db_lock("idgroup2", "yes", m.chat.id)
        await m.reply_text("◍ تم قفل الايدي بالصوره فى الروم\n√")
        return
    else:
        for per in get_db_lock("idgroup2", m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ الايدي بالصوره مقفول بالفعل\n√")
                return
        set_db_lock("idgroup2", "yes", m.chat.id)
        await m.reply_text("◍ تم قفل الايدي بالصوره فى الروم\n√")
        return


def lock_idgroup2_test(m: Message):
    leader = False
    if get_db_lock("idgroup2", m.chat.id) is None:
        leader = False
    else:
        for per in get_db_lock("idgroup2", m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def lock_myphoto_open(m: Message):
    del_db_lock("myphoto", m.chat.id)
    await m.reply_text("◍ تم فتح صورتي فى الروم\n√")


async def lock_myphoto_close(m: Message):
    if get_db_lock("myphoto", m.chat.id) is None:
        set_db_lock("myphoto", "yes", m.chat.id)
        await m.reply_text("◍ تم قفل صورتي فى الروم\n√")
        return
    else:
        for per in get_db_lock("myphoto", m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ صورتي مقفوله بالفعل\n√")
                return
        set_db_lock("myphoto", "yes", m.chat.id)
        await m.reply_text("◍ تم قفل صورتي فى الروم\n√")
        return


def lock_myphoto_test(m: Message):
    leader = False
    if get_db_lock("myphoto", m.chat.id) is None:
        leader = False
    else:
        for per in get_db_lock("myphoto", m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def lock_entrygp_open(m: Message):
    del_db_lock("entrygp", m.chat.id)
    await m.reply_text("◍ تم فتح الدخول فى الروم\n√")


async def lock_entrygp_close(m: Message):
    if get_db_lock("entrygp", m.chat.id) is None:
        set_db_lock("entrygp", "yes", m.chat.id)
        await m.reply_text("◍ تم قفل الدخول فى الروم\n√")
        return
    else:
        for per in get_db_lock("entrygp", m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ الدخول مقفول بالفعل\n√")
                return
        set_db_lock("entrygp", "yes", m.chat.id)
        await m.reply_text("◍ تم قفل الدخول فى الروم\n√")
        return


def lock_entrygp_test(m: Message):
    leader = False
    if get_db_lock("entrygp", m.chat.id) is None:
        leader = False
    else:
        for per in get_db_lock("entrygp", m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def openallthings(m):
    del_db_locktext(m.chat.id)
    del_db_lockmnshn(m.chat.id)
    del_db_locklink(m.chat.id)
    del_db_locklink_ban(m.chat.id)
    del_db_locklink_mute(m.chat.id)
    del_db_lockphoto(m.chat.id)
    del_db_lockvideo(m.chat.id)
    del_db_locksticker(m.chat.id)
    del_db_lockanimation(m.chat.id)
    del_db_lockaudio(m.chat.id)
    del_db_lockvoice(m.chat.id)
    del_db_lockforward(m.chat.id)
    del_db_lockforward_ban(m.chat.id)
    del_db_lockforward_mute(m.chat.id)
    del_db_lockdocument(m.chat.id)
    del_db_lockcontact(m.chat.id)
    del_db_lockfshar(m.chat.id)
    del_db_lockfshar_ban(m.chat.id)
    del_db_lockfshar_mute(m.chat.id)
    del_db_lockzhrafa(m.chat.id)
    del_db_lockmusic(m.chat.id)
    del_db_lockaflam(m.chat.id)
    del_db_lockyoutube(m.chat.id)
    del_db_locktranslate(m.chat.id)
    del_db_blocktext_ban(m.chat.id)
    del_db_blocktext_mute(m.chat.id)
    del_db_lockupper(m.chat.id)
    del_db_lockgames(m.chat.id)
    del_db_lock("lockazkar", m.chat.id)
    del_db_locknotification(m.chat.id)
    del_db_locktag(m.chat.id)
    del_db_lockmeendafny(m.chat.id)
    del_db_lockmeendafny(m.chat.id)
    del_db_lockrwayat(m.chat.id)
    del_db_lock("namemeaning", m.chat.id)
    del_db_lock("abrag", m.chat.id)
    del_db_lock("locklinggroup", m.chat.id)
    del_db_lock("idgroup", m.chat.id)
    del_db_lock("entrygp", m.chat.id)
    del_db_lock("myphoto", m.chat.id)


async def closellthings(m):
    set_db_locktext("yes", m.chat.id)
    set_db_lockmnshn("yes", m.chat.id)
    set_db_locklink("yes", m.chat.id)
    set_db_lockphoto("yes", m.chat.id)
    set_db_lockvideo("yes", m.chat.id)
    set_db_locksticker("yes", m.chat.id)
    set_db_lockanimation("yes", m.chat.id)
    set_db_lockaudio("yes", m.chat.id)
    set_db_lockvoice("yes", m.chat.id)
    set_db_lockforward("yes", m.chat.id)
    set_db_lockdocument("yes", m.chat.id)
    set_db_lockcontact("yes", m.chat.id)
    set_db_lockfshar("yes", m.chat.id)
    set_db_lockzhrafa("yes", m.chat.id)
    set_db_lockmusic("yes", m.chat.id)
    set_db_lockaflam("yes", m.chat.id)
    set_db_lockyoutube("yes", m.chat.id)
    set_db_locktranslate("yes", m.chat.id)
    set_db_lockupper("yes", m.chat.id)
    set_db_lockgames("yes", m.chat.id)
    set_db_lock("lockazkar", "yes", m.chat.id)
    set_db_locknotification("yes", m.chat.id)
    set_db_locktag("yes", m.chat.id)
    set_db_lockmeendafny("yes", m.chat.id)
    set_db_lockrwayat("yes", m.chat.id)
    set_db_lock("namemeaning", "yes", m.chat.id)
    set_db_lock("abrag", "yes", m.chat.id)
    set_db_lock("locklinggroup", "yes", m.chat.id)
    set_db_lock("idgroup", "yes", m.chat.id)
    set_db_lock("myphoto", "yes", m.chat.id)


async def lock_openall(m: Message):
    a = await m.reply_text("◍ انتظر...\n√")
    await openallthings(m)
    await a.delete()
    await m.reply_text("◍ تم فتح جميع الاوامر فى الروم\n√")


async def lock_closeall(m: Message):
    a = await m.reply_text("◍ انتظر...\n√")
    await openallthings(m)
    await a.delete()
    b = await m.reply_text("◍ هانت اهي...\n√")
    await closellthings(m)
    await b.delete()
    await m.reply_text("◍ تم قفل جميع الاوامر فى الروم\n√")


########################################################################################################################
########################################################################################################################


async def lock_deletelink_open(m: Message):
    del_db_deletelink(m.chat.id)
    await m.reply_text("◍ تم قفل رابط الحذف\n√")


async def lock_deletelink_close(m: Message):
    if get_db_deletelink(m.chat.id) is None:
        set_db_deletelink("yes", m.chat.id)
        await m.reply_text("◍ تم فتح رابط الحذف\n√")
        return
    else:
        for per in get_db_deletelink(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ رابط الحذف مفتوح بالفعل\n√")
                return
        set_db_deletelink("yes", m.chat.id)
        await m.reply_text("◍ تم فتح رابط الحذف\n√")
        return


def lock_deletelink_test(m: Message):
    leader = False
    if get_db_deletelink(m.chat.id) is None:
        leader = False
    else:
        for per in get_db_deletelink(m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################


async def lock_kickme_open(m: Message):
    del_db_lockkickme(m.chat.id)
    await m.reply_text("◍ تم قفل اطردني واكتمني فى الجروب\n√")


async def lock_kickme_close(m: Message):
    if get_db_lockkickme(m.chat.id) is None:
        set_db_lockkickme("yes", m.chat.id)
        await m.reply_text("◍ تم فتح اطردني واكتمني\n√")
        return
    else:
        for per in get_db_lockkickme(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ اطردني او اكتمني مفتوحه بالفعل\n√")
                return
        set_db_lockkickme("yes", m.chat.id)
        await m.reply_text("◍ تم فتح اطردني واكتمني\n√")
        return


def lock_kickme_test(m: Message):
    leader = False
    if get_db_lockkickme(m.chat.id) is None:
        leader = False
    else:
        for per in get_db_lockkickme(m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def lock_kickbotatban_open(m: Message):
    del_db_lockkickbotatban(m.chat.id)
    await m.reply_text("◍ تم تعطيل وضع طرد البوتات بالحظر فى الجروب\n√")


async def lock_kickbotatban_close(m: Message):
    if get_db_lockkickbotatban(m.chat.id) is None:
        set_db_lockkickbotatban("yes", m.chat.id)
        await m.reply_text("◍ تم فتح وضع طرد البوتات بالحظر\n√")
        return
    else:
        for per in get_db_lockkickbotatban(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ وضع طرد البوتات بالحظر مفتوح بالفعل\n√")
                return
        set_db_lockkickbotatban("yes", m.chat.id)
        await m.reply_text("◍ تم فتح وضع طرد البوتات بالحظر\n√")
        return


def lock_kickbotatban_test(m: Message):
    leader = False
    if get_db_lockkickbotatban(m.chat.id) is None:
        leader = False
    else:
        for per in get_db_lockkickbotatban(m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def lock_all_test(m: Message):
    if lock_chat_test(m):
        chatlock = "✘"
    else:
        chatlock = "✓"
    if lock_mnshn_test(m):
        mnshnlock = "✘"
    else:
        mnshnlock = "✓"
    if lock_link_test(m):
        linklock = "✘"
    else:
        linklock = "✓"
    if lock_link_ban_test(m):
        linkbanlock = "✘"
    else:
        linkbanlock = "✓"
    if lock_link_mute_test(m):
        linkmutelock = "✘"
    else:
        linkmutelock = "✓"
    if lock_photo_test(m):
        photolock = "✘"
    else:
        photolock = "✓"
    if lock_video_test(m):
        videolock = "✘"
    else:
        videolock = "✓"
    if lock_sticker_test(m):
        stickerlock = "✘"
    else:
        stickerlock = "✓"
    if lock_animation_test(m):
        animationlock = "✘"
    else:
        animationlock = "✓"
    if lock_audio_test(m):
        audiolock = "✘"
    else:
        audiolock = "✓"
    if lock_voice_test(m):
        voicelock = "✘"
    else:
        voicelock = "✓"
    if lock_forward_test(m):
        forwardlock = "✘"
    else:
        forwardlock = "✓"
    if lock_forward_test_ban(m):
        forwardbanlock = "✘"
    else:
        forwardbanlock = "✓"
    if lock_forward_test_mute(m):
        forwardmutelock = "✘"
    else:
        forwardmutelock = "✓"
    if lock_document_test(m):
        documentlock = "✘"
    else:
        documentlock = "✓"
    if lock_contact_test(m):
        contactlock = "✘"
    else:
        contactlock = "✓"
    if lock_fshar_test(m):
        fsharlock = "✘"
    else:
        fsharlock = "✓"
    if lock_fshar_test_ban(m):
        fsharbanlock = "✘"
    else:
        fsharbanlock = "✓"
    if lock_fshar_test_mute(m):
        fsharmutelock = "✘"
    else:
        fsharmutelock = "✓"
    if await lock_zhrafa_test(m):
        zhrafalock = "✘"
    else:
        zhrafalock = "✓"
    if await lock_music_test(m):
        musiclock = "✘"
    else:
        musiclock = "✓"
    if await lock_aflam_test(m):
        aflamlock = "✘"
    else:
        aflamlock = "✓"
    if await lock_youtube_test(m):
        youtubelock = "✘"
    else:
        youtubelock = "✓"
    if await lock_translate_test(m):
        translatelock = "✘"
    else:
        translatelock = "✓"
    if lock_blocktext_test(m):
        blocktextlock = "✘"
    else:
        blocktextlock = "✓"
    if lock_blocktext_test_ban(m):
        blocktextbanlock = "✘"
    else:
        blocktextbanlock = "✓"
    if lock_blocktext_test_mute(m):
        blocktextmutelock = "✘"
    else:
        blocktextmutelock = "✓"
    if lock_notification_test(m):
        notificationlock = "✘"
    else:
        notificationlock = "✓"
    if lock_upp_test(m):
        upplock = "✘"
    else:
        upplock = "✓"
    if lock_azkar_test(m):
        azkarlock = "✘"
    else:
        azkarlock = "✓"
    if lock_games_test(m):
        gameslock = "✘"
    else:
        gameslock = "✓"
    if lock_tag_test(m):
        taglock = "✘"
    else:
        taglock = "✓"
    if lock_meendafny_test(m):
        meendafnylock = "✘"
    else:
        meendafnylock = "✓"
    if lock_rwayat_test(m):
        rwayatlock = "✘"
    else:
        rwayatlock = "✓"
    if lock_deletelink_test(m):
        deletelinklock = "✓"
    else:
        deletelinklock = "✘"
    if lock_kickme_test(m):
        kickmelock = "✓"
    else:
        kickmelock = "✘"
    if lock_kickbotatban_test(m):
        kickbotatban = "✓"
    else:
        kickbotatban = "✘"
    if lock_namemeaning_test(m):
        namemeaning = "✘"
    else:
        namemeaning = "✓"
    if lock_abrag_test(m):
        abrag = "✘"
    else:
        abrag = "✓"
    if lock_lockwelcome_test(m):
        welcome = "✓"
    else:
        welcome = "✘"
    if lock_lockbye_test(m):
        bye = "✓"
    else:
        bye = "✘"
    textmessage = f"""
    ⚙️┇اعدادات الجروب ⇊
    ٴ━━━━━━━━━━━━
    ☑️┇  علامة ال ❬ ✓ ❭ تعني مفتوح
    ❌┇  علامة ال ❬ ✘ ❭ تعني مقفول
    ٴ━━━━━━━━━━━━
    💬┇ الدردشه » {chatlock}
    🌀┇ المعرفات » {mnshnlock}
    🖼️┇ الصور » {photolock}
    📽️┇ الفديوهات » {videolock}
    📣┇ الصوت » {audiolock}
    🎤┇ الريكورد » {voicelock}
    🏷️┇ الاستيكر » {stickerlock}
    ⛓️┇ المتحركه » {animationlock}
    🗂️┇ الوسائط » {documentlock}
    👁️‍🗨️┇ الاشعارات » {notificationlock}
    📻┇ الجهات » {contactlock}
    👋┇ الترحيب » {welcome}
    🦵┇ المغادره » {bye}
    ٴ━━━━━━━━━━━━
    ⛓┇ الروابط » {linklock}
    ⛓┇ الروابط بالحظر » {linkbanlock}
    ⛓┇ الروابط بالكتم » {linkmutelock}
    🚫┇ الممنوعه » {blocktextlock}
    🚫┇ الممنوعه بالحظر » {blocktextbanlock}
    🚫┇ الممنوعه بالكتم » {blocktextmutelock}
    🍿┇ الفشار » {fsharlock}
    🍿┇ الفشار بالحظر » {fsharbanlock}
    🍿┇ الفشار بالكتم » {fsharmutelock}
    ♻️┇ التوجيه » {forwardlock}
    ♻️┇ التوجيه بالحظر » {forwardbanlock}
    ♻️┇ التوجيه بالكتم » {forwardmutelock}
    🤖┇ قفل البوتات بالطرد » {kickbotatban}
    ٴ━━━━━━━━━━━━
    🖥┇ اليوتيوب » {youtubelock}
    📝┇ الترجمه » {translatelock}
    🔊┇ الاغاني » {musiclock}
    📽️┇ الافلام » {aflamlock}
    📠┇ الروايات » {rwayatlock}
    🎲┇ الالعاب » {gameslock}
    ⏱┇ الاذكار » {azkarlock}
    🔮┇ الزخرفه » {zhrafalock}
    🗞┇ الابراج » {abrag}
    🧾┇ معاني الاسماء » {namemeaning}
    ⏫┇ الرفع » {upplock}
    💫️┇ التاج » {taglock}
    👀┇ مين ضافني » {meendafnylock}
    ⚠️┇ رابط الحذف » {deletelinklock}
    💤┇ اطردني » {kickmelock}
    ٴ━━━━━━━━━━━━━━━━
      ძᥱ᥎ » @V_9_G 
      ᥴɦ  » @OR_UP
      ᥴɦ  » @UP_OF
                """
    await m.reply_text(textmessage, parse_mode=enums.ParseMode.MARKDOWN)
 
########################################################################################################################
########################################################################################################################

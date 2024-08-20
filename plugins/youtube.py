import os
import re
import requests
import aiofiles
import aiohttp
import requests
import wget
import lyricsgenius
import ffmpeg
import yt_dlp
from yt_dlp import YoutubeDL
from pyrogram import Client, filters, enums
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import get_bot_information
from database import set_db_wait
from urllib.parse import urlparse
from youtube_search import YoutubeSearch
from requests import get


ydl_opts = {
    'format': 'bestaudio/best',
    'write_thumbnail': True
}

ydl_opts_video = {
    'format': 'best',
    'write_thumbnail': True,
    'writethumbnail': True,
    'thumbnail_quality': 90
}


@Client.on_callback_query(filters.regex("^youtube (\\d+)$"))
async def youtube_main(c: Client, m: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("نتائج اليوتوب", callback_data="ntagyout " + str(m.from_user.id))] +
        [InlineKeyboardButton("تحميل من الرابط", callback_data="downyout " + str(m.from_user.id))],
        [InlineKeyboardButton("بحث اليوتوب صوت", callback_data="searchyout " + str(m.from_user.id))] +
        [InlineKeyboardButton("بحث اليوتوب فديو", callback_data="searchyoutvideo " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=dream")],
    ])
    await m.reply_text("◍ اهلا بك عزيزي قم بالاختيار...\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^ntagyout (\\d+)$"))
async def ntagyout(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    set_db_wait("ntagyoutube", m.from_user.id, m.message.chat.id)
    await m.message.edit_text("◍ماذا تريد انا ابحث لك...\n√")


@Client.on_callback_query(filters.regex("^downyout (\\d+)$"))
async def downyout(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    set_db_wait("downyout", m.from_user.id, m.message.chat.id)
    await m.message.edit_text("◍ارسل لى الرابط الان وساقوم بتحميله لك...\n√")


@Client.on_callback_query(filters.regex("^searchyout (\\d+)$"))
async def searchyout(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    set_db_wait("searchyout", m.from_user.id, m.message.chat.id)
    await m.message.edit_text("◍ارسل لى اسم الاغنيه وساجلبها لك...\n√")


@Client.on_callback_query(filters.regex("^searchyoutvideo (\\d+)$"))
async def searchyoutvideo(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    set_db_wait("searchyoutvideo", m.from_user.id, m.message.chat.id)
    await m.message.edit_text("◍ارسل لى اسم الفديو وساجلبه لك...\n√")


async def downfromlink(message: Message):
    m = await message.reply_text(f"◍ جاري تحميل الصوت من : {message.text}", disable_web_page_preview=True)
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(message.text, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
            # .webm -> .weba
            basename = audio_file.rsplit(".", 1)[-2]
            thumbnail_url = info_dict.get('thumbnail')
            # thumb
            if thumbnail_url and os.path.exists(thumbnail_url):
                thumbnail_file = basename + "." + get_file_extension_from_url(thumbnail_url)
            else:
                thumbnail_file = None
            if info_dict['ext'] == 'webm':
                audio_file_weba = basename + ".weba"
                os.rename(audio_file, audio_file_weba)
                audio_file = audio_file_weba
    except Exception as e:
        if str(e) == "ERROR: requested format not available":
            await m.edit("◍ هذه الاغنية مساحتها كبيرة جدا\n√")
            return
        else:
            await m.edit(str(e))
            return
    # info
    title = info_dict.get('title')
    webpage_url = info_dict.get('webpage_url')
    duration = int(float(info_dict.get('duration')))
    views = info_dict.get('view_count', 'N/A')
    if views != 'N/A':
        views = "{:,.0f}".format(int(views)).replace(",", ".") + " προβολές"
    else:
        views = 'N/A'
    channel = info_dict['uploader']
    caption = f"**🎶 Title ➖ [{title}]({webpage_url})**\n**⏱ Duration ➖** {duration // 60}:{duration % 60:02d}\n**👁 Views ➖** {views}\n**🎤 Channel ➖** {channel}" if title and webpage_url else None
    await m.delete()
    await message.reply_chat_action("upload_document")
    if thumbnail_file:
        await message.reply_audio(audio_file, caption=caption,
                                  reply_to_message_id=message.id,
                                  duration=duration,
                                  title=title, thumb=thumbnail_file, parse_mode=enums.ParseMode.MARKDOWN)
    else:
        await message.reply_audio(audio_file, caption=caption,
                                  reply_to_message_id=message.id,
                                  duration=duration,
                                  title=title, parse_mode=enums.ParseMode.MARKDOWN)
    os.remove(audio_file)
    if thumbnail_file:
        os.remove(thumbnail_file)

def get_file_extension_from_url(url):
    url_path = urlparse(url).path
    basename = os.path.basename(url_path)
    return basename.split(".")[-1]


async def urbandict(_, message: Message):
    if len(message.command) < 2:
        await message.reply_text('"/ud" Needs An Argument.')
        return
    text = message.text.split(None, 1)[1]
    api = "http://api.urbandictionary.com/v0/define?term="

    try:
        results = get(f"{api}{text}").json()
        reply_text = f'Definition: {results["list"][0]["definition"]}'
        reply_text += f'\n\nExample: {results["list"][0]["example"]}'
    except IndexError:
        reply_text = "Sorry could not find any matching results!"
    ignore_chars = "[]"
    reply = reply_text
    for chars in ignore_chars:
        reply = reply.replace(chars, "")
    if len(reply) >= 4096:
        reply = reply[:4096]
    await message.reply_text(reply)

# YouTube


async def ntagyoutube(message: Message):
    try:
        m = await message.reply_text("◍ جاري البحث....")
        results = YoutubeSearch(message.text, max_results=6).to_dict()
        i = 0
        text = ""
        while i < 6:
            text += f"Title - {results[i]['title']}\n"
            text += f"Duration - {results[i]['duration']}\n"
            text += f"Views - {results[i]['views']}\n"
            text += f"Channel - {results[i]['channel']}\n"
            text += f"https://youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        await m.edit(text, disable_web_page_preview=True)
    except Exception as e:
        await message.reply_text(str(e))


async def youttsearch(message: Message):
    try:
        a = await message.reply_text("◍ جاري البحث....")
        results = YoutubeSearch(message.text, max_results=1).to_dict()
        i = 0
        text = ""
        text += f"Title - {results[i]['title']}\n"
        text += f"Duration - {results[i]['duration']}\n"
        text += f"Views - {results[i]['views']}\n"
        text += f"Channel - {results[i]['channel']}\n"
        text += f"https://youtube.com{results[i]['url_suffix']}\n\n"

        a = await a.edit(f"{results[i]['title']}", disable_web_page_preview=True)
        a = await a.edit("جارى التحميل...", disable_web_page_preview=True)
        link = f"https://youtube.com{results[i]['url_suffix']}"
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(link, download=False)
                audio_file = ydl.prepare_filename(info_dict)
                ydl.process_info(info_dict)
                # .webm -> .weba
                basename = audio_file.rsplit(".", 1)[-2]
                thumbnail_url = info_dict['thumbnail']
                thumbnail_file = basename + "." + get_file_extension_from_url(thumbnail_url)
                if info_dict['ext'] == 'webm':
                    audio_file_weba = basename + ".weba"
                    os.rename(audio_file, audio_file_weba)
                    audio_file = audio_file_weba
        except Exception as e:
            if str(e) == "ERROR: requested format not available":
                await a.edit("◍ هذه الاغنيه مساحتها كبيره جداا\n√")
                return
            else:
                await a.edit(str(e))
                return
        # info
        title = info_dict['title']
        webpage_url = info_dict['webpage_url']
        duration = int(float(info_dict['duration']))
        views = info_dict.get('view_count', 'N/A')
        if views != 'N/A':
            views = "{:,.0f}".format(int(views)).replace(",", ".") + " προβολές"
        else:
            views = 'N/A'
        performer = info_dict['uploader']
        caption = f"**🎶 Title ➖ [{title}]({webpage_url})**\n**⏱ Duration ➖** {duration // 60}:{duration % 60:02d}\n**👁 Views ➖** {views}\n**🎤 Channel ➖** {performer}"
        await a.edit("انتظر جارى الرفع....", disable_web_page_preview=True)
        if os.path.isfile(thumbnail_file):
            await message.reply_audio(audio_file, caption=caption,
                                      reply_to_message_id=message.id,
                                      duration=duration, performer=performer,
                                      title=title, thumb=thumbnail_file, parse_mode=enums.ParseMode.MARKDOWN)
            os.remove(thumbnail_file)
        else:
            await message.reply_audio(audio_file, caption=caption,
                                      reply_to_message_id=message.id,
                                      duration=duration, performer=performer,
                                      title=title, parse_mode=enums.ParseMode.MARKDOWN)
        await a.delete()
        os.remove(audio_file)
    except Exception as e:
        await message.reply_text(str(e))


def download_file(url, file_name):
    with open(file_name, "wb") as f:
        response = requests.get(url)
        f.write(response.content)

async def youttsearch_video(message: Message):
    try:
        a = await message.reply_text("◍ جاري البحث....")
        results = YoutubeSearch(message.text, max_results=1).to_dict()
        i = 0
        text = ""
        text += f"Title - {results[i]['title']}\n"
        text += f"Duration - {results[i]['duration']}\n"
        text += f"Views - {results[i]['views']}\n"
        text += f"Channel - {results[i]['channel']}\n"
        text += f"https://youtube.com{results[i]['url_suffix']}\n\n"
        a = await a.edit(f"{results[i]['title']}", disable_web_page_preview=True)
        a = await a.edit("جارى التحميل...", disable_web_page_preview=True)
        link = f"https://youtube.com{results[i]['url_suffix']}"
        with YoutubeDL(ydl_opts_video) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
            if info_dict['ext'] == 'webm':
                audio_file_weba = audio_file.rsplit(".", 1)[0] + ".weba"
                os.rename(audio_file, audio_file_weba)
                audio_file = audio_file_weba
            thumbnail_url = info_dict['thumbnail']
            basename = audio_file.rsplit(".", 1)[-2]
            thumbnail_file = basename + "." + get_file_extension_from_url(thumbnail_url)
            download_file(thumbnail_url, thumbnail_file)
        title = info_dict['title']
        webpage_url = info_dict['webpage_url']
        duration = int(float(info_dict['duration']))
        views = info_dict.get('view_count', 'N/A')
        if views != 'N/A':
            views = "{:,.0f}".format(int(views)).replace(",", ".") + " προβολές"
        else:
            views = 'N/A'
        channel = info_dict['uploader']
        caption = f"**🎶 Title ➖ [{title}]({webpage_url})**\n**⏱ Duration ➖** {duration // 60}:{duration % 60:02d}\n**👁 Views ➖** {views}\n**🎤 Channel ➖** {channel}"
        await message.reply_video(audio_file, caption=caption, reply_to_message_id=message.id, duration=duration, thumb=thumbnail_file, parse_mode=enums.ParseMode.MARKDOWN)
        await a.delete()
        os.remove(audio_file)
        os.remove(thumbnail_file)
    except Exception as e:
        await message.reply_text(str(e))

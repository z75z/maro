import random
from datetime import datetime
import requests
from pyrogram import Client
from pyrogram.types import Message
from database import set_db_wait, del_db_botname, get_db_lockreply, set_db_lockreply, del_db_lockreply


########################################################################################################################
########################################################################################################################


# rep one text msg
async def txt1(m, txt, rep):
    if m.text == txt:
        await m.reply_text(random.choice(rep))
        return


# rep one sticker
async def sticker1(m, txt, rep):
    if m.text == txt:
        await m.reply_sticker(rep)
        return


# rep audio one
async def audio1(m, txt, rep):
    if m.text == txt:
        await m.reply_audio(rep)
        return


# rep video one
async def video1(m, txt, rep):
    if m.text == txt:
        await m.reply_video(rep)
        return


# rep document one
async def document1(m, txt, rep):
    if m.text == txt:
        await m.reply_document(rep)
        return


###################################

# rep all text msg
async def txtall(m, lists, rep):
    if m.text:
        for v in lists:
            if v in m.text:
                await m.reply_text(random.choice(rep))
                return


# rep all sticker
async def stickerall(m, lists, rep):
    if m.text:
        for v in lists:
            if v in m.text:
                await m.reply_sticker(rep)
                return


# rep audio all
async def audioall(m, lists, rep):
    if m.text:
        for v in lists:
            if v in m.text:
                await m.reply_audio(rep)
                return


# rep video all
async def videoall(m, lists, rep):
    if m.text:
        for v in lists:
            if v in m.text:
                await m.reply_video(rep)
                return


# rep document all
async def documentall(m, lists, rep):
    if m.text:
        for v in lists:
            if v in m.text:
                await m.reply_document(rep)
                return


########################################################################################################################
########################################################################################################################

async def lock_lockreply_open(m: Message):
    del_db_lockreply(m.chat.id)
    await m.reply_text("◍ تم فتح الردود\n√")


async def lock_lockreply_close(m: Message):
    if get_db_lockreply(m.chat.id) is None:
        set_db_lockreply("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الردود\n√")
        return
    else:
        for per in get_db_lockreply(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ الردود مقفوله بالفعل\n√")
                return
        set_db_lockreply("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الردود\n√")
        return


async def lock_lockreply_test(m: Message):
    leader = True
    if get_db_lockreply(m.chat.id) is None:
        leader = True
    else:
        for per in get_db_lockreply(m.chat.id):
            if per[0] == "yes":
                leader = False
            else:
                leader = True
    return leader


########################################################################################################################
########################################################################################################################

async def echo_text(m: Message):
    await m.reply_text(m.text[3:])


async def say_text(m: Message):
    r = requests.get("https://apiabs.ml/Antk.php?abs=" + m.text[5:])
    rj = r.json()
    await m.reply_audio("https://translate" + rj["result"]["google"] + rj["result"]["code"] + "UTF-8" +
                       rj["result"]["utf"] + rj["result"]["translate"] + "&tl=ar-IN")


async def omrk(m: Message):
    set_db_wait("calcomrak", m.from_user.id, m.chat.id)
    await m.reply_text("◍ ارسل لى تاريخ ميلادك بهذا الشكل -> 5/9/2000\n√")


async def addgeneralrep(m: Message):
    set_db_wait("addgreply", m.from_user.id, m.chat.id)
    await m.reply_text("◍ ارسل لى الكلمه الان\n√")


async def delgeneralrep(m: Message):
    set_db_wait("delgreply", m.from_user.id, m.chat.id)
    await m.reply_text("◍ ارسل لى الكلمه التى ترغب فى حذفها\n√")


async def namebot(m: Message):
    del_db_botname()
    set_db_wait("namebot", m.from_user.id, m.chat.id)
    await m.reply_text("◍ ارسل لى الاسم الان\n√")


########################################################################################################################
########################################################################################################################

async def allreply_for_bot(c: Client, m: Message):
    await txt1(m, "عندك كام سنه", ["لا قول انت الاول 😂❤️", "خمنااشر وانت 🙄", "بتعرف تعد لحد كام 🙄😂"])
    await txt1(m, "حبك", ["حبككك اكترر ❤️", "مسمعكش تقولي كده تانى 🙂", "ياهلا بالخوازيق 🥺❤️", "بكرهههههك 🙂🙂"])
    await txt1(m, "حصلخير", ["حصلخير اي هيجي منين الخير وانت هنا. 🙂😂"])
    await txt1(m, "حه", ["اي يستا جيت ع الجرح 🙂😂", "عيييييييييييب 🙄", "متنرفزوناش بقا اللاه 🙄"])
    await txt1(m, "خدو مني الفون", ["كلميني ع الواتس يمزه 😂❤️"])
    await txt1(m, "بابا", ["😂❤️ مين حبيب بابا انا مين روح بابا انا نينينيني "])
    await txt1(m, "ماما", ["ست الحبايب ياحبيه ياحبيبه 😌😂"])
    await txt1(m, "شتمني", ["ولا حاجه يقلبي بكرا يتزنق ويجي حقك من غير متقل ادبك 😂❤️ مصيبه ده "])
    await txt1(m, "يبرو", ["اي يقلب البرو في حد مزعلك انا هقوم بالواجب 😂❤️"])
    await txt1(m, "يسطا", ["قابلتك ع البسطه 😂❤"])
    await txt1(m, "فرحان", ["❤️ ربنا يتمم افراحك "])
    await txt1(m, "عيب", ["سيب الواد يلعب 😂😂"])
    await txt1(m, "يحب", ["🥺❤️ اي ياكبد الحب "])
    await txt1(m, "عامل اي", ["احسن منك 😌😂👌", "الحمدلله وانت 🥺❤️", "بخير طول مانت بخير 🥺❤️"])
    await txt1(m, "بعشقك", ["وه وه قدام الناس كده عيب 🙈❤️", "راعو ان فى ناس سناجل 🥺❤️", "بشعشك بكل تفاصيلك ❤️😂"])
    await txt1(m, "انت نرم", ["الله يرحم ابوك كان بيشرب الشربه بخرطوم الغساله😂🙂"])
    await txt1(m, "خد", ["لا يعم نا ماشي سلام 🌝😂"])
    await txt1(m, "الزعامه", ["الزعامه فوق وكسكلياه ضالابواه 💔😹"])
    await txt1(m, "فين الادمن", ["ايش بتريد منه🤔"])
    await txt1(m, "هاي", ["هاى ماى جايز❤️😉"])
    await txt1(m, "هلو", ["هلو باللى سرق قلبى 🤗🌟"])
    await txt1(m, "ماشى", ["ماشى رايح فين ❤️🥺", "خد الباب وراك 😂😂", "المركب اللى تودي 🙂😂"])
    await txt1(m, "غلس", ["اهو انت💔🥺"])
    await txt1(m, "بف", ["خدوني معاكم بف..🙄💔"])
    await txt1(m, "تع بف", ["خدوني معاكم بف..🙄💔"])
    await txt1(m, "انت مين", [" بتسال لي💨🌝"])
    await txt1(m, "احبك", ["احبككك اكترر ❤️", "مسمعكش تقولي كده تانى 🙂", "ياهلا بالخوازيق 🥺❤️", "بكرهههههك 🙂🙂"])
    await txt1(m, "اوف", ["لمين هاي ؟🌚🌙"])
    await txt1(m, "في اي", ["مافيش حاجه🙄"])
    await txt1(m, "نايمين", ["انا سهران😿😹"])
    await txt1(m, "كفايه كلام", ["اسكت انت😼👊"])
    await txt1(m, "هيي", ["يالا ياض من هنا😂💔"])
    await txt1(m, "انت فين", ["بارض الله الواسعه 😽😂"])
    await txt1(m, "هه", ["ضحكه مش سالكه 😳😂"])
    await txt1(m, "البوت عطلان", ["بطلو كدب بقي 🙄🙂"])
    await txt1(m, "البوت واقف", ["لا تكذب حبي🌞"])
    await txt1(m, "المدرسه", ["اذا بتجيب اسمها بطردك🌞✨"])
    await txt1(m, "شوف", [" اشوف اي 🌝🌝"])
    await txt1(m, "🙂", ["هنكد بقا اهو 😕"])
    await txt1(m, "🚶💔", ["تعالي اشكيلي ايش فيك🙁💔"])
    await txt1(m, "🙁", [" اشكيلي هموك ليش متضايق🙁💔"])
    await txt1(m, "😳", ["اوميقد😐😹"])
    await txt1(m, "😒", ["ايش بيك ؟😟"])
    await txt1(m, "تحبني", ["اممم افكر🙁😹", "زى اختي 🙂", "ياهلا بالخوازيق 🥺❤️", "بكرهههههك 🙂🙂"])
    await txt1(m, "بتحبني", ["اممم افكر🙁😹", "زى اختي 🙂", "ياهلا بالخوازيق 🥺❤️", "وهو القمر ميتحبش ؟؟ ❤️😂"])
    await txt1(m, "باي", ["ع فين لوين رايح وسايبنى🙁💔", "بايباي 🙂", "في رعايه الله 🥺❤️", "فى ستين داهيه 🙂🙂"])
    await txt1(m, "تعالي خاص", ["لو بنت هاجي غير كدة لا 🙄😂"])
    await txt1(m, "فرخه", ["خليها تبيض😂😂😂"])
    await txt1(m, "حاضر", ["حضرلك الخير ياارب ❤️", "شطووور 🙂", "اى الاحترام ده 🙄"])
    await txt1(m, "😐", ["مالك ي حبيبي 😔"])
    await txt1(m, "ار يو ريدى", ["بكوى القميص وجهزت اهو 🔥🥺😂"])
    await txt1(m, "وات", ["ازغط بط 😳😂"])
    await txt1(m, "ملكش دعوة", ["خدو واستعوى ❤️😂"])
    await txt1(m, "ملكش دعوه", ["خدو واستعوى ❤️😂"])
    await txt1(m, "انت مالك", ["مالى فى جيبى هه ❤️😂"])
    await txt1(m, "احسن", ["جتك لحسه 😂💃"])
    await txt1(m, "نعم", ["نعم الله عليك🙂"])
    await txt1(m, "نرتبط", ["مرتبط مع نفسي واحزاني ❤️😢"])
    await txt1(m, "بلوك", ["لما اللي منك يجرحك😢"])
    await txt1(m, "انا بكرهك", ["حبني بلييز 🥺"])
    await txt1(m, "بيبى", ["قلبى ياناس قلباااااى 😂❤️"])
    await txt1(m, "ها", ["هاا ياروحي"])
    await txt1(m, "فديت", ["فدااك ♥️"])
    await txt1(m, "محدش بيسال عليا", ["بنسأل عليك ياحلووو 🖤🔍"])
    await txt1(m, "شلونكم", ["تمام وانت يكيوت ؟ 💕"])
    await txt1(m, "كداب", ["انت اللى كدااب يحليتها ❤️😹"])
    await txt1(m, "عادي", ["فى المعادى هه😂😂"])
    await txt1(m, "عجبتك", ["اكييد اكتيير 😎"])
    await txt1(m, "حبيبي", ["اوه ياه 🌝😂"])
    await txt1(m, "بت", ["ليا اسم ياض يعره يمهزء نينينينني😹😎🏃🏻‍♀"])
    await txt1(m, "روحي", ["خلصتت روحكك يبعيد😹🚶🏻‍♀💔"])
    await txt1(m, "بوتي", ["قلب بوتكك من جواا 🥺♥️"])
    await txt1(m, "مش هتيجي", ["مش هرووووح 😹🏃🏻‍♀🏃🏻‍♀"])
    await txt1(m, "تف", ["اصفخص عليك منتن ءتفووووو😹👅"])
    await txt1(m, "وه", ["بسيفلاح يعره مسمعش صوتكك😹🤸🏻‍♀🙊"])
    await txt1(m, "وهه", ["بسيفلاح يعره مسمعش صوتكك😹🤸🏻‍♀🙊"])
    await txt1(m, "اي", ["جتك اوهه م سامع ولا ايي😹👻"])
    await txt1(m, "ايي", ["جتك اوهه م سامع ولا ايي😹👻"])
    await txt1(m, "طيب", ["فرح خالتك قريب😹💋💃🏻"])
    await txt1(m, "تيب", ["فرح خالتك قريب😹💋💃🏻"])
    await txt1(m, "خلاص", ["خلصتت روحكك يبعيد😹🚶🏻‍♀💔"])
    await txt1(m, "حصل", ["حصل حصوله 😹💜"])

    await txt1(m, "رفع شاذ", ["""✓ أهلاً عزيزي 
✓ تم رفع العضو شاذ بنجاح 🏳‍🌈
✓ هو الان شاذ وقابل للشقط واي مصلحه اخري 💅🏼
•اللهم احفظنا• 😹😎"""])
    await txt1(m, "رفع شاذه", ["""✓ أهلاً عزيزي 
✓ تم رفع العضوه شاذه بنجاح 🏳‍🌈
✓ هي الان شاذه وقابله للشقط واي مصلحه اخري 💅🏼
•اللهم احفظنا• 😹😎"""])
    await txt1(m, "كتم الكل", ["""✓ تم كتم الكل بنجاح 🙆🏻‍♀
× وهتتكلم مع مين يمتوحد انت× 😹🚶🏻‍♀"""])
    await txt1(m, "تنزيل شقوطه", ["""✓ تم تنزيل العضو شقوطه بنجاح 🥲
✓ الان هو ولا بيعرف يشقط ولا ينيل حاجه😹🤸🏻‍♀💔"""])
    await txt1(m, "حذف حياتي", ["""✓ اهلا يعم المجهول 
✓  تم حذف حياتك الي مكنتش موجوده اصلا
✓ الان انت معدوم من كل حته 
• خزان ءحزان •"""])
    await txt1(m, "تعطيل المحن", ["""✓ اهلا عزيزي 🙆🏻‍♀
✓ تم تعطيل المحن بنجاح 😎😹
✓ اتمحونوا بف عشان المراره 😌🙂"""])
    await txt1(m, "رفع خنزير", ["""✓ تم رفع العضو حنزير بنجاح
✓ هو الان خنزير بيشخر 24 ساعهه ومحدش عارف يلمو🐷😳"""])
    await txt1(m, "رفع شقوطه", ["""✓ تم رفع العضو شقوطه 
✓ هو الان بيعرف يشقط ومش سايب حد فحالو😹💔"""])
    await txt1(m, "شخ", ["""✓ تم الشخ ع العضو بنجاح 💩
✓ هو الان عليه شخايه يععععععععععع 😹😵"""])
    await txt1(m, "نف", ["""✓ تم النف ع العضو بنجاح 🤧
 هو الان عليه بربور يععععععععععع 😹😪"""])
    await txt1(m, "رفع حكاك", ["""✓ تم رفع العضو حكاك بنجاح 🙈
    ✓ اه ياحكاك ياعره المجتمع 😹😵"""])
    await txt1(m, "رفع قمر", ["""✓ تم رفع العضو قمر بنجاح 🌚
    ✓ يخلاثى على قمرايه الروم ياناس 🥺❤️"""])
    await txt1(m, "رفع مزتي", ["""✓ تم رفع العضو مزه جامده فحت بنجاح 🙄
    ✓ اه يابت يامزززه يلا هزى هزاااه 💃💃"""])
    await txt1(m, "رفع اخويا", ["""✓ تم رفع العضو اخا لك 🙄
    ✓ وبقى اخويا اللى مجبتهوش امي ❤️😂"""])
    await txt1(m, "رفع اختي", ["""✓ تم رفع المزه دى اختك 🙄
    ✓ بقيتو اخوات خلاص مينفعش تتجوزو 🙂😂"""])

    if m.text == "كلب" or m.text == "كلاب":
        r = requests.get("https://random.dog/woof.json")
        rj = r.json()
        dog = rj["url"]
        await m.reply_photo(dog)
        return

    if m.text == "قطه" or m.text == "قطط":
        r = requests.get("https://api.thecatapi.com/v1/images/search")
        rj = r.json()
        dog = rj[0]["url"]
        await m.reply_photo(dog)
        return

    if m.text == "بينج" or m.text == "ping":
        first = datetime.now()
        sent = await m.reply_text("<b>Pong!</b>")
        second = datetime.now()
        await sent.edit_text(f"<b>Pong!</b> <code>{(second - first).microseconds / 1000}</code>ms")
        return

    # all ====================
    # await txtall(m, ["S"], "G")
    await txtall(m, ["مراتي"], ["عرفني عليها ينوبك ثواب🥺🙈"])
    await txtall(m, ["يوتكه"], ["بتعاكس انت لحد ميقولو عليك حكاك بتحصل بتحصل 🙂😂"])
    await txtall(m, ["مزه"], ["خف معاكسه يبني عييب 🙂😂"])
    await txtall(m, ["حلال"], ["الله عليك ياشيخنا 🙄😹"])
    await txtall(m, ["حرام"], ["اخيرا في حد عاقل ❤️🙈"])
    await txtall(m, ["سجاره"], ["ابوك عارف انك بتشرب سجاير 😂🙂"])
    await txtall(m, ["ينرم", "نرم"], ["عييب مشوفتش نفسك لم اول مره مسكت تلفون كان منظرك كده 🤪"])
    await txtall(m, ["حبيبتي"], ["اوعه ع الجمدان بقا حبيبتي وشغل عالي 🙈❤️"])
    await txtall(m, ["سي في", "سيفي", "cv"], ["كفايه شقط يبني سيب حاجه لغيرك 😹👅"])
    await txtall(m, ["اخرس"], ["هتت لازقه وحطها ع بوئيي😹🙊🤸🏻‍♀"])
    await txtall(m, ["بقولك", "بقول"], ["لاء متقولش نينينينني😹🏃🏻‍♀♥️", "شفلك كلبه🙄😂",
                                        "التافه اللى زيك هيقول اى يعنى🙂😂"])
    await txtall(m, ["ده بوت", "دا بوت", "دهه بوت"], ["ياحلولي هو كان فاكرني انسان ولا ايي 😹"])
    await txtall(m, ["جيت", "انا جيت"], ["لف وارجع تاني م حوارر 😹🚶🏻‍♀♥️"])
    await txtall(m, ["مساء الخير", "سالخير", "مساء النور"], ["سالنور ياولا 💃🏻😹", "مسائك عسل ي عسل❤️🙄",
                                                             "مسا مسا ع الناس الكويسه 🙄❤️", "مسااااءو فل ❤️😂"])
    await txtall(m, ["احتويه"], ["""✓ تم احتواء العضو بنجاح 
    ✓ تع ف حضن حمو ياولا 😹♥️"""])
    await txtall(m, ["يوه"], ["يقطعني 😹🙆🏻‍♀♥️"])
    await txtall(m, ["💋"], ["عايز من ده..💋🥀"])
    await txtall(m, ["😒"], ["اعدل وشكك ونت بتكلمني 😒"])
    await txtall(m, ["🌝", "🌚"], ["القمر ده شبهك..🙂♥️"])
    await txtall(m, ["شش"], ["بنهش كتاكيت احنا هنا ولا اى😒💔"])
    await txtall(m, ["صباح الخير"], ["صباحك عسل ي عسل❤️🙄", "صبح صبح ياعم الحج 🙄❤️", "صباحووو فل ❤️😂"])
    await txtall(m, ["روم اي ده"], ["رغى وشقط😉🙄", "هيكون اى يعني غير رغى🙄😂"])
    await txtall(m, ["اسكت"], ["اما انت غتت صحيح💔🥺", "هنكد لحد امتى🙂🙂"])
    await txtall(m, ["ب.ف", "ب ف", "بي اف"], ["🌝خدوني معاكووا", "اجي وياكم 🌚💁", "وااالعه🔥😂","خدوني معاكم بف..🙄💔"])
    await txtall(m, ["السلام عليكم", "سلام عليكم"], ["وعليكم السلام❤️"])
    await txtall(m, ["😂😂😂"], ["ضحكتك عثل زيكك ينوحيي 🌝❤️"])

    # rep all sticker ====================
    # await stickerall(m, ["t"], "sticker link")
    await stickerall(m, ["بص", "بصي", "بص كده"], "https://t.me/var_alpop/7")
    await stickerall(m, ["اجري", "إجري", "أجري"], "https://t.me/var_alpop/9")
    await stickerall(m, ["مكسوفة", "مكسوفه"], "https://t.me/UUSDI55/9")
    await stickerall(m, ["عاش"], "https://t.me/var_alpop/13")
    await stickerall(m, ["جامد"], "https://t.me/var_alpop/14")
    await stickerall(m, ["دماغ"], "https://t.me/var_alpop/15")
    await stickerall(m, ["بفكر"], "https://t.me/UUSDI55/13")
    await stickerall(m, ["حبكي"], "https://t.me/var_alpop/17")
    await stickerall(m, ["قطتي"], "https://t.me/var_alpop/18")
    await stickerall(m, ["بطه"], "https://t.me/var_alpop/19")
    await stickerall(m, ["قمر"], "https://t.me/var_alpop/20")
    await stickerall(m, ["كتكوت"], "https://t.me/var_alpop/21")
    await stickerall(m, ["حزين"], "https://t.me/var_alpop/22")
    await stickerall(m, ["ماتيجي", "متيجي", "متيقي"], "https://t.me/var_alpop/23")
    await stickerall(m, ["اسطوره"], "https://t.me/UUSDI55/22")
    await stickerall(m, ["عشه"], "https://t.me/UUSDI55/23")
    await stickerall(m, ["فقير"], "https://t.me/var_alpop/32")
    await stickerall(m, ["بصلي"], "https://t.me/UUSDI55/25")
    await stickerall(m, ["احزنني"], "https://t.me/var_alpop/779")
    await stickerall(m, ["جمدان"], "https://t.me/var_alpop/778")
    await stickerall(m, ["حرامي"], "https://t.me/var_alpop/27")
    await stickerall(m, ["اتفق", "اتفق"], "https://t.me/var_alpop/780")
    await stickerall(m, ["عادل شكل", "قلقاسه", "الناحو", "الزعامه"], "https://t.me/var_alpop/28")
    await stickerall(m, ["م عارف", "مش عارف"], "https://t.me/var_alpop/29")
    await stickerall(m, ["error", "ايرور", "404"], "https://t.me/var_alpop/782")
    await stickerall(m, ["صدمتني", "صدمه"], "https://t.me/var_alpop/783")
    await stickerall(m, ["المطرشم", "maro", "المشطشط", "مارو"], "https://t.me/marovip/45")
    await stickerall(m, ["المطرشم", "maro", "المشطشط", "مارو"], "https://t.me/marovip/46")


    # rep one sticker ====================
    # await sticker1(m, "t", "sticker link")
    await sticker1(m, "يتي", "https://t.me/var_alpop/784")

    # rep audio one
    await audioall(m, ["كتاب حياتي ياعين", "كتاب حياتي"], "https://t.me/var_alpop/785")

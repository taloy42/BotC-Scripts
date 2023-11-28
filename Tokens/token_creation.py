import utils
import const
from PIL import ImageDraw, ImageFont
import PIL
from wand.image import Image as WandImage
from wand.font import Font as WandFont
import numpy as np


def create_token_backup(name, img, text):
    # font_space_frac = 5/16
    font_space_frac = 7 / 16

    # put image on background
    res = utils.add_img_to_bg(
        img, const.TOKEN_BG(), vertical_offset_frac=0.2
    )  # ,vertical_space_frac=font_space_frac)
    W, H = res.size

    draw = ImageDraw.Draw(res)
    # add ability text
    font = ImageFont.truetype(font=const.FONT_PATH(), size=20)
    s = font.getsize(name)
    # draw.multiline_text(((W-s[0])//2,50),text,font=font,align='right',fill='black',)
    font = get_optimal_multiline_font(
        const.FONT_PATH(), text, H * font_space_frac, im_size=H
    )
    font = ImageFont.truetype(font=const.FONT_PATH(), size=25)
    draw_multiline(draw, res.size, font, text)
    # add name
    # font = ImageFont.truetype(font='dorian2.ttf', size=50)
    font = get_optimal_font(const.FONT_PATH(), name, W * 7 / 12)
    s = font.getsize(name)
    if const.DIRECTION == "rtl":
        name = utils.change_dir(name)
    draw.text(
        ((W - s[0]) // 2, int(512 * 19 / 24)),
        name,
        font=font,
        align="right" if const.DIRECTION == "rtl" else "left",
        fill="black",
    )

    return res


def add_leaves(character, img, group=None):
    firstNight = len(character.get("firstNightReminder", "")) > 0

    otherNight = len(character.get("otherNightReminder", "")) > 0

    ability = character.get("ability", "")
    changeSetup = "[" in ability and "]" in ability
    changeSetup = character.get("setup", changeSetup)

    n_reminders = len(character.get("reminders", []))

    if firstNight:
        left_leaf = const.LEFT_LEAF(group)
        img.paste(left_leaf, (0, 0), left_leaf)

    if otherNight:
        right_leaf = const.RIGHT_LEAF(group)
        img.paste(right_leaf, (0, 0), right_leaf)

    if changeSetup:
        orange_leaf = const.ORANGE_LEAF(group)
        img.paste(orange_leaf, (0, 0), orange_leaf)

    if n_reminders > 0:
        top_leaf = const.TOP_LEAF(n_reminders, group)
        img.paste(top_leaf, (0, 0), top_leaf)
    return img


def add_name_to_img(name, img, color="black", mode="token", font_path=None):
    if font_path is None:
        font_path = const.NAME_FONT_PATH()
    font = ImageFont.truetype(font_path, size=60)
    font_width = font.getsize(name)[0]
    r = img.size[0] // 2
    # degs_per_let = 12
    # rmax,rmin,cx,cy,angmin,angmax = 0.8*r,0.55*r,r,r,-degs_per_let*len(name)/2,degs_per_let*len(name)/2
    if mode == "token":
        let_width = const.LETTER_WIDTH(mode)
        rmax, rmin, cx, cy, angmin, angmax = (
            0.8 * r,
            0.55 * r,
            r,
            r,
            -let_width * font_width / 2,
            let_width * font_width / 2,
        )
    elif mode == "reminder":
        let_width = const.LETTER_WIDTH(mode)
        rmax, rmin, cx, cy, angmin, angmax = (
            0.95 * r,
            0.7 * r,
            r,
            r,
            -let_width * font_width / 2,
            let_width * font_width / 2,
        )
    else:
        raise Exception()
    with WandImage(width=2 * r, height=2 * r) as wand_img:
        wand_img.background_color = "transparent"
        wand_img.font = WandFont(font_path, 60)
        wand_img.font_color = color
        wand_img.read(filename="label: {} ".format(name))
        wand_img.resize(2 * r, 2 * r)
        wand_img.virtual_pixel = "transparent"
        # 360 degree arc, rotated -90 degrees
        wand_img.distort("polar", (rmax, rmin, cx, cy, angmin, angmax))

        # img.save(filename='arc_text.png')
        wand_img.format = "png"
        # display(img)
        # img_buffer = np.asarray(bytearray(img.make_blob()), dtype='uint8')
        # bytesio = BytesIO(img_buffer)
        # img = skimage.io.imread(bytesio)
        npa = np.array(wand_img)
        # text = wand2pil(img)
    # bg.show()
    text = PIL.Image.fromarray(npa)

    img.paste(text, (0, 0), text)
    return img


def create_token(character, img, group=None):
    # font_space_frac = 5/16
    # font_space_frac = 7/16
    name, text = character["name"], character["ability"]
    # put image on background
    res = utils.add_img_to_bg(
        img, const.TOKEN_BG(group)
    )  # ,vertical_space_frac=font_space_frac)
    res = add_leaves(character, res, group)
    W, H = res.size

    draw = ImageDraw.Draw(res)
    # add ability text
    # font = ImageFont.truetype(font=const.FONT_PATH(), size=20)
    # s = font.getsize(name)
    # draw.multiline_text(((W-s[0])//2,50),text,font=font,align='right',fill='black',)
    font = get_optimal_multiline_font(
        const.FONT_PATH(), text, int((H // 2) * 13 / 16), im_size=H
    )
    # font = ImageFont.truetype(font=const.FONT_PATH(), size=const.FONT_SIZE())
    draw_multiline(draw, res.size, font, text)
    # add name
    # font = ImageFont.truetype(font='dorian2.ttf', size=50)

    name = name.upper()

    # font = get_optimal_font(const.NAME_FONT_PATH(),name,W*5/12)
    # s = font.getsize(name)
    # if const.DIRECTION=='rtl':
    #   name = utils.change_dir(name)
    # draw.text(((W-s[0])//2,int(H*.8)),name,font=font,align='right' if const.DIRECTION=='rtl' else 'left',fill='black')
    add_name_to_img(name, res, mode="token")
    return res


def create_token_ch(character, group=None):
    if character["id"] == "_meta":
        return None

    edition = character.get("edition")
    is_fabled = character.get("team") == "fabled"
    if is_fabled:
        group = "fabled"
    elif edition in const.groups:
        group = edition

    copies = character.get("tokenCopies", 1)
    if copies < 0:
        copies = const.MAX_TOKENS_FOR_SINGLE_ROLE
    # images = character["image"]
    images = rf'C:\Users\anukh\Downloads\BotC\repository\BotC-Scripts\Resources\Icons\{character["id"]}.png'
    if isinstance(images, list):
        images = [
            utils.url_to_image(image).resize((const.IMG_SIZE, const.IMG_SIZE))
            for image in images
        ]
        tokens = [create_token(character, im, group) for i, im in enumerate(images)]
        return [x for x in tokens for i in range(copies)]
    image = utils.url_to_image(images).resize((const.IMG_SIZE, const.IMG_SIZE))
    token = create_token(character, image, group)
    return [token for i in range(copies)]


# def cv2_to_PIL(img):
#   img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#   im_pil = Image.fromarray(img)
#   return im_pil
def create_reminder(image, reminder):
    bg = const.REMINDER_BG()
    W, H = bg.size
    box = ((W * 1) // 2, (H * 1) // 2)
    res = utils.add_img_to_bg(
        image, bg, box=box, from_height=int(H * 0.2)
    )  # ,vertical_space_frac=font_space_frac)

    draw = ImageDraw.Draw(res)
    # add ability text
    # s = font.getsize(name)
    # draw.multiline_text(((W-s[0])//2,50),text,font=font,align='right',fill='black',)
    # font = get_optimal_multiline_font(const.FONT_PATH(),text,H*font_space_frac,im_size=H)
    # font = ImageFont.truetype(font=const.FONT_PATH(), size=const.REMINDER_FONT_SIZE())
    # draw_multiline(draw,res.size,font,reminder,min_height=H*0.8,color='white')
    add_name_to_img(
        reminder, res, color="white", mode="reminder", font_path=const.FONT_PATH()
    )
    # add name
    # font = ImageFont.truetype(font='dorian2.ttf', size=50)

    # font = ImageFont.truetype(font=const.FONT_PATH(), size=20)
    # name = name.upper()

    # font = get_optimal_font(const.NAME_FONT_PATH(),name,W*5/12)
    # s = font.getsize(name)
    # if const.DIRECTION=='rtl':
    #   name = utils.change_dir(name)
    # draw.text(((W-s[0])//2,int(H*.8)),name,font=font,align='right' if const.DIRECTION=='rtl' else 'left',fill='black')
    # add_name_to_img(name,res)
    return res


def create_reminders_ch(character):
    if character["id"] == "_meta":
        return None

    # edition = character.get('edition')
    # is_fabled = character.get('team') == 'fabled'
    # if is_fabled:
    #   group = 'fabled'
    # elif edition in const.groups:
    #   group = edition

    # image = character["image"]

    # image = character["image"]
    image = rf'C:\Users\anukh\Downloads\BotC\repository\BotC-Scripts\Resources\Icons\{character["id"]}.png'
    if isinstance(image, list):
        image = image[0]
    image = utils.url_to_image(image).resize((const.REMINDER_SIZE, const.REMINDER_SIZE))
    reminders = character.get("reminders", [])
    reminderCopies = character.get("reminderCopies", [1] * len(reminders))

    import itertools

    reminders = zip(reminders, itertools.cycle(reminderCopies))
    # reminders = [(x,1) if isinstance(x,str) else tuple(x) for x in reminders]

    # if isinstance(reminders,list):
    reminders = [
        [create_reminder(image, reminder)] * copies for reminder, copies in reminders
    ]
    # tokens = [create_token(character,im) for i,im in enumerate(reminders)]
    return reminders
    # image = utils.url_to_image(reminders).resize((const.IMG_SIZE,const.IMG_SIZE))
    # token = create_token(character,image,group)
    # return [token for i in range(copies)]


def get_optimal_font_size(font_path, text, width, is_width=True):
    for size in range(50, 1, -1):
        font = ImageFont.truetype(font=font_path, size=size)
        s = font.getsize(text)

        if s[is_width] < width:
            return size
    return 1


def get_optimal_font(font_path, text, width, is_height=False):
    for size in range(50, 1, -1):
        font = ImageFont.truetype(font=font_path, size=size)
        s = font.getsize(text)

        if s[int(is_height)] < width:
            break
    return font


def get_optimal_multiline_size(font_path, text, max_height, min_height=60, im_size=512):
    for size in range(50, 1, -1):
        font = ImageFont.truetype(font=font_path, size=size)
        if check_multiline_font(font, text, max_height, min_height, im_size):
            return size
    return 1


def get_optimal_multiline_font(
    font_path, text, max_height, min_height=90, im_size=512, max_font_size=25
):
    for size in range(max_font_size, 1, -1):
        font = ImageFont.truetype(font=font_path, size=size)
        if check_multiline_font(font, text, max_height, min_height, im_size):
            break
    return font


def draw_multiline(draw, size, font, text, min_height=90, color="black"):
    W, H = size
    # R = get_diam_for_size(W)
    R = W // 2
    h = min_height
    later = text
    while later is not None:
        now, later = split_by_width(font, width4height(h, R), later)
        s = font.getsize(now)
        if const.DIRECTION == "rtl":
            now = utils.change_dir(now)
        draw.text(((W - s[0]) // 2, h), now, fill=color, font=font)
        h += font.getsize(now)[1]
    return draw


def check_multiline_font(font, text, max_height, min_height=90, im_size=512):
    h = min_height
    later = text
    # R = get_diam_for_size(im_size)
    R = im_size // 2
    while later is not None:
        now, later = split_by_width(font, width4height(h, R), later)
        h += font.getsize(now)[1]
    return h <= max_height


def split_by_width(font, width, text):
    words = text.split(" ")
    if len(words) <= 1:
        return text, None
    check = ""
    for i in range(len(words) + 1):
        if i == len(words):
            break
        check += words[i]
        if font.getsize(check)[0] > width:
            break
    if i == 0:
        return words[0], " ".join(words[1:])
    return " ".join(words[:i]), " ".join(words[i:])


def get_diam_for_size(size, perc=5):
    return size * (1 - 2 * perc / 100)


def width4height(height, R, p=5):
    """
    allowed width for given height in circle with diameter diam
    """
    p = 1 - 5 * p / 100
    h = height - R * (1 - p)
    delta = (p**2 - 1) * R**2 + 2 * R * height - height**2
    if delta < 0:
        return 0

    return 2 * (delta) ** 0.5

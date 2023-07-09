from PIL import Image
import json
import utils
ROOT_DIR = ''
ROOT_DIR = 'Tokens'

__TOKEN_BG = Image.open(rf'{ROOT_DIR}\resources\token_bg.png')
__TOKEN_BG = __TOKEN_BG.resize((512,512))
FONT_PATH = rf'{ROOT_DIR}\resources\dorian2.ttf'
def TOKEN_BG():
    return __TOKEN_BG.copy()

SCRIPTS = {
    'trouble-brewing':None,
    'sects-and-violets':None,
    'bad-moon-rising':None,
    'all-roles':None
}

DPI = 300
IMG_SIZE_INCH = 1.75
REMINDER_SIZE_INCH = 1

PAGE_WIDTH_INCH = 8.3
PAGE_HEIGHT_INCH = 11.7

IMG_SIZE = int(DPI*IMG_SIZE_INCH)
REMINDER_SIZE = int(DPI*REMINDER_SIZE_INCH)

PAGE_WIDTH = int(PAGE_WIDTH_INCH*DPI)
PAGE_HEIGHT = int(PAGE_HEIGHT_INCH*DPI)

PAGE_SIZE = (PAGE_WIDTH,PAGE_HEIGHT)

TOKENS_PER_WIDTH =  int(PAGE_WIDTH_INCH/IMG_SIZE_INCH)
TOKENS_PER_HEIGHT = int(PAGE_HEIGHT_INCH/IMG_SIZE_INCH)
TOKENS_PER_SHEET = TOKENS_PER_WIDTH*TOKENS_PER_HEIGHT

REMINDERS_PER_WIDTH =  int(PAGE_WIDTH_INCH/REMINDER_SIZE_INCH)
REMINDERS_PER_HEIGHT = int(PAGE_HEIGHT_INCH/REMINDER_SIZE_INCH)
REMINDERS_PER_SHEET = REMINDERS_PER_WIDTH*REMINDERS_PER_HEIGHT

DIRECTION = 'rtl'
for k in SCRIPTS.keys():
    path = f'{ROOT_DIR}\\resources\\scripts\\{utils.kebab2snake(k)}.json'
    # print(path)
    SCRIPTS[k] = json.load(open(path,'r',encoding='utf8'))
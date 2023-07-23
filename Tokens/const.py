from PIL import Image
import json
import utils
import numpy as np
# ROOT_DIR = ''
ROOT_DIR = 'Tokens\\'
groups = ['tb','bmr','snv','fabled']
__TOKEN_BG = {
        None:Image.open(rf'{ROOT_DIR}resources\token_bg.png').resize((512,512))
} | {
    group:Image.open(rf'{ROOT_DIR}resources\{group}_token_bg.png').resize((512,512)) for group in groups
}
def TOKEN_BG(group=None):
    return __TOKEN_BG[group].copy()

MAX_LEAVES_GROUP = {
    None:6,
    'tb':5,
    'bmr':5,
    'snv':7,
    'fabled':4,
}
MAX_LEAVES = min(MAX_LEAVES_GROUP.values())
__TOP_LEAF = {
    None:[Image.open(rf'{ROOT_DIR}resources\top_leaf_{k}.png').resize((512,512)) for k in range(1,MAX_LEAVES_GROUP[None]+1)]
} | {
    group:[Image.open(rf'{ROOT_DIR}resources\{group}_top_leaf_{k}.png').resize((512,512)) for k in range(1,MAX_LEAVES_GROUP[group]+1)] for group in groups
}
    # __TOP_LEAF = __TOP_LEAF.resize((512,512))
def TOP_LEAF(n,group=None):
    n = min(n,MAX_LEAVES_GROUP[group])
    return __TOP_LEAF[group][n-1].copy()


__LEFT_LEAF = {
        None:Image.open(rf'{ROOT_DIR}resources\left_leaf.png').resize((512,512))
} | {
    group:Image.open(rf'{ROOT_DIR}resources\{group}_left_leaf.png').resize((512,512)) for group in groups
}
# __LEFT_LEAF = Image.open(rf'{ROOT_DIR}resources\left_leaf.png')
# __LEFT_LEAF = __LEFT_LEAF.resize((512,512))
def LEFT_LEAF(group=None):
    return __LEFT_LEAF[group].copy()

__RIGHT_LEAF = {
        None:Image.open(rf'{ROOT_DIR}resources\right_leaf.png').resize((512,512))
} | {
    group:Image.open(rf'{ROOT_DIR}resources\{group}_right_leaf.png').resize((512,512)) for group in groups
}
# __RIGHT_LEAF = Image.open(rf'{ROOT_DIR}resources\right_leaf.png')
# __RIGHT_LEAF = __RIGHT_LEAF.resize((512,512))
def RIGHT_LEAF(group=None):
    return __RIGHT_LEAF[group].copy()

__ORANGE_LEAF = {
        None:Image.open(rf'{ROOT_DIR}resources\orange_leaf.png').resize((512,512))
} | {
    group:Image.open(rf'{ROOT_DIR}resources\{group}_orange_leaf.png').resize((512,512)) for group in groups
}
# __ORANGE_LEAF = Image.open(rf'{ROOT_DIR}resources\orange_leaf.png')
# __ORANGE_LEAF = __ORANGE_LEAF.resize((512,512))
def ORANGE_LEAF(group=None):
    return __ORANGE_LEAF[group].copy()

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

DIRECTION = 'ltr'
# FONT_PATH = rf'{ROOT_DIR}resources\he_font.ttf'

# DIRECTION = 'ltr'
# FONT_PATH = rf'{ROOT_DIR}resources\en_font.ttf'
# FONT_PATH = rf'{ROOT_DIR}resources\Arshaq.ttf'
# FONT_PATH = rf'{ROOT_DIR}resources\Mogan.ttf'
def FONT_PATH():
    if DIRECTION=='rtl':
        return rf'{ROOT_DIR}resources\he_font.ttf'
    if DIRECTION=='ltr':
        return rf'{ROOT_DIR}resources\en_font.ttf'
def NAME_FONT_PATH():
    if DIRECTION=='rtl':
        return rf'{ROOT_DIR}resources\he_font.ttf'
    if DIRECTION=='ltr':
        return rf'{ROOT_DIR}resources\en_font_name.ttf'
def FONT_SIZE():
    if DIRECTION=='rtl':
        return 18
    if DIRECTION=='ltr':
        return 23
def LETTER_WIDTH():
    if DIRECTION=='rtl':
        return 1/3
    if DIRECTION=='ltr':
        return 1/5

for k in SCRIPTS.keys():
    path = f'{ROOT_DIR}resources\\scripts\\{utils.kebab2snake(k)}.json'
    # print(path)
    # SCRIPTS[k] = json.load(open(path,'r',encoding='utf8'))
    SCRIPTS[k] = json.load(open(path,'r',encoding='utf8'))
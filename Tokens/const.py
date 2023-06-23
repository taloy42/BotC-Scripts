from PIL import Image
import json
import utils
__TOKEN_BG = Image.open('token_bg.png')
__TOKEN_BG = __TOKEN_BG.resize((512,512))
def TOKEN_BG():
    return __TOKEN_BG.copy()

SCRIPTS = {
    'trouble-brewing':None,
    'sects-and-violets':None,
    'bad-moon-rising':None,
    'all-roles':None
}


for k in SCRIPTS.keys():
    SCRIPTS[k] = json.load(open(f'{utils.kebab2snake(k)}.json','r'))
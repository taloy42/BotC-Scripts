#imports
import requests
import const
import token_creation as tc
import sheet_creation as sc
import json
import os
from tqdm import tqdm
import utils
# import click


def gen_imgs_for_script(script_dir,script,out_dir):
    # read script
    script_json = json.load(open(f'{os.path.join(script_dir,script)}.json','r'))
    # generate images
    imgs = [(ch['id'],tc.create_token_ch(ch)) for ch in script_json]
    # save images
    for id,img in imgs:
        img.save(f'{out_dir}/{id}.png')

def gen_sheets_for_script(script_dir,script,out_dir):
    # read script
    script_json = json.load(open(f'{os.path.join(script_dir,script)}.json','r'))
    # generate images
    imgs = [tc.create_token_ch(ch) for ch in script_json]
    # generate sheets
    # sheets = sc.create_sheets(imgs)
    sheets = sc.generate_sheets(imgs)
    # save sheets
    for i,sheet in enumerate(sheets):
        sheet.save(f'{out_dir}/{i}.png')

def f():
    const.DIRECTION = 'poop'
def load_script_from_url(url):
    resp = requests.get(url)
    return json.loads(resp.content)

def load_local_script(name):
    path = f'{const.ROOT_DIR}resources\\scripts\\{name}.json'
    # print(path)
    # SCRIPTS[k] = json.load(open(path,'r',encoding='utf8'))
    return json.load(open(path,'r',encoding='utf8'))
def main():
    # script = const.SCRIPTS['trouble-brewing']
    script = const.SCRIPTS['all-roles']
    # script = load_script_from_url('https://www.bloodstar.xyz/p/taloy/fabled_for_the_storytellers/script.json?7e75943c')
    # script = load_local_script('fallofrome')
    # script = load_script_from_url(r'https://www.bloodstar.xyz/p/AlexS/Fall_of_Rome/script.json')
    const.DIRECTION = 'rtl'
    # const.GROUP = 'tb'
    if script[0]['id'] == '_meta':
        script = script[1:]
    imgs = [tc.create_token_ch(ch) for ch in tqdm(script[:])]
    while None in imgs:
        imgs.remove(None)
    imgs = utils.flatten_list(imgs)
    # print(imgs)
    sheets = sc.generate_sheets(imgs)
    
    sheet_path = 'sheets\\allroles'

    if not os.path.exists(sheet_path):
        os.makedirs(sheet_path,exist_ok=True)
    
    for i,sheet in enumerate(tqdm(sheets)):
        sheet.save(os.path.join(sheet_path,f'{i}.png'))

if __name__=='__main__':
    main()
    # script = const.SCRIPTS['all-roles'] 
    # script = json.load(open(r'C:\Users\anukh\Downloads\BotC\repository\BotC-Scripts\Tokens\resources\scripts\all_roles_en.json','r'))
    # b = []
    # for c in script:
    #     n = len(c.get('reminders',[]))
    #     if n>1:
    #         # print(c.get('name'),n)   
    #         b.append((n,c['name']))
    # b.sort()
    # for x,y in b:
    #     print(y,x)
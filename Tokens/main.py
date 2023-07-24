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

def gen_sheets_for_script(script,sheet_path = '.\\sheets',script_name='unnamed script'):
    meta = dict()
    if script[0]['id'] == '_meta':
        meta,script = script[0],script[1:]
    name = meta.get('name',script_name)
    token_path = os.path.join(sheet_path,name,'Tokens')
    reminder_path = os.path.join(sheet_path,name,'Reminders')
    imgs = [tc.create_token_ch(ch) for ch in tqdm(script)]
    while None in imgs:
        imgs.remove(None)
    imgs = utils.flatten_list(imgs)
    sheets = sc.generate_sheets(imgs)

    if not os.path.exists(token_path):
        os.makedirs(token_path,exist_ok=True)
    
    for i,sheet in enumerate(tqdm(sheets)):
        sheet.save(os.path.join(token_path,f'{name}_{i}.png'))
    
    reminders = [tc.create_reminders_ch(ch) for ch in tqdm(script)]
    while None in reminders:
        reminders.remove(None)
    reminders = utils.flatten_list(reminders)
    sheets = sc.generate_sheets(reminders,mode='reminders')

    if not os.path.exists(reminder_path):
        os.makedirs(reminder_path,exist_ok=True)
    
    for i,sheet in enumerate(tqdm(sheets)):
        sheet.save(os.path.join(reminder_path,f'{name}_{i}.png'))

def main():
    # script = const.SCRIPTS['trouble-brewing']
    # script = const.SCRIPTS['all-roles']
    # script = json.load(open(r'C:\Users\anukh\Downloads\BotC\repository\BotC-Scripts\Tokens\resources\scripts\all_roles_en_underscore.json','r'))
    script = json.load(open(r'C:\Users\anukh\Downloads\BotC\repository\BotC-Scripts\Tokens\resources\scripts\he_IL.json','r',encoding='utf8'))
    
    if script[0]['id']=='_meta' and 'direction' in script[0]:
        const.DIRECTION = script[0]['direction']
    const.DIRECTION = 'rtl'
    sheet_path = 'sheets'
    gen_sheets_for_script(script,sheet_path,script_name='all_roles_he')

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
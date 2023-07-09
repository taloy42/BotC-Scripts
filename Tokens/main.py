#imports
import const
import token_creation as tc
import sheet_creation as sc
import json
import os
from tqdm import tqdm
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

if __name__=='__main__':
    script = const.SCRIPTS['all-roles']
    imgs = [tc.create_token_ch(ch) for ch in tqdm(script)]
    sheets = sc.generate_sheets(imgs)
    
    sheet_path = 'sheets'

    if not os.path.exists(sheet_path):
        os.makedirs(sheet_path,exist_ok=True)
    
    for i,sheet in enumerate(sheets):
        sheet.save(os.path.join(sheet_path,f'{i}.png'))
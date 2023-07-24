from math import ceil
import utils
import const
from PIL import Image

def create_sheets(imgs):
  return (generate_sheet(chunk) for chunk in utils.split(imgs,6*4))
def generate_sheet(imgs):
  assert len(imgs)<=6*4
  rows = [utils.img_concat(chunk) for chunk in utils.split(imgs,4)]
  return utils.img_concat(rows,horizontal=False)

def idx_to_tabular(idx,mode='tokens'):
  if mode=='tokens':
    per_sheet, per_width = const.TOKENS_PER_SHEET,const.TOKENS_PER_WIDTH 
  elif mode=='reminders':
    per_sheet, per_width = const.REMINDERS_PER_SHEET,const.REMINDERS_PER_WIDTH
  sheet_num = idx//per_sheet
  idx_in_sheet = idx%per_sheet
  idx_col = idx_in_sheet%per_width
  idx_row = idx_in_sheet//per_width
  return (sheet_num,idx_row,idx_col)

def list_total_items(lst):
  total = 0
  for x in lst:
    if isinstance(x,list):
      total += list_total_items(x)
    else:
      total += 1
  return total

def generate_sheets(imgs,mode='tokens'):
  # print('here')
  imgs = utils.flatten_list(imgs)
  total_tokens = len(imgs)
  # total_tokens = list_total_items(imgs)
  if mode=='tokens':
    num_sheets = ceil(total_tokens/const.TOKENS_PER_SHEET)
    sheets = [Image.new("RGBA", const.PAGE_SIZE, (0,0,0,0)) for i in range(num_sheets)]
    
    x_space = (const.PAGE_WIDTH - const.TOKENS_PER_WIDTH*const.IMG_SIZE)//(const.TOKENS_PER_WIDTH+1)
    y_space = (const.PAGE_HEIGHT - const.TOKENS_PER_HEIGHT*const.IMG_SIZE)//(const.TOKENS_PER_HEIGHT+1)
    
    box_side = const.IMG_SIZE + min(x_space,y_space)
  elif mode=='reminders':
    num_sheets = ceil(total_tokens/const.REMINDERS_PER_SHEET)
    sheets = [Image.new("RGBA", const.PAGE_SIZE, (0,0,0,0)) for i in range(num_sheets)]

    x_space = (const.PAGE_WIDTH - const.REMINDERS_PER_WIDTH*const.REMINDER_SIZE)//(const.REMINDERS_PER_WIDTH+1)
    y_space = (const.PAGE_HEIGHT - const.REMINDERS_PER_HEIGHT*const.REMINDER_SIZE)//(const.REMINDERS_PER_HEIGHT+1)
    
    box_side = const.REMINDER_SIZE + min(x_space,y_space)
  else:
    raise Exception('not right mode!')
    return
  for idx,img in enumerate(imgs):
    sheet_num,idx_row,idx_col = idx_to_tabular(idx,mode=mode)
    x = x_space+idx_col*box_side
    y = y_space+idx_row*box_side
    sheets[sheet_num].paste(img,(x,y)) 
  
  # for i,s in tqdm(enumerate(sheets)):
  #   s.save(f'sheet_{i}.png')
  return sheets
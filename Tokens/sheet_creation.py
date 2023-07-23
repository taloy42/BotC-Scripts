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

def idx_to_tabular(idx):
  sheet_num = idx//(const.TOKENS_PER_SHEET)
  idx_in_sheet = idx%(const.TOKENS_PER_SHEET)
  idx_col = idx_in_sheet%const.TOKENS_PER_WIDTH
  idx_row = idx_in_sheet//const.TOKENS_PER_WIDTH
  return (sheet_num,idx_row,idx_col)

def list_total_items(lst):
  total = 0
  for x in lst:
    if isinstance(x,list):
      total += list_total_items(x)
    else:
      total += 1
  return total

def generate_sheets(imgs):
  # print('here')
  imgs = utils.flatten_list(imgs)
  total_tokens = len(imgs)
  # total_tokens = list_total_items(imgs)
  num_sheets = ceil(total_tokens/const.TOKENS_PER_SHEET)
  sheets = [Image.new("RGBA", const.PAGE_SIZE, (0,0,0,0)) for i in range(num_sheets)]

  x_space = (const.PAGE_WIDTH - const.TOKENS_PER_WIDTH*const.IMG_SIZE)//(const.TOKENS_PER_WIDTH+1)
  y_space = (const.PAGE_HEIGHT - const.TOKENS_PER_HEIGHT*const.IMG_SIZE)//(const.TOKENS_PER_HEIGHT+1)
  
  box_side = const.IMG_SIZE + min(x_space,y_space)

  for idx,img in enumerate(imgs):
    sheet_num,idx_row,idx_col = idx_to_tabular(idx)
    x = x_space+idx_col*box_side
    y = y_space+idx_row*box_side
    sheets[sheet_num].paste(img,(x,y)) 
  
  # for i,s in tqdm(enumerate(sheets)):
  #   s.save(f'sheet_{i}.png')
  return sheets
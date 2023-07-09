import utils
import const
from PIL import ImageDraw,ImageFont

def create_token(name,img,text):

  # put image on background
  res = utils.add_img_to_bg(img,const.TOKEN_BG())
  W,H = res.size
  
  
  draw = ImageDraw.Draw(res)
  # add ability text
  font = ImageFont.truetype(font=const.FONT_PATH, size=20)
  s = font.getsize(name)
  # draw.multiline_text(((W-s[0])//2,50),text,font=font,align='right',fill='black',)
  font = get_optimal_multiline_font(const.FONT_PATH,text,H*5/16,im_size=H)
  draw_multiline(draw,res.size,font,text)
  # add name
  # font = ImageFont.truetype(font='dorian2.ttf', size=50)
  font = get_optimal_font(const.FONT_PATH,name,W*7/12)
  s = font.getsize(name)
  draw.text(((W-s[0])//2,int(512*19/24)),name,font=font,align='right',fill='black')

  return res
def create_token_ch(character):
  image = utils.url_to_image(character['image']).resize((const.IMG_SIZE,const.IMG_SIZE))
  return create_token(character['name'],image,character['ability'])
# def cv2_to_PIL(img):
#   img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#   im_pil = Image.fromarray(img)
#   return im_pil
def get_optimal_font_size(font_path,text,width,is_width=True):
  for size in range(50,1,-1):
    font = ImageFont.truetype(font=font_path, size=size)
    s = font.getsize(text)
    
    if s[is_width] < width:
      return size
  return 1
def get_optimal_font(font_path,text,width,is_height=False):
  for size in range(50,1,-1):
    font = ImageFont.truetype(font=font_path, size=size)
    s = font.getsize(text)
    
    if s[int(is_height)] < width:
      break
  return font
def get_optimal_multiline_size(font_path,text,max_height,min_height=60,im_size=512):
  for size in range(50,1,-1):
    font = ImageFont.truetype(font=font_path, size=size)
    if check_multiline_font(font,text,max_height,min_height,im_size):
      return size
  return 1
def get_optimal_multiline_font(font_path,text,max_height,min_height=60,im_size=512):
  for size in range(50,1,-1):
    font = ImageFont.truetype(font=font_path, size=size)
    if check_multiline_font(font,text,max_height,min_height,im_size):
      break
  return font
def draw_multiline(draw,size,font,text,min_height=60):
  W,H = size
  # R = get_diam_for_size(W)
  R = W//2
  h = min_height
  later = text
  while later is not None:
    now, later = split_by_width(font,width4height(h,R),later)
    s = font.getsize(now)
    draw.text(((W-s[0])//2,h),now,fill='black',font=font)
    h+=font.getsize(now)[1]
  return draw
def check_multiline_font(font,text,max_height,min_height=60,im_size=512):
  h = min_height
  later = text
  # R = get_diam_for_size(im_size)
  R = im_size//2
  while later is not None:
    now, later = split_by_width(font,width4height(h,R),later)
    h+=font.getsize(now)[1]
  return h<=max_height
def split_by_width(font,width,text):
  words = text.split(' ')
  if len(words)<=1:
    return text,None
  check = ''
  for i in range(len(words)+1):
    if i==len(words):
      break
    check += words[i]
    if font.getsize(check)[0]>width:
      break
  if i==0:
    return words[0], ' '.join(words[1:])
  return ' '.join(words[:i]),' '.join(words[i:])
def get_diam_for_size(size,perc=5):
  return size*(1-2*perc/100)
def width4height(height,R,p=5):
  '''
  allowed width for given height in circle with diameter diam
  '''
  p = 1-2*p/100
  h = height - R*(1-p)
  delta = (p**2-1)*R**2+2*R*height-height**2
  if delta<0:
    return 0

  return 2*(delta)**0.5
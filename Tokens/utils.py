from PIL import Image, ImageChops
import requests
from io import BytesIO
import os

def kebab2snake(m):
   return m.replace('-','_')
def split(list_a, chunk_size):
  for i in range(0, len(list_a), chunk_size):
    yield list_a[i:i + chunk_size]

def img_concat(images,horizontal=True,pad_percent=5):
  widths, heights = zip(*(i.size for i in images))
  n = len(images)
  max_width = max(widths)
  max_height = max(heights)
  w_pad = int(max_width*pad_percent/100)
  h_pad = int(max_height*pad_percent/100)
  total_width = sum(widths) + (n-1)*w_pad
  total_height = sum(heights) + (n-1)*h_pad
  if horizontal:
    nwidth, nheight = total_width, max_height
  else:
    nwidth, nheight = max_width, total_height
  new_im = Image.new('RGBA', (nwidth, nheight))
  if horizontal:    
    x_offset = 0
    for im in images:
      new_im.paste(im, (x_offset,0))
      x_offset += im.size[0] + w_pad
  else:
    y_offset = 0
    for im in images:
      new_im.paste(im, (0,y_offset))
      y_offset += im.size[1] + h_pad
  return new_im

def url_to_image(url):
  '''
  turn white to transparent
  '''
  if os.path.exists(os.path.exists(url)):
    img = Image.open(url)
  else:
    print(url)
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
  # img = img.convert("RGBA")
  
  # pixdata = img.load()
  # width, height = img.size
  # for y in range(height):
  #     for x in range(width):
  #         if pixdata[x, y] == (255, 255, 255, 255):
  #             pixdata[x, y] = (255, 255, 255, 0)
  return img

def crop_image(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)
def expand2square(pil_img, background_color=(0,0,0,0)):
    width, height = pil_img.size
    if width == height:
        return pil_img
    elif width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        result.paste(pil_img, (0, (width - height) // 2))
        return result
    else:
        result = Image.new(pil_img.mode, (height, height), background_color)
        result.paste(pil_img, ((height - width) // 2, 0))
        return result
def crop_and_square(image,pixel_value=0):
  return expand2square(crop_image(image))
def overlay(background,foreground):
  res = background.copy()
  res.paste(foreground, (0, 0), foreground)
  return res
def position_foreground(img,bg_size,fg_size,fg_loc):
  img = img.resize(fg_size)
  bg = Image.new('RGBA',bg_size,color=(0,0,0,0))
  bg.paste(img,fg_loc,img)
  return bg
def add_img_to_bg(img,bg,perc=0.5,loc=None):
  img = crop_and_square(img)
  W,H = bg.size
  size = int(H*perc)
  if loc is None:
    offset = (1-perc)
    loc = (int(W*offset/2),int(H*7*offset/12))
  resized = position_foreground(img,(W,H),(size,size),loc)
  res = overlay(bg,resized)
  return res
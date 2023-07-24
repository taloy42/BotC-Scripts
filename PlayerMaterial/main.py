import const
from PIL import Image,ImageFont,ImageDraw
import requests
from io import BytesIO
import os

def order_script(script):
    if len(script)==0:
        return []
    if isinstance(script[0],dict):
        script = [x['id'] for x in script]
    script = [x for x in const.JSON if x['id'] in script or x['team']=='reminders']
    firstNight = sorted(filter(lambda x:x['firstNight']>=0,script),key=lambda x:x['firstNight'])
    otherNight = sorted(filter(lambda x:x['otherNight']>=0,script),key=lambda x:x['otherNight'])
    return firstNight, otherNight
def url_to_image(url):
    '''
    turn white to transparent
    '''
    if isinstance(url,list):
        return [url_to_image(u) for u in url]
    if os.path.isfile(url):
        img = Image.open(url)
    else:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
    return img
def generate_line_image(role,width,height,name_width,time='firstNight'):
    name = role['name']
    image_uri = role['image']
    reminder = role[f'{time}Reminder']
    
    image_size = (height*9)//10
    image = url_to_image(image_uri).resize((image_size,image_size))
    bg = Image.new('RGBA',(width,height),(0,0,0,0))
    locx = height//20
    locy = height//20
    bg.paste(image,(locx,locy),image)
    locx += image_size
    bg.show()

# print([x['id'] for x in order_script([
#     'washerwoman',
#     'spy',
#     'ravenkeeper',
#     'chef',
#     'imp'
# ])[1]])
d = {'id': 'dusk', 'name': 'Dusk', 'ability': '', 'firstNightReminder': 'Start the Night Phase.', 'otherNightReminder': 'Start the Night Phase.', 'reminders': [], 'firstNight': 0, 'otherNight': 0, 'team': 'reminders', 'edition': float('nan'), 'setup': False, 'image': 'https://raw.githubusercontent.com/taloy42/BotC-Scripts/main/Resources/Icons/dusk.png'}
generate_line_image(d,500,100)
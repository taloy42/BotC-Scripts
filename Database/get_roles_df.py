from tqdm import tqdm
# from tqdm.notebook import tqdm
import requests
import json
from bs4 import BeautifulSoup
from lxml import etree
import urllib
import pandas as pd

def name2urlparam(s):
  return urllib.parse.quote_plus(s).replace('+','_')

def name2id(s):
  return urllib.parse.unquote(s.replace(' ','_').replace('\'','').lower())

def get_category_dict(category):
  URL = f"https://wiki.bloodontheclocktower.com/Category:{category}"
  xpath=r'//*[@id="mw-pages"]/div/div/div/ul/li/a'
  webpage = requests.get(URL)
  soup = BeautifulSoup(webpage.content, "html.parser")
  dom = etree.HTML(str(soup))
  a = dom.xpath(xpath)
  print('getting category:',category)
  return {
      name2id(aa.attrib['title']):
      {
          'urlparam':name2urlparam(aa.attrib['title']),
          'name':aa.attrib['title'],
          'team':category,
          }
      for aa in tqdm(a)
      }

def get_sao_dict():
  URL = r'https://botc-tools.vercel.app/sao-sorter/order.json'
  resp = requests.get(URL)
  order = json.loads(resp.content)
  order_dict = {k:dict(zip(['team_idx','order','ver_major','ver_minor'],map(int,v.split('.')))) for k,v in order.items()}
  return order_dict

def get_role_desc(role):
  URL = f"https://wiki.bloodontheclocktower.com/{role}"
  xpath=r'//*[@id="mw-content-text"]/div/div/div[2]/div[1]/div[1]/p[1]'
  webpage = requests.get(URL)
  soup = BeautifulSoup(webpage.content, "html.parser")
  dom = etree.HTML(str(soup))
  p = dom.xpath(xpath)
  if p:
    return p[0].text.strip('" \n\t\r')
  return None

def get_setup_for_role(role):
  desc = role['desc']
  start = desc.find('[')+1
  end = desc.find(']')
  if start*end <= 0:
    return None
  return desc[start:end]

def get_botc_roles_df():
  categories = [
      'townsfolk',
      'outsiders',
      'minions',
      'demons',
      'travellers',
      'fabled'
  ]
  roles = {k:v for category in categories for k,v in get_category_dict(category).items()}
  order = get_sao_dict()
  def_traveller = {
      'team_idx':5,
      'order':100,
      'ver_major':0,
      'ver_minor':0,
  }
  def_fabled = {
      'team_idx':6,
      'order':101,
      'ver_major':0,
      'ver_minor':0,
  }
  print("updating each role")
  for idx,role in tqdm(roles.items()):
    role.update(order.get(idx,
                          def_traveller if role['team']=='travellers' else def_fabled))
    role['desc'] = get_role_desc(role['urlparam'])
    role['setup'] = get_setup_for_role(role)
  # return roles

  df = pd.DataFrame(roles.values(), index = roles.keys())
  return df

if __name__=='__main__':
    df_roles = get_botc_roles_df()
    df_roles.to_csv('roles.csv')
    # df_roles.sample(frac=1).head()
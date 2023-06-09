# -*- coding: utf-8 -*-
"""get_all_roles_botc

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ecoYKRynve_kWV1CbtFdPpntMqFsacma

# Roles DataFrame
table of all the roles contatining:

key       | value
-         | -
index     | name of role as id(lowercase with spaces "` `" as underscores "`_`")
urlparam  | as parameter to the wiki|official name
name      | official name of the character
team      | townsfolk\outsider\minion\demon\traveller\fabled
team_idx  | mapping of the teams to ids
order     | order in the script (Standard Amy Order)
ver_major | version in the sao.json
ver_minor | version in the sao.json
desc      | description of the role
setup     | setup text for the role
"""

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
df_roles = get_botc_roles_df()
df_roles.to_csv('roles.csv')
df_roles.sample(frac=1).head()

"""# Scripts DataFrame

table of all the roles contatining:

key         | value
-           | -
index       | id of the script
name        | name of the script
characters  | all the characters in the script separated by commas (no spaces)
type        | full\teensyville
json        | json of the script (for online.clocktower and the such)
len         | number of characters in the script

"""

from tqdm import tqdm
# from tqdm.notebook import tqdm
import requests
import json
import pandas as pd

def get_scripts(**search_params):
  '''
  search params:
    script_type: Union['Full','Teensyville']
  '''
  api_url = 'https://botc-scripts.azurewebsites.net/api/scripts/'
  resp = requests.get(api_url,params=search_params)
  cur = json.loads(resp.content)
  n_scripts = int(cur['count'])
  # p_bar = tqdm(range(n_scripts))
  scripts = []
  # i=0
  with tqdm(total=n_scripts) as p_bar:
    while cur.get('next') is not None:
      # i+=1
      # if i%10==0:
      #   print(i)
      curres = cur['results']
      cur_n = len(curres)
      scripts.extend(curres)
      cur = json.loads(requests.get(cur['next']).content)
      p_bar.update(cur_n)
      p_bar.refresh()
    scripts.extend(cur['results'])
    p_bar.update(len(cur['results']))
    p_bar.refresh()
  return scripts

def update_scripts(scripts,script_type,scripts_dict=None):
  if scripts_dict is None:
    scripts_dict = {
      'name':[],
      'characters':[],
      'type':[],
      'json':[]
    }
  for scr in scripts:
    scrc = scr['content']
    if 'name' not in scrc[0].keys() and 'name' in scr.keys():
      if scrc[0].get('id')=='_meta':
        scrc[0]['name'] = scr['name']
      else:
        scrc = [{'id':'_meta',
                 'name':scr['name']}] + scrc
    d = {
      'name':scr.get('name') or scrc[0].get('name'),
      'characters':','.join(map(lambda x:x['id'],scrc)).replace('_meta','').strip(','),
      'type':script_type,
      'json':json.dumps(scrc),
    }
    for k in scripts_dict.keys():
      scripts_dict[k].append(d[k])
  return scripts_dict

def get_botc_scripts_df():
  print('loading teensy...')
  teensy = get_scripts(script_type='Teensyville')
  print('teensy loading done. loading full...')
  full = get_scripts(script_type='Full')
  print('full loading done.')

  scripts_dict = update_scripts(full,'full')
  scripts_dict = update_scripts(teensy,'teensy',scripts_dict)

  df = pd.DataFrame(scripts_dict)
  df['len']=df['characters'].apply(lambda x:len(x.split(',')))

  return df

df_scripts = get_botc_scripts_df()
df_scripts.to_csv('scripts.csv')
df_scripts.sample(frac=1).head()

"""## Searching in the scripts DataFrame"""

def bare_string(s):
  if s is None:
    return None
  return s.lower().replace('\'','').replace('"','').replace('-',' ').replace('_',' ')


def characters_in_play_mask(df,characters):
  return df['characters'].apply(lambda x:x.split(',')).apply(lambda x:set(characters) <= set(x))

def like_name_mask(df,name):
  return df['name'].apply(bare_string).str.contains(bare_string(name))

def is_type_mask(df, script_type):
  return df['type']==script_type


def search_scripts(df, **search_params):
  name = bare_string(search_params.get('name'))
  script_type = search_params.get('type')
  characters = search_params.get('characters')


  true_mask = pd.Series([True for n in df.index])

  has_name = true_mask if name is None else like_name_mask(df,name)
  is_type = true_mask if script_type is None else is_type_mask(df,script_type)
  characters_in_play = true_mask if characters is None else characters_in_play_mask(df,characters)

  return df[has_name & is_type & characters_in_play]

search_scripts(df_scripts,characters=['atheist','lycanthrope'],type='teensy')
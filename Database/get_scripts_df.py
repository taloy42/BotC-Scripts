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

if __name__=='__main__':
    df_scripts = get_botc_scripts_df()
    df_scripts.to_csv('scripts.csv')
    # df_scripts.sample(frac=1).head()
    # search_scripts(df_scripts,characters=['atheist','lycanthrope'],type='teensy')
import json
ROOT_DIR = 'PlayerMaterial\\'
JSON_PATH = f'{ROOT_DIR}resources\\en_GB.json'
JSON = json.load(open(JSON_PATH,'r',encoding='utf8'))
ORDER = {x['id']:{
    'firstNight':x['firstNight'],
    'otherNight':x['otherNight'],
    'firstNightReminder':x['firstNightReminder'],
    'otherNightReminder':x['otherNightReminder']
    } for x in JSON}

def COMPARE(id1,id2,time='firstNight'):
    return ORDER[id1][time]<ORDER[id2][time]
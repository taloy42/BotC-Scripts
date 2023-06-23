import json
import os
import pandas as pd

def load_json(dir,file_name):
    with open(os.path.join(dir,file_name+".json"),encoding='utf8') as fp:
        data = json.load(fp)
    return data

def dump_json(obj,dir,file_name):
    with open(os.path.join(dir,file_name+'.json'),'w',encoding='utf8') as fp:
        json.dump(obj,fp,indent=4,ensure_ascii=False)

def read_csv(dir,file,index=0):
    return pd.read_csv(os.path.join(dir,file+'.csv'),index_col=index,encoding='utf8').fillna('')
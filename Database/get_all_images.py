import requests
import json
from PIL import Image
import os
import io
from tqdm import tqdm
import re
def name_to_id(name):
    return re.sub('[-_ "\']',"",name.lower())
def url_to_image(url):
    """
    turn white to transparent
    """
    if isinstance(url, list):
        return [url_to_image(u) for u in url]
    if os.path.isfile(url):
        img = Image.open(url)
    else:
        response = requests.get(url)
        img = Image.open(io.BytesIO(response.content))
    return img


def get_images_list():
    r = requests.get(
        r"https://wiki.bloodontheclocktower.com/api.php?action=query&format=json&list=allimages&aiprefix=Icon&ailimit=500"
    ).content
    j = json.loads(r)["query"]["allimages"]

    for x in tqdm(j):
        img = url_to_image(x["url"])
        name = name_to_id(x["name"][5:])
        save_path = "Resources\\Icons\\new\\"
        os.makedirs(save_path, exist_ok=True)
        img.save(save_path + name)


get_images_list()

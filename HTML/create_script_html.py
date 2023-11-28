import json
import re

global_json_path = "en_GB.json"

global_json = json.load(open(global_json_path, "r", encoding="utf-8"))
global_dct = {d["id"]: d for d in global_json}
script_str = """
  [
  "artist",
  "barber",
  "barista",
  "bonecollector",
  "butcher",
  "cerenovus",
  "clockmaker",
  "deviant",
  "dreamer",
  "eviltwin",
  "fanggu",
  "flowergirl",
  "harlot",
  "juggler",
  "klutz",
  "mathematician",
  "mutant",
  "nodashii",
  "oracle",
  "philosopher",
  "pithag",
  "sage",
  "savant",
  "seamstress",
  "snakecharmer",
  "sweetheart",
  "towncrier",
  "vigormortis",
  "vortox",
  "witch"
]
  """


def script_from_str(script_str):
    l = json.loads(script_str)
    return [global_dct[id] for id in l]


def uri_from_github(id):
    return f"https://raw.githubusercontent.com/taloy42/BotC-Scripts/main/Resources/Icons/{id}.png"


def generate_row(role):
    id = role["id"]
    name = role["name"]
    ability = role["ability"]
    team = role["team"]
    sao = role["sao"]
    img_uri = uri_from_github(id)

    #   return f"""
    #   <div class="role {team}">
    #     <img src="{img_uri}">
    #     <span class="{id} name">{name}</span>
    #     <span class="{id} ability">{ability}</span>
    #   </div>
    #   """.strip()
    return f"""
    <div class="role {team}">
        <img src="{img_uri}"
            alt="{name} image" class="image">
        <span class="name">{name}</span>
        <span class="ability">{ability}</span>
    </div>"""


def generate_group(roles, group):
    html = f'<div class="section {group}">'
    for role in roles:
        html += "\n" + generate_row(role) + "\n"
    html += "</div>"
    return html


def generate_script(script):
    groups = ["townsfolk", "outsider", "minion", "demon", "traveler", "fabled"]
    sao_key = lambda role: role["sao"]
    final = """<!DOCTYPE html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]>      <html class="no-js"> <!--<![endif]-->
<html>

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>botc script</title>
    <meta name="description" content="">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="main.css">
</head>

<body>
    <!--[if lt IE 7]>
            <p class="browsehappy">You are using an <strong>outdated</strong> browser. Please <a href="#">upgrade your browser</a> to improve your experience.</p>
        <![endif]-->"""

    for group in groups:
        l = [role for role in script if role["team"] == group]
        l.sort(key=sao_key)

        final += generate_group(l, group)
    final += """<script src="main.js" async defer></script>
</body>

</html>"""
    soup = BeautifulSoup(final)
    return soup.prettify()


from bs4 import BeautifulSoup

with open("script.html", "w", encoding="utf-8") as f:
    f.write(generate_script(script_from_str(script_str)))

import configparser
import os
import json

import pandas as pd

### PATHS ###
config = configparser.ConfigParser()
config.read(r"pyconfig.ini")
dirs = config["DEFAULT"]
base_folder = ""
json_folder = os.path.join(base_folder, dirs["json"])
description_folder = os.path.join(base_folder, dirs["descriptions"])
script_folder = os.path.join(base_folder, dirs["scripts"])
csv_folder = os.path.join(base_folder, dirs["csv"])


### LOCALES ###
# known_locales = [
#         "ar_AR",
#         "de_DE",
#         "en_GB",
#         "es_ES",
#         "fa_IR",
#         "fil_PH",
#         "fr_FR",
#         "he_IL",
#         "hu_HU",
#         "it_IT",
#         "ja_JA",
#         "kw_KW",
#         "nl_NL",
#         "pl_PL",
#         "pt_BR",
#         "pt_PT",
#         "ru_RU",
#         "sv_SE",
#         "tr_TR",
#         "zh_CN",
#         "zh_TW",
# ]
known_locales = ["en_GB", "he_IL"]

### FOR CSV ###
csv_text_entries = ["name", "ability", "firstNightReminder", "otherNightReminder"]
csv_int_entries = ["firstNight", "otherNight", "sao", "tokenCopies"]
# csv_list_entries =['remindersGlobal', 'reminders']
csv_list_entries = [("reminders", str), ("reminderCopies", int)]


image_pattern = (
    "https://raw.githubusercontent.com/taloy42/BotC-Scripts/main/Resources/Icons/{}.png"
)


### SOURCE FOR TRANSLATION ###
def json_from_df(csv_path):
    df = pd.read_csv(csv_path)
    j = []

    for index, row in df.iterrows():
        cur = dict()
        for key in row.keys():
            cur[key] = row[key]
        cur["image"] = image_pattern.format(cur["id"])
        j.append(cur)
    return j


def json_source():
    if os.path.isfile(os.path.join(csv_folder, "en_GB.csv")):
        return json_from_df(os.path.join(csv_folder, "en_GB.csv"))
    raise Exception("no base json")
    #  return json.loads(


r"""
[
   {
      "ability":"Each night, the 1st player to choose you with their ability is drunk until dusk. You become their alignment.",
      "edition":"bmr",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"goon",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/goon.png?raw=true",
      "name":"Goon",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         "Drunk"
      ],
      "setup":false,
      "team":"outsider"
   },
   {
      "ability":"When a Minion dies by execution, all other players (except Travellers) are drunk until dusk tomorrow.",
      "edition":"bmr",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"minstrel",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/minstrel.png?raw=true",
      "name":"Minstrel",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         "Everyone drunk"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"If you were the player most responsible for your team losing, you change alignment & win, even if dead.",
      "edition":"",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"politician",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/politician.png?raw=true",
      "name":"Politician",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         
      ],
      "setup":false,
      "team":"outsider"
   },
   {
      "ability":"There are extra Outsiders in play. [+2 Outsiders]",
      "edition":"tb",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"baron",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/baron.png?raw=true",
      "name":"Baron",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         
      ],
      "setup":true,
      "team":"minion"
   },
   {
      "ability":"You start knowing a good player & their character. If the Demon kills them, you die too.",
      "edition":"bmr",
      "firstNight":39,
      "firstNightReminder":"Show the marked character token. Point to the marked player.",
      "id":"grandmother",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/grandmother.png?raw=true",
      "name":"Grandmother",
      "otherNight":50,
      "otherNightReminder":"If the Grandmother’s grandchild was killed by the Demon tonight: The Grandmother dies.",
      "reminders":[
         "Grandchild"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"Each night, choose a player: a Minion, if chosen, learns this. All chosen Minions have no ability.",
      "edition":"",
      "firstNight":14,
      "firstNightReminder":"The Preacher chooses a player. If a Minion is chosen, wake the Minion and show the 'This character selected you' card and then the Preacher token.",
      "id":"preacher",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/preacher.png?raw=true",
      "name":"Preacher",
      "otherNight":7,
      "otherNightReminder":"The Preacher chooses a player. If a Minion is chosen, wake the Minion and show the 'This character selected you' card and then the Preacher token.",
      "reminders":[
         "At a sermon"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"Once per game, at night, choose 2 players (not yourself): you learn if they are the same alignment.",
      "edition":"snv",
      "firstNight":42,
      "firstNightReminder":"The Seamstress either shows a 'no' head signal, or points to two other players. If the Seamstress chose players , nod 'yes' or shake 'no' for whether they are of same alignment.",
      "id":"seamstress",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/seamstress.png?raw=true",
      "name":"Seamstress",
      "otherNight":61,
      "otherNightReminder":"If the Seamstress has not yet used their ability: the Seamstress either shows a 'no' head signal, or points to two other players. If the Seamstress chose players , nod 'yes' or shake 'no' for whether they are of same alignment.",
      "reminders":[
         "No ability"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"1 player is drunk, even if you die. If you guess (once) who it is, learn the Demon player, but guess wrong & get false info.",
      "edition":"",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"puzzlemaster",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/puzzlemaster.png?raw=true",
      "name":"Puzzlemaster",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         "Drunk",
         "Guess used"
      ],
      "setup":false,
      "team":"outsider"
   },
   {
      "ability":"You must use a vote token to vote. Dead players may choose to give you theirs. If so, you learn their alignment. You are sober & healthy.",
      "edition":"tb",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"beggar",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/beggar.png?raw=true",
      "name":"Beggar",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         
      ],
      "setup":false,
      "team":"traveler"
   },
   {
      "ability":"Each night*, choose a player: they die. Minions you kill keep their ability & poison 1 Townsfolk neighbour. [−1 Outsider]",
      "edition":"snv",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"vigormortis",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/vigormortis.png?raw=true",
      "name":"Vigormortis",
      "otherNight":32,
      "otherNightReminder":"The Vigormortis points to a player. That player dies. If a Minion, they keep their ability and one of their Townsfolk neighbours is poisoned.",
      "reminders":[
         "Dead",
         "Has ability",
         "Poisoned"
      ],
      "setup":true,
      "team":"demon"
   },
   {
      "ability":"If both your alive neighbours are good, they can't die.",
      "edition":"bmr",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"tealady",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/tealady.png?raw=true",
      "name":"Tea Lady",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         "Can not die"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"You start knowing that 1 of 2 players is a particular Outsider. (Or that zero are in play.)",
      "edition":"tb",
      "firstNight":33,
      "firstNightReminder":"Show the character token of an Outsider in play. Point to two players, one of which is that character.",
      "id":"librarian",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/librarian.png?raw=true",
      "name":"Librarian",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         "Outsider",
         "Wrong"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"Each day, 3 players may choose to visit you. At night*, each visitor learns how many visitors are evil, but 1 gets false info.",
      "id":"duchess",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/duchess.png?raw=true",
      "name":"Duchess",
      "reminders":[
         "False Info",
         "Visitor"
      ],
      "team":"fabled"
   },
   {
      "ability":"Each night*, choose a player (different to last night): the Demon, if chosen, learns who you are then doesn't wake tonight.",
      "edition":"bmr",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"exorcist",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/exorcist.png?raw=true",
      "name":"Exorcist",
      "otherNight":22,
      "otherNightReminder":"The Exorcist points to a player, different from the previous night. If that player is the Demon: Wake the Demon. Show the Exorcist token. Point to the Exorcist. The Demon does not act tonight.",
      "reminders":[
         "Chosen"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"Each night, choose an alive player: either you or they are drunk until dusk. You can't die.",
      "edition":"bmr",
      "firstNight":10,
      "firstNightReminder":"The Sailor points to a living player. Either the Sailor, or the chosen player, is drunk.",
      "id":"sailor",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/sailor.png?raw=true",
      "name":"Sailor",
      "otherNight":4,
      "otherNightReminder":"The previously drunk player is no longer drunk. The Sailor points to a living player. Either the Sailor, or the chosen player, is drunk.",
      "reminders":[
         "Drunk"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"You think you are a good character but you are not. The Demon knows who you are. [You neighbour the Demon]",
      "edition":"",
      "firstNight":11,
      "firstNightReminder":"Select one of the good players next to the Demon and place the Is the Marionette reminder token. Wake the Demon and show them the Marionette.",
      "id":"marionette",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/marionette.png?raw=true",
      "name":"Marionette",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         
      ],
      "remindersGlobal":[
         "Is the Marionette"
      ],
      "setup":true,
      "team":"minion"
   },
   {
      "ability":"You are safe from the Demon.",
      "edition":"tb",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"soldier",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/soldier.png?raw=true",
      "name":"Soldier",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"Each night, choose a player (not yourself): their vote counts as 3 votes tomorrow.",
      "edition":"tb",
      "firstNight":1,
      "firstNightReminder":"The Bureaucrat points to a player. Put the Bureaucrat's '3 votes' reminder by the chosen player's character token.",
      "id":"bureaucrat",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/bureaucrat.png?raw=true",
      "name":"Bureaucrat",
      "otherNight":1,
      "otherNightReminder":"The Bureaucrat points to a player. Put the Bureaucrat's '3 votes' reminder by the chosen player's character token.",
      "reminders":[
         "3 votes"
      ],
      "setup":false,
      "team":"traveler"
   },
   {
      "ability":"Once per game, at night*, choose a player: they die, even if for some reason they could not.",
      "edition":"bmr",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"assassin",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/assassin.png?raw=true",
      "name":"Assassin",
      "otherNight":37,
      "otherNightReminder":"If the Assassin has not yet used their ability: The Assassin either shows the 'no' head signal, or points to a player. That player dies.",
      "reminders":[
         "Dead",
         "No ability"
      ],
      "setup":false,
      "team":"minion"
   },
   {
      "ability":"Each night*, you learn if a Demon voted today.",
      "edition":"snv",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"flowergirl",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/flowergirl.png?raw=true",
      "name":"Flowergirl",
      "otherNight":58,
      "otherNightReminder":"Nod 'yes' or shake head 'no' for whether the Demon voted today. Place the 'Demon not voted' marker (remove 'Demon voted', if any).",
      "reminders":[
         "Demon not voted",
         "Demon voted"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"Each night, you see the Grimoire. You might register as good & as a Townsfolk or Outsider, even if dead.",
      "edition":"tb",
      "firstNight":48,
      "firstNightReminder":"Show the Grimoire to the Spy for as long as they need.",
      "id":"spy",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/spy.png?raw=true",
      "name":"Spy",
      "otherNight":68,
      "otherNightReminder":"Show the Grimoire to the Spy for as long as they need.",
      "reminders":[
         
      ],
      "setup":false,
      "team":"minion"
   },
   {
      "ability":"If you died today or tonight, the Demon may choose 2 players (not another Demon) to swap characters.",
      "edition":"snv",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"barber",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/barber.png?raw=true",
      "name":"Barber",
      "otherNight":40,
      "otherNightReminder":"If the Barber died today: Wake the Demon. Show the 'This character selected you' card, then Barber token. The Demon either shows a 'no' head signal, or points to 2 players. If they chose players: Swap the character tokens. Wake each player. Show 'You are', then their new character token.",
      "reminders":[
         "Haircuts tonight"
      ],
      "setup":false,
      "team":"outsider"
   },
   {
      "ability":"On your 1st night, look at the Grimoire and choose a player: they are poisoned. 1 good player knows a Widow is in play.",
      "edition":"",
      "firstNight":18,
      "firstNightReminder":"Show the Grimoire to the Widow for as long as they need. The Widow points to a player. That player is poisoned. Wake a good player. Show the 'These characters are in play' card, then the Widow character token.",
      "id":"widow",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/widow.png?raw=true",
      "name":"Widow",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         "Poisoned"
      ],
      "remindersGlobal":[
         "Knows"
      ],
      "setup":false,
      "team":"minion"
   },
   {
      "ability":"You start knowing a secret word. The 1st good player to say this word becomes evil that night.",
      "edition":"",
      "firstNight":27,
      "firstNightReminder":"Show the Mezepheles their secret word.",
      "id":"mezepheles",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/mezepheles.png?raw=true",
      "name":"Mezepheles",
      "otherNight":19,
      "otherNightReminder":"Wake the 1st good player that said the Mezepheles' secret word and show them the 'You are' card and the thumbs down evil signal.",
      "reminders":[
         "No ability",
         "Turns evil"
      ],
      "setup":false,
      "team":"minion"
   },
   {
      "ability":"You may only nominate once per game. When you do, if the nominee is not the Demon, they die.",
      "edition":"",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"golem",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/golem.png?raw=true",
      "name":"Golem",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         "Can not nominate"
      ],
      "setup":false,
      "team":"outsider"
   },
   {
      "ability":"Each night*, choose a player: they die. If you kill yourself this way, a Minion becomes the Imp.",
      "edition":"tb",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"imp",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/imp.png?raw=true",
      "name":"Imp",
      "otherNight":24,
      "otherNightReminder":"The Imp points to a player. That player dies. If the Imp chose themselves: Replace the character of 1 alive minion with a spare Imp token. Show the 'You are' card, then the Imp token.",
      "reminders":[
         "Dead"
      ],
      "setup":false,
      "team":"demon"
   },
   {
      "ability":"There can't be more than 1 extra evil player.",
      "id":"spiritofivory",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/spiritofivory.png?raw=true",
      "name":"Spirit Of Ivory",
      "reminders":[
         "No extra evil"
      ],
      "team":"fabled"
   },
   {
      "ability":"Each day, you may choose up to 3 sets of 2 players to swap seats. Players may not leave their seats to talk in private.",
      "edition":"bmr",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"matron",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/matron.png?raw=true",
      "name":"Matron",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         
      ],
      "setup":false,
      "team":"traveler"
   },
   {
      "ability":"Once per game, the Storyteller will make a \"mistake\", correct it and publicly admit to it.",
      "id":"deusexfiasco",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/deusexfiasco.png?raw=true",
      "name":"Deus ex Fiasco",
      "reminders":[
         "Whoops"
      ],
      "team":"fabled"
   },
   {
      "ability":"Each night*, choose 2 players: they die. A dead player you chose last night might be regurgitated.",
      "edition":"bmr",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"shabaloth",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/shabaloth.png?raw=true",
      "name":"Shabaloth",
      "otherNight":27,
      "otherNightReminder":"One player that the Shabaloth chose the previous night might be resurrected. The Shabaloth points to two players. Those players die.",
      "reminders":[
         "Alive",
         "Dead"
      ],
      "setup":false,
      "team":"demon"
   },
   {
      "ability":"If only 3 players live & no execution occurs, your team wins. If you die at night, another player might die instead.",
      "edition":"tb",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"mayor",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/mayor.png?raw=true",
      "name":"Mayor",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"Each night*, you learn which character died by execution today.",
      "edition":"tb",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"undertaker",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/undertaker.png?raw=true",
      "name":"Undertaker",
      "otherNight":56,
      "otherNightReminder":"If a player was executed today: Show that player’s character token.",
      "reminders":[
         "Executed"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"Each night, choose an alive player: a chosen Demon swaps characters & alignments with you & is then poisoned.",
      "edition":"snv",
      "firstNight":20,
      "firstNightReminder":"The Snake Charmer points to a player. If that player is the Demon: swap the Demon and Snake Charmer character and alignments. Wake each player to inform them of their new role and alignment. The new Snake Charmer is poisoned.",
      "id":"snakecharmer",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/snakecharmer.png?raw=true",
      "name":"Snake Charmer",
      "otherNight":12,
      "otherNightReminder":"The Snake Charmer points to a player. If that player is the Demon: swap the Demon and Snake Charmer character and alignments. Wake each player to inform them of their new role and alignment. The new Snake Charmer is poisoned.",
      "reminders":[
         "Poisoned"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"Each night, choose 2 alive players (not yourself): you learn how many woke tonight due to their ability.",
      "edition":"bmr",
      "firstNight":50,
      "firstNightReminder":"The Chambermaid points to two players. Show the number signal (0, 1, 2, …) for how many of those players wake tonight for their ability.",
      "id":"chambermaid",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/chambermaid.png?raw=true",
      "name":"Chambermaid",
      "otherNight":70,
      "otherNightReminder":"The Chambermaid points to two players. Show the number signal (0, 1, 2, …) for how many of those players wake tonight for their ability.",
      "reminders":[
         
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"You do not know what your ability is. Each day, privately guess what it is: you learn how accurate you are.",
      "edition":"",
      "firstNight":12,
      "firstNightReminder":"Decide the Amnesiac's entire ability. If the Amnesiac's ability causes them to wake tonight: Wake the Amnesiac and run their ability.",
      "id":"amnesiac",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/amnesiac.png?raw=true",
      "name":"Amnesiac",
      "otherNight":5,
      "otherNightReminder":"If the Amnesiac's ability causes them to wake tonight: Wake the Amnesiac and run their ability.",
      "reminders":[
         "?"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"Each night*, choose a living player: if good, they die, but they are the only player that can die tonight.",
      "edition":"",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"lycanthrope",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/lycanthrope.png?raw=true",
      "name":"Lycanthrope",
      "otherNight":23,
      "otherNightReminder":"The Lycanthrope points to a living player: if good, they die and no one else can die tonight.",
      "reminders":[
         "Dead"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"2 neighboring players are known to be the same alignment. Once per game, one of them registers falsely",
      "id":"revolutionary",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/revolutionary.png?raw=true",
      "name":"Revolutionary",
      "reminders":[
         "Register Falsely?"
      ],
      "team":"fabled"
   },
   {
      "ability":"If you are executed, all but 3 players die. 1 minute later, the player with the most players pointing at them dies.",
      "edition":"",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"boomdandy",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/boomdandy.png?raw=true",
      "name":"Boomdandy",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         
      ],
      "setup":false,
      "team":"minion"
   },
   {
      "ability":"If the Demon kills you, you learn that it is 1 of 2 players.",
      "edition":"snv",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"sage",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/sage.png?raw=true",
      "name":"Sage",
      "otherNight":43,
      "otherNightReminder":"If the Sage was killed by a Demon: Point to two players, one of which is that Demon.",
      "reminders":[
         
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"Each night*, choose 3 players (all players learn who): each silently chooses to live or die, but if all live, all die.",
      "edition":"",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"alhadikhia",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/alhadikhia.png?raw=true",
      "name":"Al-Hadikhia",
      "otherNight":33,
      "otherNightReminder":"The Al-Hadikhia chooses 3 players. Announce the first player, wake them to nod yes to live or shake head no to die, kill or resurrect accordingly, then put to sleep and announce the next player. If all 3 are alive after this, all 3 die.",
      "reminders":[
         "1",
         "2",
         "3",
         "Chose death",
         "Chose life"
      ],
      "setup":false,
      "team":"demon"
   },
   {
      "ability":"You start knowing that 1 of 2 players is a particular Townsfolk.",
      "edition":"tb",
      "firstNight":32,
      "firstNightReminder":"Show the character token of a Townsfolk in play. Point to two players, one of which is that character.",
      "id":"washerwoman",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/washerwoman.png?raw=true",
      "name":"Washerwoman",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         "Townsfolk",
         "Wrong"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"Each night, choose a player. If you nominate & execute them, their team loses. All players know if you choose a new player.",
      "edition":"",
      "firstNight":26,
      "firstNightReminder":"The Fearmonger points to a player. Place the Fear token next to that player and announce that a new player has been selected with the Fearmonger ability.",
      "id":"fearmonger",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/fearmonger.png?raw=true",
      "name":"Fearmonger",
      "otherNight":18,
      "otherNightReminder":"The Fearmonger points to a player. If different from the previous night, place the Fear token next to that player and announce that a new player has been selected with the Fearmonger ability.",
      "reminders":[
         "Fear"
      ],
      "setup":false,
      "team":"minion"
   },
   {
      "ability":"Each night*, if either good living neighbour is drunk or poisoned, you die.",
      "edition":"",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"acrobat",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/acrobat.png?raw=true",
      "name":"Acrobat",
      "otherNight":39,
      "otherNightReminder":"If a good living neighbour is drunk or poisoned, the Acrobat player dies.",
      "reminders":[
         "Dead"
      ],
      "setup":false,
      "team":"outsider"
   },
   {
      "ability":"The Demon thinks you are a Minion. Minions think you are a Demon.",
      "edition":"",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"magician",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/magician.png?raw=true",
      "name":"Magician",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"Each night*, choose a player & a character they become (if not-in-play). If a Demon is made, deaths tonight are arbitrary.",
      "edition":"snv",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"pithag",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/pithag.png?raw=true",
      "name":"Pit-Hag",
      "otherNight":17,
      "otherNightReminder":"The Pit-Hag points to a player and a character on the sheet. If this character is not in play, wake that player and show them the 'You are' card and the relevant character token. If the character is in play, nothing happens.",
      "reminders":[
         
      ],
      "setup":false,
      "team":"minion"
   },
   {
      "ability":"For the first 2 minutes of each day, veteran players may not talk.",
      "id":"buddhist",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/buddhist.png?raw=true",
      "name":"Buddhist",
      "team":"fabled"
   },
   {
      "ability":"Each night*, choose a player: they die. Townsfolk abilities yield false info. Each day, if no-one is executed, evil wins.",
      "edition":"snv",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"vortox",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/vortox.png?raw=true",
      "name":"Vortox",
      "otherNight":31,
      "otherNightReminder":"The Vortox points to a player. That player dies.",
      "reminders":[
         "Dead"
      ],
      "setup":false,
      "team":"demon"
   },
   {
      "ability":"Each night, if the dead outnumber the living, you learn 1 alive character. The Demon knows who you are.",
      "edition":"",
      "firstNight":9,
      "firstNightReminder":"Wake the Demon, show them the 'This character selected you' card, show the King token and point to the King player.",
      "id":"king",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/king.png?raw=true",
      "name":"King",
      "otherNight":64,
      "otherNightReminder":"If there are more dead than living, show the King a character token of a living player.",
      "reminders":[
         
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"Each night*, choose a player: they die. Your 2 Townsfolk neighbours are poisoned.",
      "edition":"snv",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"nodashii",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/nodashii.png?raw=true",
      "name":"No Dashii",
      "otherNight":30,
      "otherNightReminder":"The No Dashii points to a player. That player dies.",
      "reminders":[
         "Dead",
         "Poisoned"
      ],
      "setup":false,
      "team":"demon"
   },
   {
      "ability":"All Minions know you are in play. If a Minion publicly guesses you (once), your team loses.",
      "edition":"",
      "firstNight":31,
      "firstNightReminder":"Wake all the Minions, show them the 'This character selected you' card and the Damsel token.",
      "id":"damsel",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/damsel.png?raw=true",
      "name":"Damsel",
      "otherNight":52,
      "otherNightReminder":"If selected by the Huntsman, wake the Damsel, show 'You are' card and a not-in-play Townsfolk token.",
      "reminders":[
         "Guess used"
      ],
      "setup":false,
      "team":"outsider"
   },
   {
      "ability":"When you learn that you died, publicly choose 1 alive player: if they are evil, your team loses.",
      "edition":"snv",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"klutz",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/klutz.png?raw=true",
      "name":"Klutz",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         
      ],
      "setup":false,
      "team":"outsider"
   },
   {
      "ability":"You have the ability of the recently killed executee. If they are evil, you are poisoned until a good player dies by execution.",
      "edition":"",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"cannibal",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/cannibal.png?raw=true",
      "name":"Cannibal",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         "Died today",
         "Poisoned"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"On your 1st day, publicly guess up to 5 players' characters. That night, you learn how many you got correct.",
      "edition":"snv",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"juggler",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/juggler.png?raw=true",
      "name":"Juggler",
      "otherNight":62,
      "otherNightReminder":"If today was the Juggler’s first day: Show the hand signal for the number (0, 1, 2, etc.) of 'Correct' markers. Remove markers.",
      "reminders":[
         "Correct"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"Each night*, you learn how many dead players are evil.",
      "edition":"snv",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"oracle",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/oracle.png?raw=true",
      "name":"Oracle",
      "otherNight":60,
      "otherNightReminder":"Show the hand signal for the number (0, 1, 2, etc.) of dead evil players.",
      "reminders":[
         
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"Once per game, during the day, visit the Storyteller for some advice to help you win.",
      "edition":"",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"fisherman",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/fisherman.png?raw=true",
      "name":"Fisherman",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         "No ability"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"Each night, choose a player (not yourself or Travellers): you learn 1 good and 1 evil character, 1 of which is correct.",
      "edition":"snv",
      "firstNight":41,
      "firstNightReminder":"The Dreamer points to a player. Show 1 good and 1 evil character token; one of these is correct.",
      "id":"dreamer",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/dreamer.png?raw=true",
      "name":"Dreamer",
      "otherNight":57,
      "otherNightReminder":"The Dreamer points to a player. Show 1 good and 1 evil character token; one of these is correct.",
      "reminders":[
         
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"Once per day, you may choose to kill an alive neighbour, if your other alive neighbour agrees.",
      "edition":"",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"gangster",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/gangster.png?raw=true",
      "name":"Gangster",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         
      ],
      "setup":false,
      "team":"traveler"
   },
   {
      "ability":"Once per game, during the day, publicly choose a player: if they are the Demon, they die.",
      "edition":"tb",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"slayer",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/slayer.png?raw=true",
      "name":"Slayer",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         "No ability"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"Each night*, choose 2 players: they can't die tonight, but 1 is drunk until dusk.",
      "edition":"bmr",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"innkeeper",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/innkeeper.png?raw=true",
      "name":"Innkeeper",
      "otherNight":9,
      "otherNightReminder":"The previously protected and drunk players lose those markers. The Innkeeper points to two players. Those players are protected. One is drunk.",
      "reminders":[
         "Drunk",
         "Protected"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"Once per game, during the day, privately ask the Storyteller any yes/no question.",
      "edition":"snv",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"artist",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/artist.png?raw=true",
      "name":"Artist",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         "No ability"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"Once per game, the Demon secretly chooses an opposing player: all players choose which of these 2 players win.",
      "id":"fiddler",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/fiddler.png?raw=true",
      "name":"Fiddler",
      "team":"fabled"
   },
   {
      "ability":"You think you are a Demon, but you are not. The Demon knows who you are & who you choose at night.",
      "edition":"bmr",
      "firstNight":7,
      "firstNightReminder":"If 7 or more players: Show the Lunatic a number of arbitrary 'Minions', players equal to the number of Minions in play. Show 3 character tokens of arbitrary good characters. If the token received by the Lunatic is a Demon that would wake tonight: Allow the Lunatic to do the Demon actions. Place their 'attack' markers. Wake the Demon. Show the Demon’s real character token. Show them the Lunatic player. If the Lunatic attacked players: Show the real demon each marked player. Remove any Lunatic 'attack' markers.",
      "id":"lunatic",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/lunatic.png?raw=true",
      "name":"Lunatic",
      "otherNight":21,
      "otherNightReminder":"Allow the Lunatic to do the actions of the Demon. Place their 'attack' markers. If the Lunatic selected players: Wake the Demon. Show the 'attack' marker, then point to each marked player. Remove any Lunatic 'attack' markers.",
      "reminders":[
         "Attack 1",
         "Attack 2",
         "Attack 3"
      ],
      "setup":false,
      "team":"outsider"
   },
   {
      "ability":"Each night, choose a living player (different to last night): if executed tomorrow, they don't die.",
      "edition":"bmr",
      "firstNight":22,
      "firstNightReminder":"The Devil’s Advocate points to a living player. That player survives execution tomorrow.",
      "id":"devilsadvocate",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/devilsadvocate.png?raw=true",
      "name":"Devil's Advocate",
      "otherNight":14,
      "otherNightReminder":"The Devil’s Advocate points to a living player, different from the previous night. That player survives execution tomorrow.",
      "reminders":[
         "Survives execution"
      ],
      "setup":false,
      "team":"minion"
   },
   {
      "ability":"Each night*, you may choose a player: they die. If your last choice was no-one, choose 3 players tonight.",
      "edition":"bmr",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"po",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/po.png?raw=true",
      "name":"Po",
      "otherNight":28,
      "otherNightReminder":"If the Po chose no-one the previous night: The Po points to three players. Otherwise: The Po either shows the 'no' head signal , or points to a player. Chosen players die",
      "reminders":[
         "3 attacks",
         "Dead"
      ],
      "setup":false,
      "team":"demon"
   },
   {
      "ability":"Once per game, at night, choose which Minions or which Demon is in play.",
      "edition":"",
      "firstNight":13,
      "firstNightReminder":"The Engineer shows a 'no' head signal, or points to a Demon or points to the relevant number of Minions. If the Engineer chose characters, replace the Demon or Minions with the choices, then wake the relevant players and show them the You are card and the relevant character tokens.",
      "id":"engineer",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/engineer.png?raw=true",
      "name":"Engineer",
      "otherNight":6,
      "otherNightReminder":"The Engineer shows a 'no' head signal, or points to a Demon or points to the relevant number of Minions. If the Engineer chose characters, replace the Demon or Minions with the choices, then wake the relevant players and show them the 'You are' card and the relevant character tokens.",
      "reminders":[
         "No ability"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"Each night, choose a player & a good character: they are “mad” they are this character tomorrow, or might be executed.",
      "edition":"snv",
      "firstNight":25,
      "firstNightReminder":"The Cerenovus points to a player, then to a character on their sheet. Wake that player. Show the 'This character selected you' card, then the Cerenovus token. Show the selected character token. If the player is not mad about being that character tomorrow, they can be executed.",
      "id":"cerenovus",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/cerenovus.png?raw=true",
      "name":"Cerenovus",
      "otherNight":16,
      "otherNightReminder":"The Cerenovus points to a player, then to a character on their sheet. Wake that player. Show the 'This character selected you' card, then the Cerenovus token. Show the selected character token. If the player is not mad about being that character tomorrow, they can be executed.",
      "reminders":[
         "Mad"
      ],
      "setup":false,
      "team":"minion"
   },
   {
      "ability":"Each night, you learn which alignment the Storyteller believes is winning: good, evil, or neither.",
      "edition":"",
      "firstNight":49,
      "firstNightReminder":"Show the General thumbs up for good winning, thumbs down for evil winning or thumb to the side for neither.",
      "id":"general",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/general.png?raw=true",
      "name":"General",
      "otherNight":69,
      "otherNightReminder":"Show the General thumbs up for good winning, thumbs down for evil winning or thumb to the side for neither.",
      "reminders":[
         
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"Once per game, at night, choose a player: they learn who you are.",
      "edition":"",
      "firstNight":46,
      "firstNightReminder":"The Nightwatchman may point to a player. Wake that player, show the 'This character selected you' card and the Nightwatchman token, then point to the Nightwatchman player.",
      "id":"nightwatchman",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/nightwatchman.png?raw=true",
      "name":"Nightwatchman",
      "otherNight":66,
      "otherNightReminder":"The Nightwatchman may point to a player. Wake that player, show the 'This character selected you' card and the Nightwatchman token, then point to the Nightwatchman player.",
      "reminders":[
         "No ability"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"Something bad might happen to whoever is most responsible for the death of a new player.",
      "id":"angel",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/angel.png?raw=true",
      "name":"Angel",
      "reminders":[
         "Protect",
         "Something Bad"
      ],
      "team":"fabled"
   },
   {
      "ability":"Whoever wins, loses & whoever loses, wins, even if you are dead.",
      "edition":"",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"heretic",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/heretic.png?raw=true",
      "name":"Heretic",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         
      ],
      "setup":false,
      "team":"outsider"
   },
   {
      "ability":"If you die at night, an alive good player becomes a Farmer.",
      "edition":"",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"farmer",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/farmer.png?raw=true",
      "name":"Farmer",
      "otherNight":46,
      "otherNightReminder":"If a Farmer died tonight, choose another good player and make them the Farmer. Wake this player, show them the 'You are' card and the Farmer character token.",
      "reminders":[
         
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"You start knowing that 1 of 2 players is a particular Minion.",
      "edition":"tb",
      "firstNight":34,
      "firstNightReminder":"Show the character token of a Minion in play. Point to two players, one of which is that character.",
      "id":"investigator",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/investigator.png?raw=true",
      "name":"Investigator",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         "Minion",
         "Wrong"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"When you die, 1 player is drunk from now on.",
      "edition":"snv",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"sweetheart",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/sweetheart.png?raw=true",
      "name":"Sweetheart",
      "otherNight":41,
      "otherNightReminder":"Choose a player that is drunk.",
      "reminders":[
         "Drunk"
      ],
      "setup":false,
      "team":"outsider"
   },
   {
      "ability":"If the Demon kills the King, you learn which player is the Demon. [+ the King]",
      "edition":"",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"choirboy",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/choirboy.png?raw=true",
      "name":"Choirboy",
      "otherNight":44,
      "otherNightReminder":"If the King was killed by the Demon, wake the Choirboy and point to the Demon player.",
      "reminders":[
         
      ],
      "setup":true,
      "team":"townsfolk"
   },
   {
      "ability":"Each night*, choose a player & guess their character: if you guess wrong, you die.",
      "edition":"bmr",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"gambler",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/gambler.png?raw=true",
      "name":"Gambler",
      "otherNight":11,
      "otherNightReminder":"The Gambler points to a player, and a character on their sheet. If incorrect, the Gambler dies.",
      "reminders":[
         "Dead"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"There might be 1 extra or 1 fewer Outsider in-play.",
      "id":"sentinel",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/sentinel.png?raw=true",
      "name":"Sentinel",
      "team":"fabled"
   },
   {
      "ability":"Once per game, 1 good player might get false information.",
      "id":"fibbin",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/fibbin.png?raw=true",
      "name":"Fibbin",
      "reminders":[
         "Used"
      ],
      "team":"fabled"
   },
   {
      "ability":"Each night, choose a player: they are poisoned. The previously poisoned player dies then becomes healthy.",
      "edition":"bmr",
      "firstNight":28,
      "firstNightReminder":"The Pukka points to a player. That player is poisoned.",
      "id":"pukka",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/pukka.png?raw=true",
      "name":"Pukka",
      "otherNight":26,
      "otherNightReminder":"The Pukka points to a player. That player is poisoned. The previously poisoned player dies.",
      "reminders":[
         "Dead",
         "Poisoned"
      ],
      "setup":false,
      "team":"demon"
   },
   {
      "ability":"The 1st time you are nominated, if the nominator is a Townsfolk, they are executed immediately.",
      "edition":"tb",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"virgin",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/virgin.png?raw=true",
      "name":"Virgin",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         "No ability"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"Each day, you may visit the Storyteller to learn 2 things in private: 1 is true & 1 is false.",
      "edition":"snv",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"savant",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/savant.png?raw=true",
      "name":"Savant",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"You start knowing 1 evil player. If the player you know dies, you learn another evil player tonight. [1 Townsfolk is evil]",
      "edition":"",
      "firstNight":45,
      "firstNightReminder":"Point to 1 evil player. Wake the townsfolk who is evil and show them the 'You are' card and the thumbs down evil sign.",
      "id":"bountyhunter",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/bountyhunter.png?raw=true",
      "name":"Bounty Hunter",
      "otherNight":65,
      "otherNightReminder":"If the known evil player has died, point to another evil player.",
      "reminders":[
         "Known"
      ],
      "setup":true,
      "team":"townsfolk"
   },
   {
      "ability":"The Demon may choose not to attack & must do this at least once per game. Evil players get normal starting info.",
      "id":"toymaker",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/toymaker.png?raw=true",
      "name":"Toymaker",
      "reminders":[
         "No Attack"
      ],
      "team":"fabled"
   },
   {
      "ability":"Each night*, you learn if a Minion nominated today.",
      "edition":"snv",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"towncrier",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/towncrier.png?raw=true",
      "name":"Town Crier",
      "otherNight":59,
      "otherNightReminder":"Nod 'yes' or shake head 'no' for whether a Minion nominated today. Place the 'Minion not nominated' marker (remove 'Minion nominated', if any).",
      "reminders":[
         "Minion nominated",
         "Minions not nominated"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"If 4 or more players live, each living player may publicly choose (once per game) that a player of their own alignment dies.",
      "id":"doomsayer",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/doomsayer.png?raw=true",
      "name":"Doomsayer",
      "team":"fabled"
   },
   {
      "ability":"Nominees die, but may nominate again immediately (on day 3, they must). After day 3, evil wins. [All Minions are Riot]",
      "edition":"",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"riot",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/riot.png?raw=true",
      "name":"Riot",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         
      ],
      "setup":true,
      "team":"demon"
   },
   {
      "ability":"Each night, you learn 1 player of each character type, until there are no more types to learn. [+1 Outsider]",
      "edition":"",
      "firstNight":44,
      "firstNightReminder":"Choose a character type. Point to a player whose character is of that type. Place the Balloonist's Seen reminder next to that character.",
      "id":"balloonist",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/balloonist.png?raw=true",
      "name":"Balloonist",
      "otherNight":63,
      "otherNightReminder":"Choose a character type that does not yet have a Seen reminder next to a character of that type. Point to a player whose character is of that type, if there are any. Place the Balloonist's Seen reminder next to that character.",
      "reminders":[
         "Seen Demon",
         "Seen Minion",
         "Seen Outsider",
         "Seen Townsfolk",
         "Seen Traveller"
      ],
      "setup":true,
      "team":"townsfolk"
   },
   {
      "ability":"Each night, choose a player (not yourself): tomorrow, you may only vote if they are voting too.",
      "edition":"tb",
      "firstNight":38,
      "firstNightReminder":"The Butler points to a player. Mark that player as 'Master'.",
      "id":"butler",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/butler.png?raw=true",
      "name":"Butler",
      "otherNight":55,
      "otherNightReminder":"The Butler points to a player. Mark that player as 'Master'.",
      "reminders":[
         "Master"
      ],
      "setup":false,
      "team":"outsider"
   },
   {
      "ability":"Each day, you may make a public statement. Tonight, if it was true, a player dies.",
      "edition":"bmr",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"gossip",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/gossip.png?raw=true",
      "name":"Gossip",
      "otherNight":47,
      "otherNightReminder":"If the Gossip’s public statement was true: Choose a player not protected from dying tonight. That player dies.",
      "reminders":[
         "Dead"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"Each night*, if no-one died today, choose a player: they die. The 1st time you die, you live but register as dead.",
      "edition":"bmr",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"zombuul",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/zombuul.png?raw=true",
      "name":"Zombuul",
      "otherNight":25,
      "otherNightReminder":"If no-one died during the day: The Zombuul points to a player. That player dies.",
      "reminders":[
         "Dead",
         "Died today"
      ],
      "setup":false,
      "team":"demon"
   },
   {
      "ability":"Each day, after the 1st execution, you may nominate again.",
      "edition":"snv",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"butcher",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/butcher.png?raw=true",
      "name":"Butcher",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         
      ],
      "setup":false,
      "team":"traveler"
   },
   {
      "ability":"If more than 1 good player is executed, you win. All players know you are in play. After day 5, evil wins.",
      "edition":"",
      "firstNight":53,
      "firstNightReminder":"Place the Leviathan 'Day 1' marker. Announce 'The Leviathan is in play; this is Day 1.'",
      "id":"leviathan",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/leviathan.png?raw=true",
      "name":"Leviathan",
      "otherNight":73,
      "otherNightReminder":"Change the Leviathan Day reminder for the next day.",
      "reminders":[
         "Day 1",
         "Day 2",
         "Day 3",
         "Day 4",
         "Day 5",
         "Good player executed"
      ],
      "setup":false,
      "team":"demon"
   },
   {
      "ability":"You start knowing which Outsiders are in play. If 1 died today, choose a player tonight: they die. [−1 or +1 Outsider]",
      "edition":"bmr",
      "firstNight":21,
      "firstNightReminder":"Show each of the Outsider tokens in play.",
      "id":"godfather",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/godfather.png?raw=true",
      "name":"Godfather",
      "otherNight":38,
      "otherNightReminder":"If an Outsider died today: The Godfather points to a player. That player dies.",
      "reminders":[
         "Dead",
         "Died today"
      ],
      "setup":true,
      "team":"minion"
   },
   {
      "ability":"Each night*, choose a player: they die. The 1st Outsider this kills becomes an evil Fang Gu & you die instead. [+1 Outsider]",
      "edition":"snv",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"fanggu",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/fanggu.png?raw=true",
      "name":"Fang Gu",
      "otherNight":29,
      "otherNightReminder":"The Fang Gu points to a player. That player dies. Or, if that player was an Outsider and there are no other Fang Gu in play: The Fang Gu dies instead of the chosen player. The chosen player is now an evil Fang Gu. Wake the new Fang Gu. Show the 'You are' card, then the Fang Gu token. Show the 'You are' card, then the thumb-down 'evil' hand sign.",
      "reminders":[
         "Dead",
         "Once"
      ],
      "setup":true,
      "team":"demon"
   },
   {
      "ability":"Each night, you become the alignment of an alive neighbour. If all good players choose to join your cult, your team wins.",
      "edition":"",
      "firstNight":47,
      "firstNightReminder":"If the cult leader changed alignment, show them the thumbs up good signal of the thumbs down evil signal accordingly.",
      "id":"cultleader",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/cultleader.png?raw=true",
      "name":"Cult Leader",
      "otherNight":67,
      "otherNightReminder":"If the cult leader changed alignment, show them the thumbs up good signal of the thumbs down evil signal accordingly.",
      "reminders":[
         
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"You & an opposing player know each other. If the good player is executed, evil wins. Good can't win if you both live.",
      "edition":"snv",
      "firstNight":23,
      "firstNightReminder":"Wake the Evil Twin and their twin. Confirm that they have acknowledged each other. Point to the Evil Twin. Show their Evil Twin token to the twin player. Point to the twin. Show their character token to the Evil Twin player.",
      "id":"eviltwin",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/eviltwin.png?raw=true",
      "name":"Evil Twin",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         "Twin"
      ],
      "setup":false,
      "team":"minion"
   },
   {
      "ability":"If you publicly claim to be the Goblin when nominated & are executed that day, your team wins.",
      "edition":"",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"goblin",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/goblin.png?raw=true",
      "name":"Goblin",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         "Claimed"
      ],
      "setup":false,
      "team":"minion"
   },
   {
      "ability":"Once per game, at night, choose a living player: the Damsel, if chosen, becomes a not-in-play Townsfolk. [+the Damsel]",
      "edition":"",
      "firstNight":30,
      "firstNightReminder":"The Huntsman shakes their head 'no' or points to a player. If they point to the Damsel, wake that player, show the 'You are' card and a not-in-play character token.",
      "id":"huntsman",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/huntsman.png?raw=true",
      "name":"Huntsman",
      "otherNight":51,
      "otherNightReminder":"The Huntsman shakes their head 'no' or points to a player. If they point to the Damsel, wake that player, show the 'You are' card and a not-in-play character token.",
      "reminders":[
         "No ability"
      ],
      "setup":true,
      "team":"townsfolk"
   },
   {
      "ability":"Once per game, at night, choose a dead player: they regain their ability until dusk.",
      "edition":"snv",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"bonecollector",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/bonecollector.png?raw=true",
      "name":"Bone Collector",
      "otherNight":1,
      "otherNightReminder":"The Bone Collector either shakes their head no or points at any dead player. If they pointed at any dead player, put the Bone Collector's 'Has Ability' reminder by the chosen player's character token. (They may need to be woken tonight to use it.)",
      "reminders":[
         "Has ability",
         "No ability"
      ],
      "setup":false,
      "team":"traveler"
   },
   {
      "ability":"Once per game, at night, choose a character: they are drunk for 3 nights & 3 days.",
      "edition":"bmr",
      "firstNight":19,
      "firstNightReminder":"The Courtier either shows a 'no' head signal, or points to a character on the sheet. If the Courtier used their ability: If that character is in play, that player is drunk.",
      "id":"courtier",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/courtier.png?raw=true",
      "name":"Courtier",
      "otherNight":10,
      "otherNightReminder":"Reduce the remaining number of days the marked player is poisoned. If the Courtier has not yet used their ability: The Courtier either shows a 'no' head signal, or points to a character on the sheet. If the Courtier used their ability: If that character is in play, that player is drunk.",
      "reminders":[
         "Drunk 1",
         "Drunk 2",
         "Drunk 3",
         "No ability"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"You start knowing 1 in-play Townsfolk. If you were mad that you were this character, you gain their ability when they die.",
      "edition":"",
      "firstNight":29,
      "firstNightReminder":"Show the Pixie 1 in-play Townsfolk character token.",
      "id":"pixie",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/pixie.png?raw=true",
      "name":"Pixie",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         "Has ability",
         "Mad"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"Each night*, choose a player: they die. You start by choosing an alive player: they are poisoned - you die if & only if they die.",
      "edition":"",
      "firstNight":15,
      "firstNightReminder":"The Lleech points to a player. Place the Poisoned reminder token.",
      "id":"lleech",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/lleech.png?raw=true",
      "name":"Lleech",
      "otherNight":35,
      "otherNightReminder":"The Lleech points to a player. That player dies.",
      "reminders":[
         "Dead",
         "Poisoned"
      ],
      "setup":false,
      "team":"demon"
   },
   {
      "ability":"You start knowing 3 players, 1 and only 1 of which is evil.",
      "edition":"",
      "firstNight":43,
      "firstNightReminder":"Point to 3 players including one evil player, in no particular order.",
      "id":"noble",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/noble.png?raw=true",
      "name":"Noble",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         "Seen"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"If the Demon dies by execution (ending the game), play for 1 more day. If a player is then executed, their team loses.",
      "edition":"bmr",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"mastermind",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/mastermind.png?raw=true",
      "name":"Mastermind",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         
      ],
      "setup":false,
      "team":"minion"
   },
   {
      "ability":"Each night, choose a player: they are poisoned tonight and tomorrow day.",
      "edition":"tb",
      "firstNight":17,
      "firstNightReminder":"The Poisoner points to a player. That player is poisoned.",
      "id":"poisoner",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/poisoner.png?raw=true",
      "name":"Poisoner",
      "otherNight":8,
      "otherNightReminder":"The previously poisoned player is no longer poisoned. The Poisoner points to a player. That player is poisoned.",
      "reminders":[
         "Poisoned"
      ],
      "setup":false,
      "team":"minion"
   },
   {
      "ability":"Each night, choose a player: if they nominate tomorrow, they die. If just 3 players live, you lose this ability.",
      "edition":"snv",
      "firstNight":24,
      "firstNightReminder":"The Witch points to a player. If that player nominates tomorrow they die immediately.",
      "id":"witch",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/witch.png?raw=true",
      "name":"Witch",
      "otherNight":15,
      "otherNightReminder":"If there are 4 or more players alive: The Witch points to a player. If that player nominates tomorrow they die immediately.",
      "reminders":[
         "Cursed"
      ],
      "setup":false,
      "team":"minion"
   },
   {
      "ability":"Only the Storyteller can nominate. At least 1 opposite player must be nominated each day.",
      "edition":"bmr",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"bishop",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/bishop.png?raw=true",
      "name":"Bishop",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         "Nominate evil",
         "Nominate good"
      ],
      "setup":false,
      "team":"traveler"
   },
   {
      "ability":"If there are 5 or more players alive & the Demon dies, you become the Demon. (Travellers don’t count)",
      "edition":"tb",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"scarletwoman",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/scarletwoman.png?raw=true",
      "name":"Scarlet Woman",
      "otherNight":20,
      "otherNightReminder":"If the Scarlet Woman became the Demon today: Show the 'You are' card, then the demon token.",
      "reminders":[
         "Demon"
      ],
      "setup":false,
      "team":"minion"
   },
   {
      "ability":"Once per game, at night, choose a good character: gain that ability. If this character is in play, they are drunk.",
      "edition":"snv",
      "firstNight":2,
      "firstNightReminder":"The Philosopher either shows a 'no' head signal, or points to a good character on their sheet. If they chose a character: Swap the out-of-play character token with the Philosopher token. Or, if the character is in play, place the drunk marker by that player and the Not the Philosopher token by the Philosopher.",
      "id":"philosopher",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/philosopher.png?raw=true",
      "name":"Philosopher",
      "otherNight":2,
      "otherNightReminder":"If the Philosopher has not used their ability: the Philosopher either shows a 'no' head signal, or points to a good character on their sheet. If they chose a character: Swap the out-of-play character token with the Philosopher token. Or, if the character is in play, place the drunk marker by that player and the Not the Philosopher token by the Philosopher.",
      "remindersGlobal":[
         "Drunk",
         "Is the Philosopher"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"Each night*, choose a living player: if they agree, you learn their character, but you both might die.",
      "edition":"snv",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"harlot",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/harlot.png?raw=true",
      "name":"Harlot",
      "otherNight":1,
      "otherNightReminder":"The Harlot points at any player. Then, put the Harlot to sleep. Wake the chosen player, show them the 'This character selected you' token, then the Harlot token. That player either nods their head yes or shakes their head no. If they nodded their head yes, wake the Harlot and show them the chosen player's character token. Then, you may decide that both players die.",
      "reminders":[
         "Dead"
      ],
      "setup":false,
      "team":"traveler"
   },
   {
      "ability":"When you learn that you died, publicly choose 1 alive player. Tonight, if it was a good player, they die.",
      "edition":"bmr",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"moonchild",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/moonchild.png?raw=true",
      "name":"Moonchild",
      "otherNight":49,
      "otherNightReminder":"If the Moonchild used their ability to target a player today: If that player is good, they die.",
      "reminders":[
         "Dead"
      ],
      "setup":false,
      "team":"outsider"
   },
   {
      "ability":"Once per game, if another player nominated, you may choose to force the current execution to pass or fail.",
      "edition":"bmr",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"judge",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/judge.png?raw=true",
      "name":"Judge",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         "No ability"
      ],
      "setup":false,
      "team":"traveler"
   },
   {
      "ability":"You do not know you are the Drunk. You think you are a Townsfolk character, but you are not.",
      "edition":"tb",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"drunk",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/drunk.png?raw=true",
      "name":"Drunk",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         
      ],
      "remindersGlobal":[
         "Drunk"
      ],
      "setup":true,
      "team":"outsider"
   },
   {
      "ability":"Each night*, a player might die. Executions fail if only evil voted. You register as a Minion too. [Most players are Legion]",
      "edition":"",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"legion",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/legion.png?raw=true",
      "name":"Legion",
      "otherNight":34,
      "otherNightReminder":"Choose a player, that player dies.",
      "reminders":[
         "About to die",
         "Dead"
      ],
      "setup":true,
      "team":"demon"
   },
   {
      "ability":"Each night, you learn how many players’ abilities worked abnormally (since dawn) due to another character's ability.",
      "edition":"snv",
      "firstNight":51,
      "firstNightReminder":"Show the hand signal for the number (0, 1, 2, etc.) of players whose ability malfunctioned due to other abilities.",
      "id":"mathematician",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/mathematician.png?raw=true",
      "name":"Mathematician",
      "otherNight":71,
      "otherNightReminder":"Show the hand signal for the number (0, 1, 2, etc.) of players whose ability malfunctioned due to other abilities.",
      "reminders":[
         "Abnormal"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"Each night, choose a player (not yourself): their vote counts negatively tomorrow.",
      "edition":"tb",
      "firstNight":1,
      "firstNightReminder":"The Thief points to a player. Put the Thief's 'Negative vote' reminder by the chosen player's character token.",
      "id":"thief",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/thief.png?raw=true",
      "name":"Thief",
      "otherNight":1,
      "otherNightReminder":"The Thief points to a player. Put the Thief's 'Negative vote' reminder by the chosen player's character token.",
      "reminders":[
         "Negative vote"
      ],
      "setup":false,
      "team":"traveler"
   },
   {
      "ability":"Minions & Demons do not know each other. If you die, they learn who each other are that night.",
      "edition":"",
      "firstNight":4,
      "firstNightReminder":"Do not inform the Demon/Minions who each other are",
      "id":"poppygrower",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/poppygrower.png?raw=true",
      "name":"Poppy Grower",
      "otherNight":3,
      "otherNightReminder":"If the Poppy Grower has died, show the Minions/Demon who each other are.",
      "reminders":[
         "Evil wakes"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"The first time you die, you don't.",
      "edition":"bmr",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"fool",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/fool.png?raw=true",
      "name":"Fool",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         "No ability"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"You have a not-in-play Minion ability.",
      "edition":"",
      "firstNight":3,
      "firstNightReminder":"Show the Alchemist a not-in-play Minion token",
      "id":"alchemist",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/alchemist.png?raw=true",
      "name":"Alchemist",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         
      ],
      "remindersGlobal":[
         "Is the Alchemist"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"Each night, choose 2 players: you learn if either is a Demon. There is a good player that registers as a Demon to you.",
      "edition":"tb",
      "firstNight":37,
      "firstNightReminder":"The Fortune Teller points to two players. Give the head signal (nod yes, shake no) for whether one of those players is the Demon.",
      "id":"fortuneteller",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/fortuneteller.png?raw=true",
      "name":"Fortune Teller",
      "otherNight":54,
      "otherNightReminder":"The Fortune Teller points to two players. Show the head signal (nod 'yes', shake 'no') for whether one of those players is the Demon.",
      "reminders":[
         "Red herring"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"Once per game, at night*, choose a dead player: if they are a Townsfolk, they are resurrected.",
      "edition":"bmr",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"professor",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/professor.png?raw=true",
      "name":"Professor",
      "otherNight":45,
      "otherNightReminder":"If the Professor has not used their ability: The Professor either shakes their head no, or points to a player. If that player is a Townsfolk, they are now alive.",
      "reminders":[
         "Alive",
         "No ability"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"You might die at any time.",
      "edition":"bmr",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"tinker",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/tinker.png?raw=true",
      "name":"Tinker",
      "otherNight":48,
      "otherNightReminder":"The Tinker might die.",
      "reminders":[
         "Dead"
      ],
      "setup":false,
      "team":"outsider"
   },
   {
      "ability":"Minions start knowing 3 not-in-play characters.",
      "edition":"",
      "firstNight":6,
      "firstNightReminder":"After Minion info wake each Minion and show them three not-in-play character tokens. These may be the same or different to each other and the ones shown to the Demon.",
      "id":"snitch",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/snitch.png?raw=true",
      "name":"Snitch",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         
      ],
      "setup":false,
      "team":"outsider"
   },
   {
      "ability":"Each night, Minions choose who babysits Lil' Monsta's token & \"is the Demon\". A player dies each night*. [+1 Minion]",
      "edition":"",
      "firstNight":16,
      "firstNightReminder":"Wake all Minions together, allow them to vote by pointing at who they want to babysit Lil' Monsta.",
      "id":"lilmonsta",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/lilmonsta.png?raw=true",
      "name":"Lil' Monsta",
      "otherNight":36,
      "otherNightReminder":"Wake all Minions together, allow them to vote by pointing at who they want to babysit Lil' Monsta. Choose a player, that player dies.",
      "reminders":[
         
      ],
      "remindersGlobal":[
         "Dead",
         "Is the Demon"
      ],
      "setup":true,
      "team":"demon"
   },
   {
      "ability":"Each day, after the 1st vote has been tallied, you may choose a player that voted: they die.",
      "edition":"tb",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"gunslinger",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/gunslinger.png?raw=true",
      "name":"Gunslinger",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         
      ],
      "setup":false,
      "team":"traveler"
   },
   {
      "ability":"Only you and the dead can vote. They don't need a vote token to do so. A 50% majority is not required.",
      "edition":"bmr",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"voudon",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/voudon.png?raw=true",
      "name":"Voudon",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         
      ],
      "setup":false,
      "team":"traveler"
   },
   {
      "ability":"Use the Djinn's special rule. All players know what it is.",
      "id":"djinn",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/djinn.png?raw=true",
      "name":"Djinn",
      "team":"fabled"
   },
   {
      "ability":"If you are “mad” about being an Outsider, you might be executed.",
      "edition":"snv",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"mutant",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/mutant.png?raw=true",
      "name":"Mutant",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         
      ],
      "setup":false,
      "team":"outsider"
   },
   {
      "ability":"You start knowing how many pairs of evil players there are.",
      "edition":"tb",
      "firstNight":35,
      "firstNightReminder":"Show the finger signal (0, 1, 2, …) for the number of pairs of neighbouring evil players.",
      "id":"chef",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/chef.png?raw=true",
      "name":"Chef",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"If you die at night, you are woken to choose a player: you learn their character.",
      "edition":"tb",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"ravenkeeper",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/ravenkeeper.png?raw=true",
      "name":"Ravenkeeper",
      "otherNight":42,
      "otherNightReminder":"If the Ravenkeeper died tonight: The Ravenkeeper points to a player. Show that player’s character token.",
      "reminders":[
         
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"If you were funny today, you cannot die by exile.",
      "edition":"snv",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"deviant",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/deviant.png?raw=true",
      "name":"Deviant",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         
      ],
      "setup":false,
      "team":"traveler"
   },
   {
      "ability":"You start knowing how many steps from the Demon to its nearest Minion.",
      "edition":"snv",
      "firstNight":40,
      "firstNightReminder":"Show the hand signal for the number (1, 2, 3, etc.) of places from Demon to closest Minion.",
      "id":"clockmaker",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/clockmaker.png?raw=true",
      "name":"Clockmaker",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"Each night, until dusk, 1) a player becomes sober, healthy and gets true info, or 2) their ability works twice. They learn which.",
      "edition":"snv",
      "firstNight":1,
      "firstNightReminder":"Choose a player, wake them and tell them which Barista power is affecting them. Treat them accordingly (sober/healthy/true info or activate their ability twice).",
      "id":"barista",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/barista.png?raw=true",
      "name":"Barista",
      "otherNight":1,
      "otherNightReminder":"Choose a player, wake them and tell them which Barista power is affecting them. Treat them accordingly (sober/healthy/true info or activate their ability twice).",
      "reminders":[
         "Ability twice",
         "Sober & Healthy"
      ],
      "setup":false,
      "team":"traveler"
   },
   {
      "ability":"If you die by execution, your team loses.",
      "edition":"tb",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"saint",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/saint.png?raw=true",
      "name":"Saint",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         
      ],
      "setup":false,
      "team":"outsider"
   },
   {
      "ability":"Each day, before nominations, you may publicly choose a player: they die. If executed, you only die if you lose roshambo.",
      "edition":"",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"psychopath",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/psychopath.png?raw=true",
      "name":"Psychopath",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         
      ],
      "setup":false,
      "team":"minion"
   },
   {
      "ability":"Each night, you learn how many of your 2 alive neighbours are evil.",
      "edition":"tb",
      "firstNight":36,
      "firstNightReminder":"Show the finger signal (0, 1, 2) for the number of evil alive neighbours of the Empath.",
      "id":"empath",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/empath.png?raw=true",
      "name":"Empath",
      "otherNight":53,
      "otherNightReminder":"Show the finger signal (0, 1, 2) for the number of evil neighbours.",
      "reminders":[
         
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"If a player of your alignment is executed, you might be executed instead.",
      "edition":"tb",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"scapegoat",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/scapegoat.png?raw=true",
      "name":"Scapegoat",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         
      ],
      "setup":false,
      "team":"traveler"
   },
   {
      "ability":"The Storyteller can break the game rules & if executed, good wins, even if you are dead [No evil characters]",
      "edition":"",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"atheist",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/atheist.png?raw=true",
      "name":"Atheist",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         
      ],
      "setup":true,
      "team":"townsfolk"
   },
   {
      "ability":"Executed good players might not die.",
      "edition":"bmr",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"pacifist",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/pacifist.png?raw=true",
      "name":"Pacifist",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"On your 1st night, you gain a Townsfolk ability (if good), or a Minion ability (if evil).",
      "edition":"bmr",
      "firstNight":1,
      "firstNightReminder":"Show the Apprentice the 'You are' card, then a Townsfolk or Minion token. In the Grimoire, replace the Apprentice token with that character token, and put the Apprentice's 'Is the Apprentice' reminder by that character token.",
      "id":"apprentice",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/apprentice.png?raw=true",
      "name":"Apprentice",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         "Is the Apprentice"
      ],
      "setup":false,
      "team":"traveler"
   },
   {
      "ability":"Each night*, choose a player (not yourself): they are safe from the Demon tonight.",
      "edition":"tb",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"monk",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/monk.png?raw=true",
      "name":"Monk",
      "otherNight":13,
      "otherNightReminder":"The previously protected player is no longer protected. The Monk points to a player not themself. Mark that player 'Protected'.",
      "reminders":[
         "Protected"
      ],
      "setup":false,
      "team":"townsfolk"
   },
   {
      "ability":"Something bad might happen to whoever talks when the Storyteller has asked for silence.",
      "id":"hellslibrarian",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/hellslibrarian.png?raw=true",
      "name":"Hell's Librarian",
      "reminders":[
         "Something Bad"
      ],
      "team":"fabled"
   },
   {
      "ability":"You might register as evil & as a Minion or Demon, even if dead.",
      "edition":"tb",
      "firstNight":0,
      "firstNightReminder":"",
      "id":"recluse",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/recluse.png?raw=true",
      "name":"Recluse",
      "otherNight":0,
      "otherNightReminder":"",
      "reminders":[
         
      ],
      "setup":false,
      "team":"outsider"
   },
   {
      "ability":"Name a good character. If in play, they can only die by execution, but evil players learn which player it is.",
      "id":"stormcatcher",
      "image":"https://github.com/bra1n/townsquare/blob/main/src/assets/icons/stormcatcher.png?raw=true",
      "name":"Storm Catcher",
      "reminders":[
         "Safe"
      ],
      "team":"fabled"
   }
]
                      """
# )

import utility
import const

def gen_locale_json(locale,csv_folder,json_folder):
    translation = utility.read_csv(csv_folder,locale)
    origin_json = const.json_source()
    for role in origin_json:
        name = role['id']
        for k in const.csv_text_entries:
            role[k] = translation[k][name]
        for k in const.csv_list_entries:
            role[k] = list(map(str.strip,translation[k][name].split(','))) if translation[k][name]!='' else []
    utility.dump_json(origin_json,json_folder,locale)

def gen_all_json(csv_folder,json_folder):
    for locale in const.known_locales:
        gen_locale_json(locale,csv_folder,json_folder)
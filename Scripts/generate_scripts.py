
import const
import utility
import os
def generate(script_folder, scripts, description_folder, json_folder):
    for locale in const.known_locales:
        gen_locale(locale, script_folder, scripts, description_folder, json_folder)

def gen_locale(locale, script_folder, scripts, description_folder, json_folder):
    out_dir = os.path.join(script_folder,locale)
    try:
        pass
        os.makedirs(out_dir)
    except FileExistsError:
        # directory already exists
        pass
    for script in scripts:
        gen_locale_script(out_dir, script, locale, description_folder, json_folder)

def gen_locale_script(out_dir, script_name, locale, description_folder, json_folder):
    roles = []
    script = utility.load_json(description_folder, script_name)
    all_roles = utility.load_json(json_folder,locale)
    for role in all_roles:
        if role['id'] in script:
            roles.append(role)

    for role in  roles:
        role['id'] = locale+"_"+role['id']

    utility.dump_json(roles,out_dir,script_name)

def gen_script(script, script_folder, description_folder, json_folder):
    out_dir = os.path.join(script_folder,script)
    try:
        pass
        os.makedirs(out_dir)
    except FileExistsError:
        # directory already exists
        pass
    for locale in const.known_locales:
        gen_script_locale(out_dir, script, locale, description_folder, json_folder)


def gen_script_locale(out_dir, script_name, locale, description_folder, json_folder):
    roles = []
    script = utility.load_json(description_folder, script_name)
    all_roles = utility.load_json(json_folder,locale)
    for role in all_roles:
        if role['id'] in script:
            roles.append(role)

    for role in  roles:
        role['id'] = locale+"_"+role['id']

    utility.dump_json(roles,out_dir,locale)

def gen_specific(out_dir, script_name, locale, description_folder, json_folder):
    roles = []
    script = utility.load_json(description_folder, script_name)
    all_roles = utility.load_json(json_folder,locale)
    for role in all_roles:
        if role['id'] in script:
            roles.append(role)

    for role in  roles:
        role['id'] = locale+"_"+role['id']

    utility.dump_json(roles,out_dir,script_name+"_"+locale)
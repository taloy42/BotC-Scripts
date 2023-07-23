import generate_scripts
import create_json_from_csv
import click
import const
import os

@click.group()
def cli():
    pass

def gen_json_aux(csv_dir,json_dir,locale):
    locale_specific = locale is not None
    click.echo(f"Generating json file for {locale if locale_specific else 'every locale'}")
    if locale_specific:
        create_json_from_csv.gen_locale_json(locale,csv_dir,json_dir)
    else:
        create_json_from_csv.gen_all_json(csv_dir,json_dir)
    click.echo("Finished generating json")

@click.command(short_help="Generate json based on csv")
@click.option('--csv-dir',default=const.csv_folder, help='directory where all the csv files are')
@click.option('--json-dir',default=const.json_folder, help='directory where all the json files will be stored')
@click.option('--locale',default=None,help='specific locale to generate')
def gen_json(csv_dir,json_dir,locale):
    '''Generate the basic json files for the scripts based on the known(or specified) locales' csv'''
    gen_json_aux(csv_dir,json_dir,locale)


def gen_scripts_aux(desc_dir,json_dir,script_dir,locale,script):
    locale_specific = locale is not None
    script_specific = script is not None
    click.echo(f"Generating {script if script_specific else 'all of the scripts'} for {locale if locale_specific else 'every locale'}")
    scripts = [x[:x.rindex('.')] for x in os.listdir(desc_dir)]
    if locale_specific and script_specific:
        generate_scripts.gen_specific(script_dir,script,locale,desc_dir,json_dir)
    if locale_specific and not script_specific:
        generate_scripts.gen_locale(locale,script_dir,scripts,desc_dir,json_dir)
    if not locale_specific and script_specific:
        generate_scripts.gen_script(script, script_dir, desc_dir,json_dir)
    if not locale_specific and not script_specific:
        generate_scripts.generate(script_dir, scripts,desc_dir,json_dir)
    click.echo(f"Finished generating script{'' if script_specific else 's'}")

@click.command(short_help="Generate script json")
@click.option('--desc-dir',default=const.description_folder,help='the directory where the script description are located')
@click.option('--json-dir',default=const.json_folder,help='directory where all the json files for the locales are located')
@click.option('--script-dir',default=const.script_folder,help='the directory where the scripts will be stored')
@click.option('--locale',default=None,help='specific locale to generate')
@click.option('--script',default=None,help='specific script to generate')
def gen_scripts(desc_dir,json_dir,script_dir,locale,script):
    '''Generate the script json to upload to clocktower.online and its relatives based on the locale json and the script description'''
    gen_scripts_aux(desc_dir,json_dir,script_dir,locale,script)

@click.command(short_help="Generate all")
@click.option('--csv-dir',default=const.csv_folder, help='directory where all the csv files are')
@click.option('--json-dir',default=const.json_folder, help='directory where all the json files will be stored')
@click.option('--desc-dir',default=const.description_folder,help='the directory where the script description are located')
@click.option('--script-dir',default=const.script_folder,help='the directory where the scripts will be stored')
@click.option('--locale',default=None,help='specific locale to generate')
@click.option('--script',default=None,help='specific script to generate')
def gen_all(csv_dir,json_dir,desc_dir,script_dir,locale,script):
    '''Generate all the json necessary and then generates the script based on the script-description'''
    gen_json_aux(csv_dir,json_dir,locale)
    gen_scripts_aux(desc_dir,json_dir,script_dir,locale,script)
    click.echo("Done with everything!")
    
cli.add_command(gen_json)
cli.add_command(gen_scripts)
cli.add_command(gen_all)
if __name__=="__main__":
    cli()
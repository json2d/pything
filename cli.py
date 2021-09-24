import json
import argparse

import pything as pyt

def cli():
    p = argparse.ArgumentParser(description = 'does pything stuff via cli]')
    subparsers = p.add_subparsers()

    p_do_stuff = subparsers.add_parser('do_stuff')
    p_do_stuff.set_defaults(menu='do_stuff')
    
    p_do_stuff.add_argument('-config', '-c', dest='config_name')
    
    p_do_crazier_stuff = subparsers.add_parser('do_crazier_stuff')
    p_do_crazier_stuff.set_defaults(menu='do_crazier_stuff')

    p_do_crazier_stuff.add_argument('-config', '-c', dest='config_name')

    p_do_crazier_stuff.add_argument(
        '-msg', '-m', dest='msg', type=str, default='hello world via cli'
    )
    p_do_crazier_stuff.add_argument(
        '-yell', '-y', dest='yell', action='store_true', default=False
    )    


    args = p.parse_args()

    # read config file, optionally for a specific context
    if args.config_name is None:
        config_path = "config.json"
    else:
        config_path = f"config.{args.config_name}.json"
        print(f'Using config file: {config_path}')

    with open(config_path, 'r') as fp: 
        CONFIG = json.load(fp)
    
    if args.menu == 'do_stuff':
        pyt.do_stuff()
    elif args.menu == 'do_crazier_stuff':
        pyt.do_crazier_stuff(
            msg = args.msg, 
            yell = args.yell, 
            extra_msg = CONFIG['extra_msg']
        )



if __name__ == '__main__':
    cli()

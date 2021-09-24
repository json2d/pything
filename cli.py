import argparse

import pything as pyt

def cli():
    p = argparse.ArgumentParser(description = '[🐍pything-cli]')
    subparsers = p.add_subparsers()

    p_do_stuff = subparsers.add_parser('do_stuff')
    p_do_stuff.set_defaults(menu='do_stuff')

    p_do_crazier_stuff = subparsers.add_parser('do_crazier_stuff')
    p_do_crazier_stuff.set_defaults(menu='do_crazier_stuff')

    p_do_crazier_stuff.add_argument(
        '-msg', '-m', dest='msg', type=str, default='hello world via cli'
    )
    p_do_crazier_stuff.add_argument(
        '-yell', '-y', dest='yell', action='store_true', default=False
    )    


    args = p.parse_args()

    if args.menu == 'do_stuff':
        pyt.core.do_stuff()
    elif args.menu == 'do_crazier_stuff':
        pyt.core.do_crazier_stuff(args.msg, args.yell)

if __name__ == '__main__':
    cli()

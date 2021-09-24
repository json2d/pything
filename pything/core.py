import logging
log = logging.getLogger("[🐍pything]")
log.addHandler(logging.NullHandler()) # ignore log messages by defualt

def do_stuff():
  print('...')
  return 42

def do_crazier_stuff(msg='hello world', yell=False):
  print('...', f'{msg}{"!!!" if yell else ""}')
  return 42
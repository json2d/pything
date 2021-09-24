from loguru import logger

def do_stuff():
  logger.info('...')
  return 42

def do_crazier_stuff(msg='hello world', yell=False, extra_msg="try your baz"):
  logger.info(f'{msg}{"!!!" if yell else "."} {extra_msg}')
  return 42
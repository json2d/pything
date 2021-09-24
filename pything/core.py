def do_stuff():
  print('...')
  return 42

def do_crazier_stuff(msg='hello world', yell=False, extra_msg="try your baz"):
  print(f'{msg}{"!!!" if yell else "."} {extra_msg}')
  return 42
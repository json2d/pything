import dotrelay

import unittest

with dotrelay.Radio(__file__): # 📻
  import pything as pyt

class TestEverything(unittest.TestCase):

  def test_base(self):
    
    self.assertEqual(pyt.do_stuff(), 42)
    self.assertEqual(pyt.do_crazier_stuff(), 42)

unittest.main()
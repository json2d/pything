import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

import unittest

import pything as pyt

class TestEverything(unittest.TestCase):

  def test_base(self):
    
    self.assertEqual(pyt.do_stuff(), 42)
    self.assertEqual(pyt.do_crazier_stuff(), 42)

unittest.main()
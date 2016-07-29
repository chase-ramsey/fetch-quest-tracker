import unittest
from lootbag import *

class TestLootbag(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.loot = Lootbag()

  def test_lootbag_setup(self):
    self.assertIsInstance(self.loot.quests, list)

  def test_add_quest(self):
    pass

  def test_remove_quest(self):
    pass

  def test_find_quest_item(self):
    pass

  def test_fulfill_quest(self):
    pass

if __name__ == '__main__':
  unittest.main()

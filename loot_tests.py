import unittest
from lootbag import *
from character import *
from quest import *

class TestQuest(unittest.TestCase):

  def test_quest_setup(self):
    quest = Quest('Abed', 'Die Hard', '50')
    self.assertEqual(quest.person, 'Abed')
    self.assertEqual(quest.item, 'Die Hard')
    self.assertEqual(quest.xp, 50)
    self.assertEqual(quest.found, False)
    self.assertEqual(quest.fulfilled, False)

  def test_mark_item_found(self):
    quest = Quest('Abed', 'Die Hard', '50')
    quest.mark_item_found()
    self.assertEqual(quest.found, True)

  def test_mark_quest_fulfilled(self):
    quest = Quest('Abed', 'Die Hard', '50')
    quest.mark_item_found()
    quest.mark_quest_fulfilled()
    self.assertEqual(quest.found, True)
    self.assertEqual(quest.fulfilled, True)


class TestCharacter(unittest.TestCase):

  def test_create_new_character(self):
    char = Character('Heathcliff', 'Dragon Age: Inquisition', '34', '8000')
    self.assertEqual(char.name, 'Heathcliff')
    self.assertEqual(char.game, 'Dragon Age: Inquisition')
    self.assertEqual(char.level, 34)
    self.assertEqual(char.xp, 8000)

  def test_increase_xp(self):
    char = Character('Heathcliff', 'Dragon Age: Inquisition', '34', '8000')
    char.increase_xp('500')
    self.assertEqual(char.xp, 8500)

  def test_level_up(self):
    char = Character('Heathcliff', 'Dragon Age: Inquisition', '34', '8000')
    char.level_up()
    self.assertEqual(char.level, 35)


if __name__ == '__main__':
  unittest.main()

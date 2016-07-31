import pickle
from character import *
from quest import *

class Lootbag:

  def __init__(self):
    self.character = self.get_character_file()

  def get_character_file(self):
    try:
      with open('character.txt', 'r') as file:
        return pickle.load(file)
    except FileNotFoundError:
      self.create_character()

  def create_character(self):
    pass

  def write_character_file(self):
    pass

  def add_quest(self, person, item, xp):
    pass

  def remove_quest(self, person):
    pass

  def find_quest_item(self, item):
    pass

  def fulfill_quest(self, person):
    pass

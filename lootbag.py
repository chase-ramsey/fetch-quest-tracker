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
    print('What is your character\'s name?')
    name = input('> ')
    print('What game does {0} belong to?'.format(name))
    game = input('> ')
    print('What level is {0}?'.format(name))
    level = input('> ')
    print('How much xp does {0} currently have?'.format(name))
    starting_xp = input('> ')
    return Character(name, game, level, starting_xp)

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

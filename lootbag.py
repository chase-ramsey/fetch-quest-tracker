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
    print('How much XP does {0} currently have?'.format(name))
    starting_xp = input('> ')
    return Character(name, game, level, starting_xp)

  def write_character_file(self):
    with open('character.txt', 'w+') as file:
      pickle.dump(self.character, file)

  def add_quest(self):
    print('Who are you questing for?')
    person = input('> ')
    print('What are you fetching for {0}'.format(person))
    item = input('> ')
    print('How much XP will you receive when you complete the quest?')
    xp = input('> ')
    new_quest = Quest(person, item, xp)
    self.character.quests.append(new_quest)

  def remove_quest(self):
    print('Who is the quest for?')
    qp = input('> ')
    print('What item were you fetching for {0}?'.format(qp))
    qi = input('> ')
    for quest in self.character.quests:
      if quest.person == qp and quest.item == qi:
        self.character.quests.remove(quest)

  def find_quest_item(self, item):
    pass

  def fulfill_quest(self, person):
    pass

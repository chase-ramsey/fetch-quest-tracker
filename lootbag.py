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

  def add_quest(self, *args):
    if len(args) > 0 and len(args) < 3:
      print('Looks like you don\'t have all the info needed to add a quest. Try again, or type "python run.py" with no arguments if you\'ve forgotten what you need.')
    else:
      if len(args) == 0:
        print('Who are you questing for?')
        person = input('> ')
        print('What are you fetching for {0}'.format(person))
        item = input('> ')
        print('How much XP will you receive when you complete the quest?')
        xp = input('> ')
      elif len(args) == 3:
        item = args[0]
        person = args[1]
        xp = args[2]
      new_quest = Quest(person, item, xp)
      self.character.quests.append(new_quest)

  def remove_quest(self, *args):
    if len(args) > 0 and len(args) < 2:
      print('Looks like you don\'t have all the info needed to add a quest. Try again, or type "python run.py" with no arguments if you\'ve forgotten what you need.')
    else:
      if len(args) == 0:
        print('Who is the quest for?')
        qp = input('> ')
        print('What item were you fetching for {0}?'.format(qp))
        qi = input('> ')
      elif len(args) == 2:
        qp = args[0]
        qi = args[1]
      for quest in self.character.quests:
        if quest.person == qp and quest.item == qi:
          self.character.quests.remove(quest)

  def find_quest_item(self, *args):
    if len(args) == 0:
      print('What item did you find?')
      item = input('> ')
      print('Who are you delivering the item to?')
      person = input('> ')
    elif len(args) == 2:
      person = args[0]
      item = args[1]
    for quest in self.character.quests:
      if quest.person == person and quest.item == item:
        quest.mark_item_found()

  def fulfill_quest(self, *args):
    if len(args) == 0:
      print('What item did you deliver?')
      item = input('> ')
      print('Who did you fetch the item for?')
      person = input('> ')
    elif len(args) == 2:
      person = args[0]
      item = args[1]
    for quest in self.character.quests:
      if quest.person == person and quest.item == item:
        if quest.found == True:
          quest.mark_quest_fulfilled()
        else:
          print('That item hasn\'t been marked as found yet. Would you like to mark it as found and fulfill the quest? [yes / no]')
          answer = input('> ')
          if answer.lower() == 'yes':
            quest.mark_item_found()
            quest.mark_quest_fulfilled()

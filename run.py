import sys
from lootbag import *

class Run:

  def __init__(self):
    self.loot = Lootbag()

  def run_args(self):
    if len(sys.argv) == 1:
      print('Current character: ' + self.loot.character.name)
      print('Current game: ' + self.loot.character.game)
      print('Character level: ' + str(self.loot.character.level))
      print('Character XP: ' + str(self.loot.character.xp))
      print('')
      print('Type "help" to see a list of options, or type "list" to see all active quests.')
    else:
      if sys.argv[1].lower() == 'help':
        with open('help.txt', 'r') as file:
          for line in file:
            print(line)
      if sys.argv[1].lower() == 'list':
        print('')
        print('Incomplete Quests')
        print('======================')
        for inc_quest in self.loot.character.quests:
          if inc_quest.fulfilled == False:
            print('Quest item: ' + inc_quest.item)
            print('Fetching for: ' + inc_quest.person)
            print('XP when completed: ' + str(inc_quest.xp))
            if inc_quest.found == True:
              print('This item has been found, but not delivered.')
            else:
              print('This item has not yet been found.')
            print('')
        print('')
        print('Complete Quests')
        print('======================')
        for comp_quest in self.loot.character.quests:
          if comp_quest.fulfilled == True:
            print('Quest item: ' + comp_quest.item)
            print('Fetched for: ' + comp_quest.person)
            print('XP when completed: ' + str(comp_quest.xp))
            print('')
        print('')
      elif sys.argv[1].lower() == 'add':
        try:
          person = sys.argv[2]
          item  = sys.argv[3]
          xp  = sys.argv[4]
          self.loot.add_quest(person, item, xp)
        except IndexError:
          self.loot.add_quest()
      elif sys.argv[1].lower() == 'remove':
        try:
          person = sys.argv[2]
          item  = sys.argv[3]
          self.loot.remove_quest(person, item)
        except IndexError:
          self.loot.remove_quest()
      elif sys.argv[1].lower() == 'found':
        try:
          person = sys.argv[2]
          item  = sys.argv[3]
          self.loot.find_quest_item(person, item)
        except IndexError:
          self.loot.find_quest_item()
      elif sys.argv[1].lower() == 'fulfill':
        try:
          person = sys.argv[2]
          item  = sys.argv[3]
          self.loot.fulfill_quest(person, item)
        except IndexError:
          self.loot.fulfill_quest()
      else:
        print('Sorry, I didn\'t understand your request. Take a look at the commands below, and make sure you formatted yours correctly. You can also type "list" as the program\'s first argument to see what quests are active.')
        print('')
        with open('help.txt', 'r') as file:
          for line in file:
            print(line)

run = Run()
run.loot.get_character_file()
run.run_args()
run.loot.write_character_file()

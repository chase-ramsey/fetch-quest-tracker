import pickle

class Lootbag:

  def __init__(self):
    self.quests = self.get_quest_file()

  def get_quest_file(self):
    try:
      with open('quests.txt', 'r') as file:
        return pickle.load(file)
    except FileNotFoundError:
      return list()

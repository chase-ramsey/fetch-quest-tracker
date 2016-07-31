class Character:

  def __init__(self, name, game, level, starting_xp):
    self.name = name
    self.game = game
    self.level = int(level)
    self.xp = int(starting_xp)
    self.quests = []

  def increase_xp(self, num):
    num = int(num)
    self.xp += num

  def level_up(self):
    self.level += 1

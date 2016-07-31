class Character:

  def __init__(self, name, game, level, starting_xp):
    self.name = name
    self.game = game
    self.level = level
    self.xp = starting_xp
    self.quests = []

  def increase_xp(self, num):
    pass

  def level_up(self):
    pass

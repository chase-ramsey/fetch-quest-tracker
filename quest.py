class Quest:

  def __init__(self, person, item, xp):
    self.person = person
    self.item = item
    self.xp = int(xp)
    self.found = False
    self.fulfilled = False

  def mark_item_found(self):
    self.found = True

  def mark_quest_fulfilled(self):
    self.fulfilled = True

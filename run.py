import sys
from lootbag import *

class Run:

  def __init__(self):
    # self.loot = Lootbag()
    pass

  def run_args(self):
    if len(sys.argv) == 1:
      with open('help.txt', 'r') as file:
        for line in file:
          print(line)

run = Run()
run.run_args()

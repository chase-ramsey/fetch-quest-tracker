# Fetch Quest Terminal Tracker

Fetch Quest Terminal Tracker is a Python program that allows you to keep track of the progress of fetch quests for an RPG character. You can add, remove, find items for, or fulfill quests by navigating the program's prompts, or you can modify your list of quests quickly by providing info as arguments to the program when running it.

### Run

Start the program by running the `run.py` file and adding any necessary arguments. With no arguments, the program will show your current character information. If you haven't entered your character's information into the program before, you'll be allowed to do so at this time.

The first argument for the program is the task you want the FQTT to perform. For example, typing `help` as the first argument will bring up info on all of the commands you can use. You can also add arguments after the initial command to quick-perform some of the programs tasks. Here's the help menu breakdown of all commands and arguments:

> `add [person] [item] [XP]` - Typing "add" as the program's first argument will take you through a prompt to add a new quest. However, you can also quickly add a quest by providing the arguments listed (i.e. "add Frodo ring 1000".)

> `remove [person] [item]` - Typing "remove" as the program's first argument will take you through a prompt to delete a previously added quest. As with add, you can quickly remove a quest by providing the arguments listed when running the program (i.e. "remove Frodo ring").

> `found [item] [person]` - Typing "find" as the program's first argument will take you through a prompt to mark a quest item as found. Adding item and person as arguments will allow you to quickly mark the item as found (i.e. "find ring Frodo")

> `fulfill [person] [item]` - Typing "fulfill" as the program's first argument will take you through a prompt to mark a quest as completed. Adding person and item as arguments will allow you to quickly mark the quest as completed (i.e. "fulfill Frodo ring")

> `list` - Typing "list" will print a list of all active quests, both completed and incomplete.


Here's a [link](https://github.com/nashville-software-school/python-milestones/blob/master/02-command-line-applications/exercises/CLI_BAG_OF_LOOT.md) to the exercise FQTT is based on. I made it about RPGs to have some fun.

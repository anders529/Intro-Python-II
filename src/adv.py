from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
print('Let\'s play a game! \n')
player_name = input("What's your name? :  ")

player = Player('AARON', room["outside"])


def print_controls():
    print('\nControls:')
    print(' n = north \n s = south \n e = east \n w = west')
    print(' q to exit game')


choices = ['n', 's', 'e', 'w', 'q']

print_controls()

choice = 0

lantern = Item('lantern', 'This lantern will light the path.')
room['overlook'].add_item(lantern)

print(
    f'\n  You are standing near the {player.location.name} \n\n  {player.location.description}')

while choice != 'q':
    choice = input('\nChoose direction: ')
    if choice == 'n':
        player.location = player.location.n_to
        print(
            f'\n  You run north towards the {player.location.name} \n\n  {player.location.description}')
    elif len(player.location.items) != 0:
        print(f'\n  You see a {player.location.items[0]}')

    if choice == 's':
        player.location = player.location.s_to
        print(
            f'\n  You run South towards the {player.location.name} \n\n  {player.location.description}')
    elif len(player.location.items) != 0:
        print(f'\n  You see a {player.location.items[0]}')

    if choice == 'e':
        player.location = player.location.e_to
        print(
            f'\n  You run East into the {player.location.name} \n\n   {player.location.description}')
    elif len(player.location.items) != 0:
        print(f'\n  You see a {player.location.items[0]}')

    if choice == 'w':
        player.location = player.location.w_to
        print(
            f'\n  You run West towards the {player.location.name} \n\n   {player.location.description}')
    elif len(player.location.items) != 0:
        print(f'\n  You see a {player.location.items[0]}')

    if choice not in choices:
        print('\n   That is not a direction! Try again you idiot!!')

    else:
        print("\n   You can't go that way! Are you that stupid!?")

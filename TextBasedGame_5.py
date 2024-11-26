# Method: main.py
# Author: Antonia Watts
# Date: 04/18/2024
# This program is a cat-themed text based adventure game. You must collect all items to win. 

# a dictionary that links a room to other rooms and respective items.
rooms = {
        'Kitchen': {'South': 'Brunch Hall'},
        'Brunch Hall': {'North': 'Kitchen', 'West': 'Coffee Bar', 'item': 'Fish Cake'},
        'Coffee Bar': {'West': 'Restroom', 'North': 'Staff Room', 'South': 'Library', 'East': 'Brunch Hall', 'item': 'Cat Cappuccino'},
        'Restroom': {'East': 'Coffee Bar', 'item': 'Kitty Litter'},
        'Library': {'East': 'Basement', 'North': 'Coffee Bar', 'item': 'Kitty Kungfu'},
        'Staff Room': {'East': 'Lounge', 'South': 'Coffee Bar', 'item': 'Recruited Staff'},
        'Basement': {'West': 'Library', 'item': 'Bones'},
        'Lounge':{'West': 'Staff Room'}
}

# introduction and instructions for the game
def game_introduction():
    print('You are a hard-working cat in charge of running your Cozy Cat Cafe.')
    print('You were working in the Kitchen when you suddenly catch the scent of dogs!')
    print("You must collect all 6 required Items before you encounter the Lounge, or you're dog meat!")
    print('Move around the Cafe using: go [North, South, East, or West]')
    print('Pick up useful Items using: get [item name]')
    print('Check what items are in your inventory with: check')
    print('If you wish to quit, use exit')
    print('You start your journey here in the Kitchen.')

# player starting room and starting inventory (empty)
current_room = 'Kitchen'
user_inventory = []
boss_room = 'Lounge'

# getting new player room in perspective of players current room
def move_room(input_direction, current_room):
    global user_inventory
    global rooms

    if input_direction in rooms[current_room]:
        new_room = rooms[current_room][input_direction]
        print('You are now in the', new_room)
        # checking if the room has an item and informing user
        if 'item' in rooms[new_room]:
            item = rooms[new_room]['item']
            print('You found', item)
    
        return new_room
    else:
        print('Invalid direction')
        return current_room

# defined check inventory and exit, both optional actions executed by player
def check_inv():
     print('Inventory:', user_inventory)

def game_close():
    print('See you next time.')

# main loop for the game
def main():
    game_introduction() #calling game introduction

    current_room = 'Kitchen'
    while True:
        player_command = input('What would you like to do?').lower()
        action, *params = player_command.split() 
        # capitalizing user input for directions
        if action == 'go':
            direction = params[0].capitalize() 
            if direction in rooms[current_room]:
                current_room = move_room(direction, current_room) # passing the user's current room as a parameter
            else:
                print('Invalid direction')
        elif action == 'get':
            if len(params) == 0:
                print('Enter the item you wish to get')
            else:
                item_name = ' '.join(params).lower()
            # checking if player requested item is in the current room
            if 'item' in rooms[current_room]:
                room_item = rooms[current_room]['item']
                if item_name.lower() == room_item.lower():
                    user_inventory.append(room_item)
                    del rooms[current_room]['item']
                    print('You have added', {room_item}, 'to your inventory.')
                else:
                    print('No item found.')
            else:
                print('Item is not in this room.')
        elif action == 'check':
            check_inv()
        elif action == 'exit':
            game_close()
            break
        else:
            print('Invalid input.')
        # creating win condition as the player needs 6 items when reaching the boss room
        if len(user_inventory) == 6 and current_room == boss_room:
            print('You have defeated the boss... YOU WIN!')
            break
        # player loses if they do not have 6 items
        if len(user_inventory) != 6 and current_room == boss_room:
            print('You were not prepared and got slain... Try Again!')
            break

if __name__ == '__main__':
    main()








   







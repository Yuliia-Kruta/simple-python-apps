# Yuliia Kruta
"""
A simple text-based adventure game called: Creepy House.

Available commands include:
    go <compass direction>
    take <object>
    # modified drop command for dropping specific objects
    drop <object>
    quit
"""

# current location: hallway, lounge or bedroom
state = "hallway"

# the list of objects that the player is carrying around (includes "nothing").
carrying = ["nothing"]

# global dictionary of the movable objects in each location
items_in = {"bedroom": ["aquarium", "bats"],
            "hallway": [],
            "lounge": ["stereo"]
            }


#####################################################
# Functions for describing the current location


def describe_bedroom():
    print("You are in a bedroom.")


def describe_hallway():
    print("You are in a dark hallway.")
    print("There is a table beside you, and a bright light to the west.")


def describe_lounge():
    print("You are in a brightly-lit lounge with two red sofas")


def describe():
    """Print a description of the current location."""
    if state == "hallway":
        describe_hallway()
    elif state == "lounge":
        describe_lounge()
    elif state == "bedroom":
        describe_bedroom()
    else:
        print("ERROR: unknown location: " + str(state))
    for item in items_in[state]:
        print("You can see: " + item)


#######################################################
# Functions for moving between locations

def move_lounge(direction):
    if direction == "west":
        return "bedroom"
    elif direction == "east":
        return "hallway"
    return ""


def move_hallway(direction):
    if direction == "west":
        return "lounge"
    # allows to go outside if there is aquarium in the list of carried things
    elif direction == "east" and ("aquarium" in carrying):
        return "outside"
    return ""


def move_bedroom(direction):
    if direction == "east":
        return "lounge"
    return ""


def move_cmd(direction):
    """Attempt to move in the given direction.

    This updates the 'state' variable to the new location,
    or leaves it unchanged and prints a warning if the move was not valid.
    :param direction: a compass direction, "north", "east", "south", or "west".
    :return: None
    """
    global state
    if state == "hallway":
        new_state = move_hallway(direction)
    elif state == "lounge":
        new_state = move_lounge(direction)
    elif state == "bedroom":
        new_state = move_bedroom(direction)
    else:
        print("WARNING: move_cmd sees unknown state: " + state)
        new_state = ""
    # now check to see if it was a valid move
    if new_state == "":
        print("You cannot go " + str(direction) + " from here.")
    else:
        state = new_state


#########################################################
def take_cmd(obj):
    """Try to pick up the given object.
    Most objects can only be picked up when in the correct room.
    """
    global carrying

    if obj in items_in[state]:
        # adds the object to the list of carried objects
        carrying.append(obj)
        print("You picked up " + obj)
        items_in[state].remove(obj)
    else:
        print("You cannot pick that up!")


def drop_cmd(obj):
    """Drop the object if it is not 'nothing' and if it is present in the list of carried objects"""
    if obj in carrying and obj != 'nothing':
        print("You dropped " + obj)
        items_in[state].append(obj)
        # removes an object from the list of carried objects
        carrying.remove(obj)
    else:
        print("You cannot drop that!")


#########################################################

def show_inventory():
    """Show the list of currently carried objects, excluding the 'nothing' item"""
    print("Your inventory: ")
    print(*(item for item in carrying if item != "nothing"), sep=", ")


#########################################################
# The main loop that processes the player's input commands.
def main():
    for turn in range(20, 0, -1):
        print("")
        describe()
        cmd = ' '.join(input("Enter your command " + str(turn) + "> ").lower().split())
        if cmd == "quit":
            print("You gave in so easily :-(")
            break
        elif cmd.startswith("go "):
            where = cmd[3:]
            move_cmd(where)
            if state == "outside":
                print("You push the door open with the heavy aquarium and escape to outside!")
                break
        elif cmd.startswith("take "):
            obj_name = cmd[5:]
            take_cmd(obj_name)
        # modified drop command for dropping specific objects
        elif cmd.startswith("drop "):
            obj_name = cmd[5:]
            drop_cmd(obj_name)
        # inventory command to show the list of carried things
        elif cmd == "inventory":
            show_inventory()
        else:
            print("I do not understand '" + cmd + "'.  Try go/take/quit")
    print("Game over")


if __name__ == "__main__":
    main()

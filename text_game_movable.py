# Yuliia Kruta
"""
A simple text-based adventure game called: Creepy House.

Available commands include:
    go <compass direction>
    take <object>
    drop #new command added to drop objects
    quit
"""

# current location: hallway, lounge or bedroom
state = "hallway"

# the object that the player is carrying around (or "nothing").
carrying = "nothing"

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
    # prints objects that are located in the current room
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
    elif direction == "east" and carrying == "aquarium":
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

    # checks if the object that user wants to take is present at current location
    if obj in items_in[state]:
        # drops a current object that is carried to take a new one
        drop_cmd()
        carrying = obj
        print("You picked up " + carrying)
        # removes an object that is taken from current location
        items_in[state].remove(carrying)
    else:
        print("You cannot pick that up!")


def drop_cmd():
    """ Drop the object that is currently carried"""

    global carrying
    print("You dropped " + carrying + " at the " + state)
    # Adds an object to the list of objects at the current location
    if carrying != 'nothing':
        items_in[state].append(carrying)
        carrying = 'nothing'


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
        # new command to drop objects
        elif cmd == "drop":
            drop_cmd()
        else:
            print("I do not understand '" + cmd + "'.  Try go/take/quit")
    print("Game over")


if __name__ == "__main__":
    main()

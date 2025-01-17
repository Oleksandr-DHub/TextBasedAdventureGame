import random

# initialise variables
maxNS = -1
maxEW = -1
currentNS = 0
currentEW = 0
exitNS = 0
exitEW = 0
myloot = 0
loot_density = -1
monster_density = -1

# Set valid instructions
directions = ["n","s","e","w","l","q"]

# Check for blocked exits
def blocked_exit():
    if currentNS == maxNS:
        print("Your path north is blocked by a wall.")
    if currentEW == maxEW:
        print("Your path east is blocked by a wall.")
    if currentNS == 1:
        print("Your path south is blocked by a wall.")
    if currentEW == 1:
        print("Your path west is blocked by a wall.")
        
# Print out description of the new room
def where_am_i():
    print("\nYou are in",this_room[currentNS - 1][currentEW - 1],"\n")
    blocked_exit()
    if this_loot[currentNS - 1][currentEW - 1] >0:
        print("\nSomething golden glints in the gloom.\n")

# Set up size of dungeon and loot density
userchoice = "0"
userchoice = input("Enter s to (s)et your own parameters for the adventure, anything else for a randomly sized dungeon: ")

if userchoice == "s":
    while maxEW < 2:
        try:
            maxEW = int(input("Maximum size (2 or more) or 0 to exit: "))
        except ValueError:
            print("Please enter an integer of 2 or more for the maximum dungeon size, or 0 to exit.")
        if maxEW == 0:
            print("You have chosen to exit, goodbye!")
            exit()

    maxNS = maxEW

    while loot_density < 1 or loot_density > 10:
        try:
            loot_density = int(input("Loot density from 1 to 10 or 0 to exit: "))
        except ValueError:
            print("Please enter an integer of 1 or more for the loot density, or 0 to exit.")
        if loot_density == 0:
            print("You have chosen to exit, goodbye!")
            exit()
else:
    maxEW = random.randint(2,4)
    maxNS = maxEW
    loot_density = random.randint(1,10)
 
# Assign user entry point
currentNS = random.randint(1, maxNS)
currentEW = random.randint(1, maxEW)
exitNS = currentNS
exitEW = currentEW

# Assign user exit point, ensuring it can't be the entry point
while ((exitNS == currentNS) and (exitEW == currentEW)):
    exitNS = random.randint(1, maxNS)
    exitEW = random.randint(1, maxEW)

# Create random rooms
room_start = ["an abandoned", "a chill", "a dismal", "a dark", "a gloomy", "an echoing", "a foetid", "an ominous", "a shadowy", "an icy", "a ruined"]
room_type = ["hall", "torture chamber", "feasting hall", "kitchen", "latrine", "dungeon", "empty armoury", "cavern", "barracks","chapel"]
room_end = ["strewn with bones.", "heaped with waste.", "damp with fresh urine.", "filled with horrors best left unmentioned.", "spattered with blood.", "squeaking with rats.", "reeking of rotting corpses."]

# 2D lists for room descriptions and loot
this_room = [["a dark and abandoned chamber" for x in range(maxNS)] for y in range(maxEW)]
this_loot = [[0 for x in range(maxNS)] for y in range(maxEW)]

# Populate rooms with descriptions and loot
ns_room = 0
while ns_room < maxNS:
    ew_room = 0
    while ew_room < maxEW:
        this_room[ns_room][ew_room] = room_start[random.randint(0, len(room_start)-1)] + " " + room_type[random.randint(0, len(room_type)-1)] + " " + room_end[random.randint(0, len(room_end)-1)]
        loot_here = random.randint(1,10)
        if loot_here <= loot_density:
            this_loot[ns_room][ew_room] = random.randint(10,1000)
        ew_room = ew_room + 1
    ns_room = ns_room + 1

# User intro
print("\nYou wake groggily in absolute darkness, your left cheek numb and cold against the wet stone floor.")
print("Wondering how you got here, and having no memory beyond that sixth \"one for the road\", you get up intent on escaping.")
where_am_i()

# Loop until user finds the exit or quits
while True:
    direction = input("Do you want to go (n)orth, (s)outh, (e)ast or (w)est, (l)oot room or (q)uit?: ")
    mymove = "invalid"

    # If the direction is valid, then loot the room,  move the character along the grid or else feedback or quit if that is selected
    if direction in directions:
        if direction == 'q':
            print("\nYou have chosen to flee the dark horrors of this dungeon. Farewell, you cowardly cur!")
            break
        if direction == 'l':
            if this_loot[currentNS -1][currentEW -1] > 0:
                print("You quickly gather up the",this_loot[currentNS-1][currentEW-1],"gold pieces worth of loot")
                myloot = myloot + this_loot[currentNS - 1][currentEW -1]
                this_loot[currentNS -1][currentEW -1] = 0
                continue
            else:
                print("You scrabble about but find no riches here.")
                continue
        if direction == 'n':
            if currentNS+1 <= maxNS:
                currentNS = currentNS+1
                mymove = "north"
        if direction == 's':
            if currentNS-1 > 0:
                currentNS = currentNS-1
                mymove = "south"
        if direction == 'e':
            if currentEW+1 <= maxEW:
                currentEW = currentEW+1
                mymove = "east"
        if direction == 'w':
            if currentEW-1 > 0:
                currentEW = currentEW-1
                mymove = "west"
        if mymove == "invalid":
                print("A damp and slimy wall blocks your route in that direction.")
                continue
    else:
        print("You can only enter", " or ".join(directions), "so please try again.")
        continue
    
    # Move the character and check if they've found the exit
    print("\n ------------------------------")
    print("\nYou move " + mymove + ".")
    where_am_i()

    if currentNS == exitNS and currentEW == exitEW:
        print("\nBut can it be? Is that light peering down through the crack in the ceiling?")
        print("\nYes, yes it is! Well done, you've found the exit.")
        # Check if the user wants to stay in the dungeon or leave
        leave = "0"
        while leave != "c" and leave != "f":
            leave = input("\nWould you like to (c)ontinue your adventure or (f)lee to safety?: ")
            if leave == "c":
                print("You nervously decide to press on, leaving the comforts of freedom behind you.\n")
                continue
            elif leave == "f":
                if myloot > 0:
                    print("\nYou clamber to freedom, leaving",myloot,"gold pieces richer.")
                else:
                    print("\nYou clamber wearily to freedom.")
                print("\nNow, to take revenge on those who left you here to rot...\n")
                exit()
            else:
                continue



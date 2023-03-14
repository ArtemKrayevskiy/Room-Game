"""
Creates a game
"""
wins = 0
class Room:
    """
    Creation of class for rooms
    """
    def __init__(self , name) -> None:
        """
        Initialization of class
        """
        self.name = name
        self.possibible_ways = []
        self.inhabitant = None
        self.item = None


    def set_description(self , description):
        """
        Sets decription to class
        """
        self.description = description
        return None
    

    def set_character(self , character):
        """
        Sets a character for room
        """
        self.inhabitant = character

    def link_room(self,room, way_of_world):
        """
        Links rooms between each other
        """
        self.possibible_ways.append((room , way_of_world))

    def set_item(self ,item):
        """
        Sets item for a room
        """
        self.item = item 

    def get_details(self):
        """
        Gives decription of  a room
        """
        return self.description

    def get_character(self):
        """
        Returns a character which is in this room
        """
        return self.inhabitant
    
    def get_item(self):
        """
        returns item which is in this room
        """
        return self.item
    
    def move(self , way):
        """
        Shows if user changed room or not 
        """
        for i in self.possibible_ways:
            if i[1] == way:
                return i[0]
    
class Enemy:
    """
    Creates class for enemies
    """
    def __init__(self , name , decription) -> None:
        """
        Initialization of class
        """
        self.name = name
        self.description = decription

    
    def set_conversation(self , phrase):
        """
        Sets a phrase which enemy will say if user would like to talk with him
        """
        self.phrase = phrase

    def set_weakness(self , weakness):
        """
        Sets an item which can beat enemy
        """
        self.weakness = weakness

    def describe(self):
        """
        Returns decribtion of enemy 
        """
        return self.description
        
    def talk(self):
        """
        Returns a phrase of enemy
        """
        return f'[{self.name} says]: {self.phrase}'
    
    def fight(self, item):
        """
        Checks if user's choice can kill a monster
        """
        if self.weakness == item:
            return True
        return False
    
    def get_defeated(self , wins):
        """
        Returns number of wins agains monsters
        """
        return wins


class Item:
    """
    Creates Item class
    """
    def __init__(self , name) -> None:
        """
        Initialization of class
        """
        self.name = name
    
    def set_description(self , decription):
        """
        Sets a decribtion of an item
        """
        self.description = decription

    def describe(self):
        """
        Returns decribtion of item 
        """
        return f'The [{self.name}] is here - {self.description}'
    
    def get_name(self):
        """
        Returns name of item
        """
        return self.name

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("What's up, dude! I'm hungry.")
dave.set_weakness("cheese")
dining_hall.set_character(dave)


tabitha = Enemy("Tabitha", "An enormous spider with countless eyes and furry legs.")
tabitha.set_conversation("Sssss....I'm so bored...")
tabitha.set_weakness("book")
ballroom.set_character(tabitha)

cheese = Item("cheese")
cheese.set_description("A large and smelly block of cheese")
ballroom.set_item(cheese)

book = Item("book")
book.set_description("A really good book entitled 'Knitting for dummies'")
dining_hall.set_item(book)

current_room = kitchen
backpack = []

dead = False
if __name__ == "__main__":
    while dead == False:

        print("\n")
        print(current_room.name)
        print('--------------------')
        print(current_room.get_details())
        for i in current_room.possibible_ways:
            print(f'{i[0].name} is {i[1]}')

        inhabitant = current_room.get_character()
        if inhabitant is not None:
            print(f'{inhabitant.name} is here!')
            print(inhabitant.describe())

        item = current_room.get_item()
        if item is not None:
            print(item.describe())

        command = input("> ")

        if command in ["north", "south", "east", "west"]:
            # Move in the given direction
            current_room = current_room.move(command)
        elif command == "talk":
            # Talk to the inhabitant - check whether there is one!
            if inhabitant is not None:
                print(inhabitant.talk())
        elif command == "fight":
            if inhabitant is not None:
                # Fight with the inhabitant, if there is one
                print("What will you fight with?")
                fight_with = input()

                # Do I have this item?
                if fight_with in backpack:

                    if inhabitant.fight(fight_with) == True:
                        wins +=1
                        # What happens if you win?
                        print("Hooray, you won the fight!")
                        current_room.inhabitant = None
                        if inhabitant.get_defeated(wins) == 2:
                            print("Congratulations, you have vanquished the enemy horde!")
                            dead = True
                    else:
                        # What happens if you lose?
                        print("Oh dear, you lost the fight.")
                        print("That's the end of the game")
                        dead = True
                else:
                    print("You don't have a " + fight_with)
            else:
                print("There is no one here to fight with")
        elif command == "take":
            if item is not None:
                print("You put the " + item.get_name() + " in your backpack")
                backpack.append(item.get_name())
                current_room.set_item(None)
            else:
                print("There's nothing here to take!")
        else:
            print("I don't know how to " + command)

#Quick test of a kind of RPG game using functions and lists to store information. 
#The game is going to be text based and set in a castle the hero is exploring. 

"""
The layout of the castle is going to be.

Entrance Halls 
        Great Hall 
                [2 Goblins(Easy)]
                [1 Healing Potion]
        Second Floor
                Kings Chamber 
                        [1 Goblin (Hard)]
                        [Chest: 1000 gold]
                Queens wardrobe
                        [Chest: Ancient Crown] 
                Third floor
                        [OUT OF BOUNDS]
        Dungeon 
                [2 Goblins]
                [1 Healing Potion]
        Exit 
                [Ends Game]
        

The end goal of the game is to get the Ancient Crown and then leave the castle. 

The Fighting Mechanic.
        When in a fight the hero can attack and then be attacked by the goblins in turns. 
        When the Hero is attacked they lose between 5 and 10 health (out of: 100). 
        The Hero also gets the option to use a healing potion with their turn, and this will heal 50 points of health. 
        The Hero can do 5-20 points of damage. 

Fuctions Im going to need:
        A Function for every room in the castle.

        A fighting Function. 

        An Opening Screen 

        Death Screen.

"""



"""Things to Note: 
I haven't worked out the perameter passing or how the lists system for storing information is going to work
"""


def File_initalising():
        #This function creates the base files that hold data about each room in the castle.
        #Which includes the hidden loot and any enemies hidden in it. 
        #This bit all works! :D (As in it creates the base files)

        #Initalising the file structure. 
        RoomLog = open("RpgGame/RoomLog.txt", "w")
        
        #Entrance Hall Files 
        #No look or enemies
        Entrance_Hall_Enemies = open("RpgGame/Entrance_Hall_Enemies.txt" , "w")
        Enterance_Hall_Loot = open("RpgGame/Enterance_Hall_Loot.txt" , "w")

        #Great Hall Files 
        Great_Hall_Enemies = open("RpgGame/Great_Hall_Enemies.txt" , "w")
        Great_Hall_Enemies.write("Goblin\nGoblin")
        Great_Hall_Loot = open("RpgGame/Great_Hall_Loot.txt" , "w")
        Great_Hall_Loot.write("Healing Potion")

        #Dungeon Files.
        Dungeon_Enemies = open("RpgGame/DungeonEnemies.txt" , "w")
        Dungeon_Enemies.write("Goblin\nGoblin")
        Dungeon_Loot = open("RpgGame/DungeonLoot.txt" , "w")
        Dungeon_Loot.write("Healing Potion")


        #Second Floor
        #No loot or enemies
        Second_Floor_Enemies = open("RpgGame/SecondFloorEnemies.txt" , "w") 
        Second_Floor_Loot = open("RpgGame/SecondFloorLoot.txt" , "w")

        #Kings Chamber Files 
        Kings_Chamber_Enemies = open("RpgGame/KingsChamberEnemies.txt" , "w")
        Kings_Chamber_Enemies.write("Large Goblin")
        Kings_Chamber_Loot = open("RpgGame/KingsChamberLoot.txt" , "w")
        Kings_Chamber_Loot.write("1000 Gold")

        #Queens Wardrobe
        Queens_Wardrobe_Loot = open("RpgGame/QueensWardrobeLoot.txt" , "w")
        Queens_Wardrobe_Loot.write("Ancient Crown")
        Queens_Wardrobe_Enemies = open("RpgGame/QueensWardrobeEnemies.txt" , "w")       
#Works.

def main():
        #Takes the Heros name and addresses them.
        PlayerName = input("Bishop: Hello, good knight, what is you name, may I ask?: ")
        print ("Bishop: Welcome, Sir ", PlayerName , " you must help us rocover the Ancient Crown from the Old Casle. But the castle is overrun with Goblins. We need you to go and deal with these beats!")
        print ("\nBishop: Here are some Items to help you on your quest")

        #You get given your items 
        ItemsFromBishop = ['Sword', 'Shield', 'Healing Potion', 'Healing Potion', ""]
        HerosInventory  = ItemsFromBishop
        HerosHealth = 100 
        print ("Your Inventory now contains: " , HerosInventory, "\n You have: " , HerosHealth , " Health")

        #The Hero decides if we wants to practice fighting. 
        LearnToFight = False 
        LearnToFight = input( ("\n\nBishop: It's been a while since your last quest, Would you like to practice how to fight? (Y/N)"))
        ValidInput = False 
        while ValidInput == False:
                LearnToFight == ""
                
                if LearnToFight == "Y":
                        ValidInput = True 
                        FightingTutorial(HerosHealth, HerosInventory)
                elif LearnToFight == "N":
                        ValidInput = True 
                        StartOfQuest(HerosInventory, HerosHealth)
                else:
                        print ("I didn't understand that, please try again")
#Above mostly Working

def FightingTutorial(HerosInventory, HerosHealth, Opponent):
        print ("You are lead outside in to a courtyard \n ")
        print ("Bishop: Here you're going to learn how to fight! You're going to fight a dummy we made for you. \n It's not a very hard fight")
        Opponent = "Dummy"        
        Fight(Opponent, HerosHealth, HerosInventory)
        print("Bishop: Now you've learned how to fight you're ready for your quest")
        #Maybe stick an IF function in here to go through it again, or something. 
        StartOfQuest(HerosInventory, HerosHealth)
#Need to fix fighting mechanic before signing off.


def Fight():

  
    
    """
    Notes:

    Variables I'll need to pass in:
    HeroHealth
    HerosInventory 
    Opponent
    
    I still need to make the actual experience more user friendly but it seems like I've gotten the barebones of the project running.
    
    Seems to be mostly working with a few crutches.
    

    """

    #Enemy Stats
    #Structure = [Lower_Damage], [Upper_Damage], [Health].
    GoblinStats = [1, 10 , 10]
    Large_GoblinStats = [5, 20 , 25]
    DummyStats = [1 , 5 , 5]

    #Initalising  variables
    OpponentAttack = [0 , 0]
    OpponentHealth = 0
    HerosAttack = [0 , 0]
    HeroDamange = 0 


    #Set the stats for the opponent
    if Opponent == "Goblin":
            OpponentName = "Goblin"
            OpponentAttack[0] = GoblinStats[0]
            OpponentAttack[1] = GoblinStats[1]
            OpponentHealth = GoblinStats[2]
            OpponentName = "Goblin"
    elif Opponent == "Large_GoblinStats":
            OpponentAttack[0] = Large_GoblinStats[0]
            OpponentAttack[1] = Large_GoblinStats[1]
            OpponentHealth = Large_GoblinStats [2]
            OpponentName = "Large Goblin"
    elif Opponent == "Dummy":
            OpponentAttack[0] = DummyStats[0]
            OpponentAttack[1] = DummyStats[1]
            OpponentHealth = DummyStats[2]
            OpponentName = "Dummy"


    #Calculating the Heros Attack
    #It needs to search through the list one item at a time to find the sword.
    #Search the Heros Inventory for a weapon and then calculate attack based on it.
    counter = 0 
    for item in HerosInventory:
        if HerosInventory[counter] == "Sword" or HerosInventory[counter] == "Axe" or HerosInventory[counter] == "Hammer":
            HerosWeapon = HerosInventory[counter]
            if HerosWeapon == "Sword":
                HerosAttack = [1 , 5]
            elif HerosWeapon == "Axe":
                HerosAttack = [0 , 10]
            elif HerosWeapon == "Hammer":
                HerosAttack = [5 , 7]
            
   
    #Variables used later: OpponentName, OpponentAttack[x,x], OpponentHealth

    import random
    #Stating Combat
    print("You begin combat! You may attack first!")
    fighting = True 
    while fighting == True:
            #Hero Picks their Action 
            UserInput = input("What do you want to do?: \n 1 - Attack! \n 2 - Drink Healing Potion \n")
            
            
            #Hero Decides to Fight 
            if UserInput == "1":
                    print (HerosAttack)
                    HeroDamage = random.randint (HerosAttack[0] , HerosAttack[1])
                    OpponentHealth = OpponentHealth - HeroDamage
                    print("You attack the " , Opponent , " and do: " , HeroDamage , " point of damage")
                    print("The " , Opponent , "s health is now: " , OpponentHealth)
                    
                    if OpponentHealth <= 0:
                            fighting = False

            #Heros drinks Healing Potion
            if UserInput == "2":
                    counter = 0
                    found = False 
                    counter1 = 0
                    counter2 = len(HerosInventory)-1
                    for items in HerosInventory:
                            counter1 = counter +1
                    while found == False:
                        if HerosInventory[counter] == ("Healing Potion"):
                                found = True
                                couner2 = 100
                                print ("Healing potion found")
                                if HerosHealth > 50:
                                        HerosHealth = 100
                                        print("You use the Healing Potion and you return to full health (100) ")
                                        del HerosInventory[counter]
                                elif HerosHealth < 50:
                                        HerosHealth += 50
                                        print ("You use the healing potion to restore 50 health points. Your health is now: " , HerosHealth)
                                        del HerosInventory[counter]
                        elif counter >= counter2:
                            print ("You don't have any healing potions, you wasted your time searching")
                            found = True
                            
                        else:
                                counter = counter +1
                                
                        InventorySize = len(HerosInventory)
                        if counter > InventorySize:
                                found = True
                                print ("You do not have any healing potions")
                    #Healing potion seems to be working, although could use another look over
                    #And more thourough testing later. Otherwise had a good session. 

                    
            #Opponents Turn
            #Calculate the amount of dame the opponent does. 
            if OpponentHealth > 0: 
                    OpponentDamage = random.randint(OpponentAttack[0] , OpponentAttack[1])
                    print ("\n \n The ", OpponentName , " atacks you and does: " , OpponentDamage , " Points of damage" )
                    HerosHealth  = HerosHealth - OpponentDamage
                    print("Your health is now: " , HerosHealth)
                    if HerosHealth <= 0:
                            print("You have been slain by the " , OpponentName , "\nBetter luck next time....")
                            death()
            elif OpponentHealth == 0:
                    print("The " , OpponentName , " is dead! You are victorious \n")
                    fighting = False 
    print("\nYou have won the day!, Congraulations")

    #Resetting the opponent Stats
    Opponent = "error"
    OpponentName = "error"
    OpponentHealth = "error"
    OpponentAttack[0] = "error"
    OpponentAttack[1] = "error"

    #End of Fight (Function Unfinished)
    #Remember to reset the HerosHealth after the fighting.


def StartOfQuest(HerosHealth, HerosInventory):
        print ("""
                You approach the Old Castle on the outskirts of town. It's clear it wasn't been tended to in decades, the burnt out walls appear unguarded and you 
                enter over the collapsed draw bridge. 
                You skirt through the courtyard quickly, feeling the walls watching you, and enter the main castle through the enterence hall. 
                """)
        EntranceHall(HerosHealth, HerosInventory)


#Locations are bellow here 

def EntranceHall(HerosInventory, HerosHealth):
        
        #Replace the little bit with an actual Loot_Log system. 
        Floor = "Nothing"

        print("""

                The entrance halls is a large rectangular space with a collapsed chandelier in the centre. 
                Ahead of you is the enterance to the Great Hall, where you hear some scabbling and movement, 
                to your left is a set of stairs that appear to lead to the second floor. 
                """)
        ValidInput = False 
        while ValidInput == False: 
                UserInput = input("\nWhat do you want to do? \n1 - Go into the Great Hall \n2 - Go upstairs\n3 - Search the room")
                if UserInput == "1" or UserInput == "Great Hall":
                        ValidInput = True 
                        GreatHall(HerosHealth, HerosInventory)
                elif UserInput == "2" or UserInput == "Second Floor": 
                        ValidInput = True 
                        SecondFloor(HerosInventory, HerosHealth)
                elif UserInput == "3" or UserInput == "Search Room":
                        print("You search the room and you find" , Floor)
                else:
                        print("I don't understand what you mean? Please try again")

def GreatHall(HerosInventory, HerosHealth):
        #UNFINISHED But also the base for the rest of the the room that I'll write after this. (Tweak enterence Hall)

        #Set up the room log system here.
        
        """
        if Roomlog != "Great Hall":
        #Sort out this if Statement at some point and work out what the actual code should be. 
                #Adding Great Hall to the Room Log
                RoomLog = open("RpgGame/RoomLog.txt" , "a")
                RoomLog.write("Great Hall")
                
        """
        
        print("""

                You enter the Great Hall, it's a long room with three tables running between you and the kings table. 
                The Floor is partially collapsed and ruble and debris are scattered all over the floor, plates and clutterly are strwen across the tables and floor
                At the far end of the room you see two goblin, but they haven't spotted you yet. What do you do?"
                """)

        #Ask the Heros what they want to do. 
        ValidInput = False 
        while ValidInput == False:
                UserInput = input("What do you want to do?\n1 - Attack the Goblins\n2 - Search the Room\n3 - Leave the room\n")
                
                #Your attack the Goblins! Or you're spotted trying to search the room.
                if UserInput == "1" or UserInput == "2": 
                        counter  = 0 
                        print("The Goblins see you enter move to attack!")
                        while counter != NoOfEnemies + 1:
                                Opponent = Enemies[counter]
                                Fight(Opponent, HerosInventory, HerosHealth)
                        del enemies[0]
                        del enemies[0]
                        GreatHallCleared = True 
                        Great_Hall_Enemies = open("GreatHallEnemies" ,"w")
                        print("You have killed the Goblins! The Great Hall is now empty")

                elif UserInput == "3" or UserInput == "Leave the Room":
                        print("You leave the room")
                        EntranceHall(HerosHealth, HerosInventory)

                #elif RoomLog == "Great Hall":
                        
                        
        #This accessing the room log is something I'll need to sort out.
                        
        UserInput = input("You have been in this room before, what do you want to do?\n2 - search the room for loot\n3 - Leave the room.")
        if UserInput == "2":
                if Great_Hall_Loot != "":
                        print ("After searching the Great Hall you find " , Great_Hall_Loot)
                elif Great_Hall_Loot == "":
                        print("You search the room and find nothing.")

        #I think I neex to fix this and make it suitable for taking and storing a list but this'll do for now. 


        #If there is things there then they can be moved into the Heros inventory then deleting form the txt.


        #Remember to delete the enemies after you've killed them, at the end of the fight session. 


#Create a text file that stores which room you've been in. 
File_initalising()
main()



        






































































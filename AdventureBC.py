import time

def ending():
    print("\nWith plenty of food and water and a cozy shelter to reside in, you quickly assimilate to life on the island. \n"
          "One day, as you go out to the beach to spear some fish, a silhouette of a ship all of a sudden looms over the \n"
          "horizon. Hooray, you are being saved!")
    time.sleep(6)
    print("Congratulations, you have survived this test of survival.")
    print("\n\nTHANKS FOR PLAYING!!")

def bear():
    print("\nAs you approach the cave, you notice a black silhouette roaming around. You see its yellow eyes and \n"
          "immediately you know its a bear! It notices you too and charges toward you! What do you do?")
    time.sleep(5)
    print("1. Fight it!!!")
    time.sleep(2)
    print("2. Run!!!")
    time.sleep(2)
    choice = input("Make your choice:")
    if(choice == 1):
        print("What were you even thinking? Did you think you could a fight off a bear with a measly stick? You are \n"
              "instantly overpowered by the bear, and you are mauled to death.")
        time.sleep(4)
        print("\n\nGAME OVER")
    else:
        print("Good choice! You are able to escape the ravenous bear by climbing up a tree. The bear cannot get to you \n"
              "and it grows extremely frustrated, so it goes away. Relieved, you return to your shelter, cook some meat, \n"
              "and boil some water for drinking. Now, you can finally rest in peace.")
        time.sleep(5)
        ending()

def deer():
    print("\nAs you search for food, you find a deer carcass before you. It looks pretty fresh. Not even flies are \n"
          "buzzing around it. You break off a tree branch and carry some of the meat back toward your shelter.")
    time.sleep(5)
    bear()

def berries():
    print("\nYou walk into the forest and search for something edible. You find some blue berries hanging off a bush, \n"
          "and they do look pretty harmless. You won't survive much longer without food, so do you want to give them a \n"
          "try?")
    time.sleep(5)
    print("1. Sure! Fruit is always a good choice.")
    time.sleep(2)
    print("2. Nah, they look suspicious")
    time.sleep(2)
    choice = input("Make your choice:")
    if(choice == 1):
        print("Worst decision of your short-lived life. The berries are incredibly poisonous, and you die hours later \n"
              "from unpleasant aftereffects. Better luck next time!")
        time.sleep(4)
        print("\n\nGAME OVER")
    else:
        print("Good choice. Never trust wild berries. Let's proceed.")
        time.sleep(3)
        deer()

def food():
    print("\nYou've kindled your fire, but now you're incredibly hungry! What should you do?")
    time.sleep(3)
    print("1. Let's head to the woods.")
    time.sleep(2)
    print("2. It's not worth the risk finding food at night. Let's wait till tomorrow.")
    time.sleep(2)
    choice = input("\nMake your choice:")
    if(choice == 1):
        berries()
    else:
        print("Bad decision. In your sleep, a wolf enters the cave and feasts upon your unfortunate soul. Shouldn't have \n"
              "been lazy and stayed in the cave. Better luck next time!")
        time.sleep(4)
        print("\n\nGAME OVER")

def firewood():
    print("\nAfter 20 minutes, you find a small pile of twigs and brush lying in the dirt. How fortunate! You then go \n"
          "back to the cave to warm up your shelter.")
    time.sleep(5)
    food()

def water():
    print("\nAs you search for something to kindle a fire, you come across a small stream along the way. The water seems \n"
          "quite harmless, and you'd love to take a nice refreshing gulp of H2O. Do you want to take a drink?")
    time.sleep(5)
    print("1. Sure, why not!")
    time.sleep(2)
    print("2. Let's not do that yet.")
    time.sleep(2)
    choice = input("\nMake your choice:")
    if(choice == 1):
        print("\nUnfortunately, you were not smart enough to know that the water was contaminated! You suffer extreme \n"
              "diarrhea the following night and die in agonizing pain.")
        time.sleep(4)
        print("\n\nGAME OVER")
    else:
        print("Good thing you didn't drink it. Who knows how polluted it must be!")
        time.sleep(3)
        firewood()

def cave():
    print("\nYou proceed to the right for 15 minutes, and you come upon a mysterious small cave. You cautiously enter \n"
          "and to your relief, there is nothing awaiting your presence. Now, you need to gather some resources to build \n"
          "a fire as it is quite chilly in your new shelter. It is currently night.")
    time.sleep(5)
    print("\nWhat would you like to do?")
    time.sleep(2)
    print("1. Let's go find some firewood!")
    time.sleep(2)
    print("2. It's too cold and dark out. Let's sleep in instead.")
    time.sleep(2)
    choice = input("\nMake your choice:")
    if(choice == 1):
        water()
    else:
        print("Sadly, not building a fire was the biggest mistake of your life. The island grows frigid in the middle of \n"
              "the night. Subsequently, you die from hypothermia.")
        time.sleep(4)
        print("\n\nGAME OVER")

def main():
    print("Survival of the Fittest: Choose Your Own Adventure!")
    time.sleep(2)
    print("\nYou have been shipwrecked on a remote, desolate island, and you have lost all of your companions and your \n"
          "resources in this tragedy. You scan for any signs of humanity, but all you see is a dark, misty forest in the \n"
          "distance. So you head there. You must survive on this dangerous island until someone passes by and comes to \n"
          "your aid. Will you have the brains to do so??")
    time.sleep(5)
    print("\nYou arrive at a fork in the path, leading to the left, right, or straight on. In which direction do you \n"
          "want to proceed?")
    time.sleep(2)
    print("1. I want to turn left.")
    time.sleep(2)
    print("2. I want to head straight.")
    time.sleep(2)
    print("3. I'm right handed so might as well go that way.")
    time.sleep(2)
    choice = input("\nMake your choice:")
    if(choice == 1):
        print("You take the left path and continue onwards for what seems like an eternity. Suddenly, you find yourself \n"
              "at the edge of a steep cliff! Good thing you have okay reflexes, or you would've fallen into the chasm. \n"
              "Let's head back and choose another path.")
        time.sleep(5)
        print("2. Go center.")
        time.sleep(2)
        print("3. Go right.")
        time.sleep(1)
        choice2 = input("\nMake another decision:")
        if(choice2 == 2):
            print("You press straight on for quite some time when all of a sudden, you hear the howls of wolves in the \n"
                  "distance. That's a good sign to stay away, so let's head back to the fork and go right.")
            time.sleep(5)
            cave()
        else:
            cave()
    elif(choice == 2):
        print("You press straight on for quite some time when all of a sudden, you hear the howls of wolves in the \n"
              "distance. That's a good sign to stay away, so let's head back to the fork in the road.")
        time.sleep(5)
        print("1. Go left")
        time.sleep(2)
        print("3. Go right")
        time.sleep(2)
        choice3 = input("\nMake another decision:")
        if(choice3 == 1):
            print("You take the left path and continue onwards for what seems like an eternity. Suddenly, you find \n"
                  "yourself at the edge of a steep cliff! Good thing you have okay reflexes, or you would've fallen into \n"
                  " the chasm. Let's head back and take the right path.")
            time.sleep(5)
            cave()
        else:
            cave()
    else:
        cave()


main()
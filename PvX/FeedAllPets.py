# Author: TheDroidUrLookingFor

from System import Array

# Script variables configuration
MeatGraphic = 0x9f1
VegGraphic = 0xc78
# Pet List
pets = []
pets.Add(0x0000000) # Pet One
pets.Add(0x0000000) # Pet Two

#Heal Pets
def feed_pets():
    for curpet in pets:
        if InRange(curpet, 1):
            if Graphic(curpet) == 0x115:
                Feed(curpet, VegGraphic)
                HeadMsg('Feed: ' + Name(curpet), curpet)
                Pause(750)
            else:
            	HeadMsg('Feed: ' + Name(curpet), curpet)
                Feed(curpet, MeatGraphic)
                Pause(750)


feed_pets()
HeadMsg('Done feeding all pets in the list!', 1998)
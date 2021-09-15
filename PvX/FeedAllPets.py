# Author: TheDroidUrLookingFor

from System import Array

# Script variables configuration
if not ListExists('Pet'):
	PlayMacro("Buddy & Pets")
# Pet List
pets = []
if ListExists('Pet'):
	for j in GetList('Pet'):
		if FindObject(j, 30):
			pets.Add(j)

#Heal Pets
def feed_pets():
    for curpet in pets:
        if InRange(curpet, 1):
            if Graphic(curpet) == 0x115:
                Feed(curpet, 0xc78)
                HeadMsg('Feeding: ' + Name(curpet), curpet)
                Pause(750)
            else:
            	HeadMsg('Feeding: ' + Name(curpet), curpet)
                Feed(curpet, 0x9f1)
                Pause(750)


feed_pets()
HeadMsg('Done feeding all pets in the list!', 1998)
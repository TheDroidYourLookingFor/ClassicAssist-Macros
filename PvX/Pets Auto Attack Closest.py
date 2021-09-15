# Author: TheDroidUrLookingFor

from System import Array

# Script variables configuration
# Pet List
pets = []
if ListExists('Pet'):
	for j in GetList('Pet'):
		if FindObject(j, 30):
			pets.Add(j)

# Send pets to attack
def pets_attack():
	for curpet in pets:
		if FindObject(curpet, 20) and not War(curpet):
			pet_enemy = GetEnemy(['Murderer', 'Enemy', 'criminal', 'gray'], 'Any', 'Closest')
			SetEnemy(pet_enemy)
			WaitForContext(curpet, 134, 5000)
			Pause(400)
			Target('enemy')


pets_attack()
Pause(2000)
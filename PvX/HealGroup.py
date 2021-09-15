# Name: Group Heal
# Description: Heal buddies, pets, and self with Magery/bandaids
# Author: TheDroidUrLookingFor
# Era: Any

from Assistant import Engine
from System import Array

if not ListExists('Buddy'):
	PlayMacro("Buddy & Pets")

if not ListExists('Pet'):
	PlayMacro("Buddy & Pets")
#
# Script variables configuration
#
# Buddy List
buddies = []
if ListExists("Buddy"):
	for i in GetList("Buddy"):
		if FindObject(i, 30):
			buddies.Add(i)
# Pet List
pets = []
if ListExists('Pet'):
	for j in GetList('Pet'):
		if FindObject(j, 30):
			pets.Add(j)
# Range
BandAidRange = 2
HealRange = 8
# Extra delay
ping = 400
# Delay Reduction
faster_cast_recovery = 6
# Self
SelfHealAtPct = 5
HealSelf = True
BandAidSelf = False
# Buddy
BuddyHealAtPct = 5
HealBuddy = True
BandAidBuddy = False
# Pet
PetHealAtPct = 5
HealPet = True
BandAidPet = False
# Delays
wait_for_target_milliseconds = 2000
wait_after_bandaid = 1000
bandage_reuse_time = 3250
#
# Stop Editing
#
Last_Bandage_Target = ''


class SpellInfo:

    def __init__(self, name, mana_cost, min_skill, delay_in_ms):
        self.name = name
        self.mana_cost = mana_cost
        self.min_skill = min_skill
        self.delay_in_ms = delay_in_ms


# Set mana and spell cast according to your stats
spells = [
    SpellInfo('Cure', 6, 0, 750),
    SpellInfo('Heal', 4, 0, 500),
    SpellInfo('Greater Heal', 11, 24, 1260),
]


def create_timer(timer_name):
	if not TimerExists(timer_name):
		CreateTimer(timer_name)


def setup_bandage_timers():
	for i in buddies:
		if FindObject(i, 30):
			create_timer(Name(i))
	for j in pets:
		if FindObject(j, 30):
			create_timer(Name(j))


def bandage_target(bandagetarget, healpct):
	global BandAidRange
	
	if DiffHitsPercent(bandagetarget) >= healpct and InRange(bandagetarget, BandAidRange):
		if Timer(Name(bandagetarget)) >= bandage_reuse_time:
			if InRange(bandagetarget, BandAidRange):
				if FindType(0xe21, -1, "backpack"):
					HeadMsg("Bandage: " + Name(bandagetarget), bandagetarget)
					UseType(0xe21, -1, "backpack")
					WaitForTarget(2000)
					Target(bandagetarget)
					SetTimer(Name(bandagetarget), 0)


def mage_heal(healtarget, healat, usebandaid):
	global BandAidRange
	global HealRange
	global ping
	global faster_cast_recovery
	
	if not Dead(healtarget):
		while Poisoned(healtarget) and InRange(healtarget, HealRange):
			HeadMsg(">> " + spells[0].name + " <<", healtarget)
			Cast(spells[0].name)
			WaitForTargetOrFizzle(wait_for_target_milliseconds)
			Target(healtarget)
			Pause((spells[0].delay_in_ms + ping) - (faster_cast_recovery * 100))
		
		if DiffHitsPercent(healtarget) >= healat and InRange(healtarget, HealRange):
			if BuffExists('Protection'):
				HeadMsg(">> " + spells[2].name + " <<", healtarget)
				Cast(spells[2].name)
				WaitForTargetOrFizzle(wait_for_target_milliseconds)
				Target(healtarget)
				Pause((spells[2].delay_in_ms + ping) - (faster_cast_recovery * 100))
			else:
				HeadMsg(">> " + spells[1].name + " <<", healtarget)
				Cast(spells[1].name)
				WaitForTargetOrFizzle(wait_for_target_milliseconds)
				Target(healtarget)
				Pause((spells[1].delay_in_ms + ping) - (faster_cast_recovery * 25))
				
			if usebandaid and InRange(healtarget, BandAidRange):
				bandage_target(healtarget, healat)

#Heal Self
def check_self_hp():
	mage_heal('self', SelfHealAtPct, BandAidSelf)


#Heal Pets
def check_pets():
	for curpet in pets:
		mage_heal(curpet, PetHealAtPct, BandAidPet)


#Heal Buddies
def check_buddies():
    for curbuddy in buddies:
		mage_heal(curbuddy, BuddyHealAtPct, BandAidBuddy)


def heal_check():
	if HealSelf:
		check_self_hp()
	if HealBuddy:
		check_buddies()
	if HealPet:
		check_pets()

setup_bandage_timers()
while True:
	heal_check()
	Pause(50)

from Assistant import Engine
from System import Array

if not FindAlias('Salvage Bag') or not FindObject('Salvage Bag'):
  HeadMsg('Select your salvage bag.')
  PromptAlias('Salvage Bag')

if not FindAlias('Storage Container') or not FindObject('Storage Container'):
  HeadMsg('Select your Storage Container.')
  PromptAlias('Storage Container')

ping = 800
CreateAmount = 20
CurrentTinkerKit = ''
SalvageItems = []


class TinkerRecipeInfo:

    def __init__(self, name, min_skill, gump1, gump2, item_type):
        self.name = name
        self.min_skill = min_skill
        self.gump1 = gump1
        self.gump2 = gump2
        self.item_type = item_type


TinkerRecipes = [
    TinkerRecipeInfo('Scissors', 40, 9003, 8, 0xf9e),
    TinkerRecipeInfo('Tongs', 45, 9003, 25, 0xfbc),
    TinkerRecipeInfo('Lockpick', 60, 9003, 25, 0x14fb),
    TinkerRecipeInfo('Bracelet', 75, 9002, 1, 0x1086),
    TinkerRecipeInfo('Spyglass', 85, 9006, 56, 0x14f5),
    TinkerRecipeInfo('Ring', 90, 9002, 2, 0x2798),
]


for tinkerrecipe in TinkerRecipes:
	if tinkerrecipe.item_type not in SalvageItems:
		SalvageItems.Add(tinkerrecipe.item_type)
                
def SalvageAllItems():
	while FindType(0x14fb, -1, 'backpack'):
		MoveType(0x14fb, 'backpack', 'Storage Container')
		Pause(1000)

	for i in SalvageItems:
		while FindType(i, 0, 'backpack'):
			MoveItem('found', 'Salvage Bag')
			Pause(1000)


def CheckTinkerSupplies():
	if CountType(0x1bf2, 'backpack') <= 1000:
		if FindType(0x1bf2, -1, 'Storage Container'):
			MoveItem('found', 'backpack', 250)
			Pause(1000)


def CreateTinkerItem(amount, page, itemnum):
    global CurrentTinkerKit

    for i in range(amount):
        if FindType(0x1eb9, -1, 'backpack') and FindObject(CurrentTinkerKit, -1, 'backpack'):
            if not GumpExists(0x1cc) and FindObject(CurrentTinkerKit, -1, 'backpack'):
                UseObject(CurrentTinkerKit)
                Pause(250)
            else:
                CreateTinkersTools()
                UseObject(CurrentTinkerKit)
                Pause(250)

            ReplyGump(0x1cc, page)
            WaitForGump(0x1cc, 5000)
            ReplyGump(0x1cc, itemnum)
            WaitForGump(0x1cc, 5000)
            Pause(1000)
            UnsetAlias('found')

    if GumpExists(0x1cc):
        ReplyGump(0x1cc, 0)
        Pause(250)


def CreateTinkersTools():
	global CurrentTinkerKit

	if not FindType(0x1eb9, -1, 'backpack'):
		HeadMsg('Creating Tinkers Tools', 'self')
		UseObject('found')
		Pause(250)
		ReplyGump(0x1cc, 11)
		WaitForGump(0x1cc, 2000)
		ReplyGump(0x1cc, 0)
		Pause(1000)
	
	if FindType(0x1eb9, -1, "backpack") and not FindObject(CurrentTinkerKit, -1, 'backpack'):
		CurrentTinkerKit = 'found'
		UnsetAlias('found')


def StartTraining():
	global CreateAmount
	
	while Skill('Tinkering') < SkillCap('Tinkering'):
		CheckTinkerSupplies()
		CreateTinkersTools()
		SalvageAllItems()
	
		current_recipe = None
		for tinkerrecipe in TinkerRecipes:
			if tinkerrecipe.min_skill <= Skill('Tinkering'):
				current_recipe = tinkerrecipe
	
		if Skill('Tinkering') < 30:
			HeadMsg('Buy more skill!')
			Stop()
		else:
			CreateTinkerItem(CreateAmount, current_recipe.gump1, current_recipe.gump2)
			Pause(250)


StartTraining()

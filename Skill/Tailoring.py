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
CurrentSewingKit = ''
SalvageItems = []


class TailorRecipeInfo:

    def __init__(self, name, min_skill, gump1, gump2, item_type):
        self.name = name
        self.min_skill = min_skill
        self.gump1 = gump1
        self.gump2 = gump2
        self.item_type = item_type


TailorRecipes = [
    TailorRecipeInfo('Short Pants', 29, 9003, 37, 0x152e),
    TailorRecipeInfo('Fur cape', 35, 9003, 28, 0x2309),
    TailorRecipeInfo('Cloaks', 41.4, 9003, 25, 0x1515),
    TailorRecipeInfo('Fur Boots', 50, 9005, 601, 0x2307),
    TailorRecipeInfo('Robes', 53.9, 9003, 26, 0x1f03),
    TailorRecipeInfo('Kasa', 60, 9002, 17, 0x2798),
    TailorRecipeInfo('Ninja Tabi', 70, 9005, 602, 0x2797),
    TailorRecipeInfo('Oil Cloths', 76, 9004, 500, 0x175d),
    TailorRecipeInfo('Elven Shirt', 85, 9003, 70, 0x3175),
    TailorRecipeInfo('Gargish Cloth Arms', 100, 9007, 200, 0x405f),
    TailorRecipeInfo('Gargish Cloth Leggings', 105, 9007, 202, 0x4065),
    TailorRecipeInfo('Gargish Cloth Chest', 110, 9007, 201, 0x4061),
]


for tailorrecipe in TailorRecipes:
	if tailorrecipe.item_type not in SalvageItems:
		SalvageItems.Add(tailorrecipe.item_type)
                
def SalvageAllItems():
    for i in SalvageItems:
        while FindType(i, 0, 'backpack'):
            MoveItem('found', 'Salvage Bag')
            Pause(1000)

	if Contents('Salvage Bag') >= 1:
		WaitForContext('Salvage Bag', 912, 5000)
		Pause(250)

	if FindType(0xe21, -1, 'backpack'):
		MoveType(0xe21, 'backpack', 'Storage Container')
		Pause(1000)


def CheckTailorSupplies():
	if CountType(0x1766, 'backpack') <= 200:
		if FindType(0x1766, -1, 'Storage Container'):
			MoveItem('found', 'backpack', 1500)
			Pause(1000)
	
	if CountType(0x1bf2, 'backpack') <= 20:
		if FindType(0x1bf2, -1, 'Storage Container'):
			MoveItem('found', 'backpack', 100)
			Pause(1000)


def CreateTailorItem(amount, page, itemnum):
    global CurrentSewingKit

    for i in range(amount):
        if FindType(0xf9d, -1, 'backpack') and FindObject(CurrentSewingKit, -1, 'backpack'):
            if not GumpExists(0x1cc) and FindObject(CurrentSewingKit, -1, 'backpack'):
                UseObject(CurrentSewingKit)
                Pause(250)
            else:
                CreateSewingKit()
                UseObject(CurrentSewingKit)
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


def CreateSewingKit():
    global CurrentSewingKit

    if not FindType(0xf9d, -1, "backpack"):
        if FindType(0x1eb9, -1, 'backpack'):
            HeadMsg('Creating Sewing Kit', 'self')
            UseObject('found')
            Pause(250)
            ReplyGump(0x1cc, 14)
            WaitForGump(0x1cc, 2000)
            ReplyGump(0x1cc, 0)
            Pause(1000)
            UnsetAlias('found')
        else:
            HeadMsg('Out of Tinkers Tools', 'self')
            Stop()

    if FindType(0xf9d, -1, "backpack") and not FindObject(CurrentSewingKit, -1, 'backpack'):
        SetAlias(CurrentSewingKit, 'found')
        UnsetAlias('found')


def CreateTinkersTools():
    if FindType(0x1eb9, -1, 'backpack'):
        HeadMsg('Creating Tinkers Tools', 'self')
        UseObject('found')
        Pause(250)
        ReplyGump(0x1cc, 11)
        WaitForGump(0x1cc, 2000)
        ReplyGump(0x1cc, 0)
        Pause(1000)
    else:
        HeadMsg('Out of Tinkers Tools', 'self')
        Stop()


def StartTraining():
	global CreateAmount
	
	while Skill('Tailoring') < SkillCap('Tailoring'):
		CheckTailorSupplies()
		CreateSewingKit()
		SalvageAllItems()
	
		current_recipe = None
		for tailorrecipe in TailorRecipes:
			if tailorrecipe.min_skill <= Skill('Tailoring'):
				current_recipe = tailorrecipe
	
		if Skill('Tailoring') < 30:
			HeadMsg('Buy more skill!')
			Stop()
		else:
			CreateTailorItem(CreateAmount, current_recipe.gump1, current_recipe.gump2)
			Pause(250)


StartTraining()

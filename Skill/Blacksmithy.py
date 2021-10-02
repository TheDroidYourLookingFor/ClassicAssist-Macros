from Assistant import Engine
from System import Array

ping = 800
CurrentTongs = ''
SmeltItems = []


class BSRecipeInfo:

    def __init__(self, name, min_skill, gump1, gump2, item_type):
        self.name = name
        self.min_skill = min_skill
        self.gump1 = gump1
        self.gump2 = gump2
        self.item_type = item_type


BSRecipes = [
    BSRecipeInfo('Mace', 40, 9007, 77, 0xf5c),
    BSRecipeInfo('Maul', 45, 9007, 78, 0x143b),
    BSRecipeInfo('Cutlass', 50, 9004, 44, 0x1441),
    BSRecipeInfo('Katana', 55, 9004, 46, 0x13ff),
    BSRecipeInfo('Scimitar', 59.5, 9004, 49, 0x13b6),
    BSRecipeInfo('Circlet', 90, 9010, 104, 0x2b6e),
    BSRecipeInfo('Boomerang', 100.1, 9009, 208, 0x4067),
]


for smeltitem in BSRecipes:
	if smeltitem.item_type not in SmeltItems:
		SmeltItems.Add(smeltitem.item_type)
                
def SmeltAllItems():
    global CurrentTongs
    
    for i in SmeltItems:
        while FindType(i, -1, 'backpack'):
            if not GumpExists(0x1cc) and FindObject(CurrentTongs, -1, 'backpack'):
                UseObject(CurrentTongs)
                Pause(250)
            else:
                CreateTongs()
                UseObject(CurrentTongs)
                Pause(250)

            if FindType(i, -1, 'backpack'):
                ReplyGump(0x1cc, 7000)
                WaitForTarget(5000)
                Target('found')
                WaitForGump(0x1cc, 5000)
                Pause(250)

    if GumpExists(0x1cc):
        ReplyGump(0x1cc, 0)
        Pause(250)


def CreateBlackSmithItem(amount, page, itemnum):
    global CurrentTongs

    for i in range(amount):
        if FindType(0xfbc, -1, 'backpack') and FindObject(CurrentTongs, -1, 'backpack'):
            if not GumpExists(0x1cc) and FindObject(CurrentTongs, -1, 'backpack'):
                UseObject(CurrentTongs)
                Pause(250)
            else:
                CreateTongs()
                UseObject(CurrentTongs)
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


def CreateTongs():
    global CurrentTongs

    if not FindType(0xfbc, -1, "backpack"):
        if FindType(0x1eb9, -1, 'backpack'):
            HeadMsg('Creating Tongs', 'self')
            UseObject('found')
            Pause(250)
            ReplyGump(0x1cc, 20)
            WaitForGump(0x1cc, 2000)
            ReplyGump(0x1cc, 0)
            Pause(1000)
            UnsetAlias('found')
        else:
            HeadMsg('Out of Tinkers Tools', 'self')
            Stop()

    if FindType(0xfbc, -1, "backpack") and not FindObject(CurrentTongs, -1, 'backpack'):
        SetAlias(CurrentTongs, 'found')
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
    while Skill('Blacksmithy') < SkillCap('Blacksmithy'):
        CreateTongs()
        SmeltAllItems()

        current_recipe = None
        for bsrecipe in BSRecipes:
            if bsrecipe.min_skill <= Skill('Blacksmithy'):
                current_recipe = bsrecipe

        if Skill('Blacksmithy') < 30:
            HeadMsg('Buy more skill!')
            Stop()
        else:
            CreateBlackSmithItem(10, current_recipe.gump1, current_recipe.gump2)

        Pause(1000)


SmeltAllItems()
StartTraining()

# Name: Group Heal
# Description: Heal buddies, pets, and self with Magery.
# Author: TheDroidUrLookingFor
# Era: Any

from Assistant import Engine
from System import Array

if not FindAlias('Loot Bag'):
    PromptAlias('Loot Bag')

# Script variables configuration
Look_For_Single_Skill = True
Look_For_Double_Skill = True
Auto_Select_Corpse = False
#
min_skill_first = 10
min_skill_second = 10
ping = 400
faster_cast_recovery = 6
wait_for_target_milliseconds = 2000
Current_Jewel = ''

# Jewelry Type List
Jewelry = []
Jewelry.Add(0x108a)
Jewelry.Add(0x1f09)
Jewelry.Add(0x1086)
Jewelry.Add(0x1f06)

# Pet List
JewelSkill = []
JewelSkill.Add('Animal Taming')
JewelSkill.Add('Animal Lore')
JewelSkill.Add('Veterinary')
JewelSkill.Add('Provocation')
JewelSkill.Add('Anatomy')
JewelSkill.Add('Archery')
JewelSkill.Add('Stealing')
JewelSkill.Add('Tactics')
JewelSkill.Add('Swordsmanship')
JewelSkill.Add('Fencing')
JewelSkill.Add('Ninjitsu')
JewelSkill.Add('Healing')
JewelSkill.Add('Focus')
JewelSkill.Add('Mace Fighting')
JewelSkill.Add('Magery')
JewelSkill.Add('Evaluating Intelligence')
JewelSkill.Add('Resisting Spells')
JewelSkill.Add('Spirit Speak')
JewelSkill.Add('Necromancy')
JewelSkill.Add('Parrying')
JewelSkill.Add('Bushido')
JewelSkill.Add('Peacemaking')
JewelSkill.Add('Discordance')
JewelSkill.Add('Provocation')


def Skin_Corpse():
    if not FindType(0xec4, -1, 'backpack'):
        SysMessage('*****No dagger*****', 25)
        Stop()
    else:
        if FindType(0xec4, -1, 'backpack'):
            UseObject('found')
            WaitForTarget(5000)
            Target('curcorpse')


def Do_Loot():
    global Look_For_Second_Skill
    global Look_For_Double_Skills

    if Look_For_Double_Skill:
        Look_For_Double()
    if Look_For_Single_Skill:
        Look_For_Single()


def Find_Corpse_To_Loot():
    if not FindType(0x2006, -1, 'ground'):
        HeadMsg('No corpses nearby', 'self')
        Stop()
    else:
        SetAlias('curcorpse', 'found')


def Select_Corpse_To_Loot():
    PromptAlias('curcorpse')
    Pause(250)


def Look_For_Single():
    global Current_Jewel

    for i in Jewelry:
        if FindType(i, -1, 'curcorpse'):
            WaitForProperties('found', 600)
            for j in JewelSkill:
                if Property('found', j) >= min_skill_first:
                    HeadMsg('Moving Jewel to Loot Bag', 1999)
                    MoveItem('found', 'loot bag')
                    Pause(1000)


def Look_For_Double():
    global Current_Jewel

    for i in Jewelry:
        if FindType(i, -1, 'curcorpse'):
            WaitForProperties('found', 600)
            for j in JewelSkill:
                if Property('found', j) >= min_skill_first:
                    for h in JewelSkill:
                        if Property('found', h) >= min_skill_second:
                            HeadMsg('Moving Jewel to Loot Bag', 1999)
                            MoveItem('found', 'loot bag')
                            Pause(1000)


UnsetAlias('curcorpse')
if Auto_Select_Corpse:
    Find_Corpse_To_Loot()
else:
    Select_Corpse_To_Loot()

Skin_Corpse()
Pause(1000)
UseObject('curcorpse')
Pause(1000)
Do_Loot()
#IgnoreObject('curcorpse')
SysMessage('Corpse Now Ignored', 25)

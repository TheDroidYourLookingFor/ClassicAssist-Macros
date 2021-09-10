# Name: Heal pet target
# Description: Auto bandage pets
# Author: TheDroidUrLookinFor
# Era: Any
# Date: Sat Sept 04 2021

#// removes pets if mounted, stabled or you get too far away
if not FindAlias("PetHealTarget") or not FindObject("PetHealTarget", 30):
    UnsetAlias("PetHealTarget")
    HeadMsg("Cleared PetHealTarget", "self", 33)

#// check if player dead
if Dead("self"):
    Stop()

if not FindType(0xe21, -1, "backpack"):
    HeadMsg("Out of Bandages", "self", 33)
    Stop()

#// Select timer timeout
if not TimerExists("SelectTimer"):
    CreateTimer("SelectTimer")

if not FindAlias("PetHealTarget"):
    HeadMsg("Select First Pet", "self", 33)
    PromptAlias("PetHealTarget")
    SetTimer("SelectTimer", 0)
    while WaitingForTarget() and Timer("SelectTimer") < 9999:
        Pause(100)

    if ((GetAlias("PetHealTarget") == GetAlias("self")) or (GetAlias("PetHealTarget") == False)):
        UnsetAlias("PetHealTarget")
        HeadMsg("No Valid Target", "self", 33)
        Stop()

if not FindObject(GetAlias("PetHealTarget")):
    HeadMsg("No PetHealTarget Found", "self", 33)
    Stop()

if Hits("PetHealTarget") > (MaxHits("PetHealTarget") - 5):
    Stop()

if Hits("PetHealTarget") != MaxHits("PetHealTarget"):
    if not InRange("PetHealTarget", 2):
        HeadMsg("Move closer to target!", "PetHealTarget", 33)
        Pause(500)
    else:
        while Poisoned('PetHealTarget'):
            Cast('Cure')
            WaitForTarget(2000)
            Target("PetHealTarget")
            Pause(1350)

        if BuffExists('Protection'):
            Cast('Greater Heal')
            WaitForTargetOrFizzle(5000)

        if not BuffExists('Protection'):
            Cast('Heal')
            WaitForTargetOrFizzle(5000)

        Target("PetHealTarget")
        UseType(0xe21, -1, "backpack")
        WaitForTarget(2000)
        Target("PetHealTarget")
        HeadMsg("Healing: " + Name("PetHealTarget"), "self", 33)
        Pause(1350)
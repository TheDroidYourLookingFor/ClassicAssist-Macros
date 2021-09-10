# Name: Blacksmithy training to cap
# Description: Train Blacksmithy to cap
# Author: TheDroidUrLookin4
# Era: Any

Blacksmithy_cap = SkillCap('Blacksmithy')
ping = 800


class ItemInfo:

    def __init__(self, name, min_skill, gump1, gump2, item_type):
        self.name = name
        self.min_skill = min_skill
        self.gump1 = gump1
        self.gump2 = gump2
        self.item_type = item_type
        self.target = target


if Skill('Blacksmithy') < 35:
    HeadMsg('Buy more skill!')
    Stop()

if FindType(0x13e3, 0, 'backpack'):
    SetAlias('Hammer', 'found')
    UnsetAlias('found')
else:
    HeadMsg("Need a Smith Hammer")
    Stop()

while Skill('Blacksmithy') < Blacksmithy_cap:
    # Set according to your server stats
    items = [
        KegInfo('Cutlas', 43, 43, 9, 0x1441),
        KegInfo('Scimitar', 47, 43, 44, 0x13b6),
        KegInfo('Kryss', 52, 43, 30, 0x1401),
        KegInfo('Katana', 60, 43, 23, 0x13ff),
        KegInfo('Short Spear', 95, 57, 16, 0x1403),
        KegInfo('Plate Gorget', 100, 22, 16, 0x1413),
    ]

    current_item = None

    for item in items:
        if item.min_skill <= Skill('Blacksmithy'):
            current_item = item

    if FindType(0x13e3, 0, 'backpack'):
        UnsetAlias('found')
        ReplyGump(0x38920abd, current_item.gump1)
        WaitForGump(0x38920abd, 15000)
        ReplyGump(0x38920abd, current_item.gump2)
        WaitForGump(0x38920abd, 2000)
    else:
        HeadMsg("Need a Smith Hammer")
        Stop()

    if FindType(current_item.item_type, 0x0, 'backpack'):
        ReplyGump(0x38920abd, 14)
        WaitForTarget(15000)
        Target('found')
        WaitForGump(0x38920abd, 15000)

    if Skill('Blacksmithy') == Blacksmithy_cap:
        HeadMsg('Blacksmithy complete!')
        Stop()

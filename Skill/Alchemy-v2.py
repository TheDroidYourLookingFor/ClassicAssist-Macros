# Name: Alchemy training to cap
# Description: Train Alchemy to cap
# Author: TheDroidUrLookin4
# Era: Any

alchemy_cap = SkillCap('Alchemy')
ping = 800


class KegInfo:

    def __init__(self, name, min_skill, gump1, gump2, keg_type, target=None):
        self.name = name
        self.min_skill = min_skill
        self.gump1 = gump1
        self.gump2 = gump2
        self.keg_type = keg_type
        self.target = target


if Skill('alchemy') < 30:
    HeadMsg('Buy more skill!')
    Stop()

while Skill('Alchemy') < alchemy_cap:
    if Skill('alchemy') < 60 and not FindObject('TR'):
        HeadMsg('Select Total Refresh Keg')
        PromptAlias('TR')

    if Skill('alchemy') < 70 and not FindObject('GA'):
        HeadMsg('Select Greater Agility Keg')
        PromptAlias('GA')

    if Skill('alchemy') < 80 and not FindObject('GS'):
        HeadMsg('Select Greater Strength Keg')
        PromptAlias('GS')

    if Skill('alchemy') < 90 and not FindObject('GH'):
        HeadMsg('Select Greater Heal Keg')
        PromptAlias('GH')

    if Skill('alchemy') < 100 and not FindObject('GC'):
        HeadMsg('Select Greater Cure Keg')
        PromptAlias('GC')

    # Set according to your server stats
    kegs = [
        KegInfo('Total Refresh Keg', 60, 1, 9, 0xf0b, TR),
        KegInfo('Greater Agility Keg', 70, 8, 9, 0xf08, GA),
        KegInfo('Greater Strength Keg', 80, 29, 9, 0xf09, GS),
        KegInfo('Greater Heal Keg', 90, 22, 16, 0xf0c, GH),
        KegInfo('Greater Cure Keg', 100, 43, 16, 0xf07, GC),
    ]

    current_keg = None

    for keg in kegs:
        if keg.min_skill <= Skill('Alchemy'):
            current_keg = keg

    if UseType(0xe9b, 0x0, 'backpack'):
        WaitForGump(0x38920abd, 15000)
        ReplyGump(0x38920abd, current_keg.gump1)
        WaitForGump(0x38920abd, 15000)
        ReplyGump(0x38920abd, current_keg.gump2)
        WaitForGump(0x38920abd, 2000)

        if FindType(current_keg.keg_type, 0x0, 'backpack'):
            MoveItem('found', 'current_keg.target')
            Pause(600)

    if Skill('Alchemy') == alchemy_cap:
        HeadMsg('Alchemy complete!')
        Stop()

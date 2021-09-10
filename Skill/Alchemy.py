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

if Skill('alchemy') < 30:
    HeadMsg('Buy more skill!')
    Stop()

elif Skill('alchemy') < 60:
    if UseType(0xe9b, 0x0, 'backpack'):
        WaitForGump(0x38920abd, 15000)
        ReplyGump(0x38920abd, 1)
        WaitForGump(0x38920abd, 15000)
        ReplyGump(0x38920abd, 9)
        WaitForGump(0x38920abd, 2000)

    if FindType(0xf0b, 0x0, 'backpack'):
        MoveItem('found', 'TR')
        Pause(600)

elif Skill('alchemy' < 70):
    if UseType(0xe9b, 0x0, 'backpack'):
        WaitForGump(0x38920abd, 15000)
        ReplyGump(0x38920abd, 8)
        WaitForGump(0x38920abd, 15000)
        ReplyGump(0x38920abd, 9)
        WaitForGump(0x38920abd, 2000)

    if FindType(0xf08, 0x0, 'backpack'):
        MoveItem('found', 'GA')
        Pause(600)

elif Skill('alchemy' < 80):
    if UseType(0xe9b, 0x0, 'backpack'):
        WaitForGump(0x38920abd, 15000)
        ReplyGump(0x38920abd, 29)
        WaitForGump(0x38920abd, 15000)
        ReplyGump(0x38920abd, 9)
        WaitForGump(0x38920abd, 2000)

    if FindType(0xf09, 0x0, 'backpack'):
        MoveItem('found', 'GS')
        Pause(600)

elif Skill('alchemy' < 90):
    if UseType(0xe9b, 0x0, 'backpack'):
        WaitForGump(0x38920abd, 15000)
        ReplyGump(0x38920abd, 22)
        WaitForGump(0x38920abd, 15000)
        ReplyGump(0x38920abd, 16)
        WaitForGump(0x38920abd, 2000)

    if FindType(0xf0c, 0x0, 'backpack'):
        MoveItem('found', 'GH')
        Pause(600)

elif Skill('alchemy') < 100:
    if UseType(0xe9b, 0x0, 'backpack'):
        WaitForGump(0x38920abd, 15000)
        ReplyGump(0x38920abd, 43)
        WaitForGump(0x38920abd, 15000)
        ReplyGump(0x38920abd, 16)
        WaitForGump(0x38920abd, 2000)

    if FindType(0xf07, 0x0, 'backpack'):
        MoveItem('found', 'GC')
        Pause(600)

else:
    HeadMsg('Alchemy complete!')
    Stop()

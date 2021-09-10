#////////////////////////////////////
#//     Uses a sewing kit. This    //
#//      macro is designed for     //
#//   training tailoring from 30.  //
#//                                //
#//  Turn on loop and click play!  //
#//                                //
#//      ~~Made by kdivers~~       //
#////////////////////////////////////
if Skill('Tailoring') < 30:
    HeadMsg("Buy Skill(from an NPC!")
    Stop()
elif Skill('Tailoring') < 41.4:
    if UseType(0xf9d, 0x0, 'backpack'):
        ReplyGump(0x38920abd, 15)
        WaitForGump(0x38920abd, 15000)
        ReplyGump(0x38920abd, 2)
        WaitForGump(0x38920abd, 15000)
        Pause(2000)
        if UseType(0xf9f, 0x0, 'backpack'):
            WaitForTarget(2000)
            TargetType(0x152e, 0x0, 'backpack')

elif Skill('Tailoring') < 54:
    if UseType(0xf9d, 0x0, 'backpack'):
        WaitForGump(0x38920abd, 15000)
        ReplyGump(0x38920abd, 8)
        WaitForGump(0x38920abd, 15000)
        ReplyGump(0x38920abd, 51)
        Pause(2000)
        if UseType(0xf9f, 0x0, 'backpack'):
            WaitForTarget(2000)
            TargetType(0x1515, 0x0, 'backpack')

elif Skill('Tailoring') < 74.6:
    if UseType(0xf9d, 0x0, 'backpack'):
        WaitForGump(0x38920abd, 15000)
        ReplyGump(0x38920abd, 8)
        WaitForGump(0x38920abd, 15000)
        ReplyGump(0x38920abd, 58)
        Pause(2000)
        if UseType(0xf9f, 0x0, 'backpack'):
            WaitForTarget(2000)
            TargetType(0x1f03, 0x0, 'backpack')

elif Skill('Tailoring') < 99:
    if UseType(0xf9d, 0x0, 'backpack'):
        WaitForGump(0x38920abd, 15000)
        ReplyGump(0x38920abd, 22)
        WaitForGump(0x38920abd, 15000)
        ReplyGump(0x38920abd, 23)
        Pause(2000)
        if DiffWeight() < 20:
            if UseType(0xf9f, 0x0, 'backpack'):
                WaitForTarget(2000)
                TargetType(0x175d, 0x7d1, 'backpack')

elif Skill('tailoring') < 100:
    if UseType(0xf9d, 0x0, 'backpack'):
        WaitForGump(0x38920abd, 15000)
        ReplyGump(0x38920abd, 43)
        WaitForGump(0x38920abd, 15000)
        ReplyGump(0x38920abd, 300)
        Pause(2000)
        if UseType(0xf9f, 0x0, 'backpack'):
            WaitForTarget(2000)
            TargetType(0x13db, 0x0, 'backpack')

else:
    HeadMsg('Tailoring complete!')
    Stop()

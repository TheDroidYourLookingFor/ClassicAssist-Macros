#////////////////////////////////////
#//   This macro is designed for   //
#//  training carpentry from 30.   //
#// It uses standard saws. Due to  //
#//  the weight of boards, it is   //
#// written to be used in a house  //
#// with a chest to restock from.  //
#//                                //
#//   Warning: Throws away deeds!  //
#//           Bank them!           //
#//                                //
#//  Turn on loop and click play!  //
#//                                //
#//      ~~Made by kdivers~~       //
#////////////////////////////////////
carpjunk = [0x13b4, 0x14f0, 0xb4a, 0xe89, 0x13f8]

if not FindType(0x1034, 0x0, 'backpack'):
    HeadMsg('Get more saws!')
    Stop()

if not FindObject('trash'):
    HeadMsg('Select your trash barrel')
    PromptAlias('trash')

if not FindObject('restock'):
    HeadMsg('Select the container with your boards')
    PromptAlias('restock')
    UseObject('restock')

if CountType(0x1bd7, 'backpack', 0x0) < 20:
    MoveType(0x1bd7, 'restock', 'backpack', 65, 68, 0, 0x0, 200)
    Pause(1000)
    
if Contents('backpack') > 20 or DiffWeight() < 20:
    Organizer("CarpTrain")
    
if Skill('carpentry') < 30:
    HeadMsg('Buy more skill!')
    Stop()
elif Skill('carpentry') < 40:
    if UseType(0x1034, 0x0, 'backpack'):
        ReplyGump(0x38920abd, 22)
        WaitForGump(0x38920abd, 15000)
        ReplyGump(0x38920abd, 30)
        WaitForGump(0x38920abd, 15000)

elif Skill('carpentry') < 50:
    if UseType(0x1034, 0x0, 'backpack'):
        WaitForGump(0x38920abd, 15000)
        ReplyGump(0x38920abd, 15)
        WaitForGump(0x38920abd, 15000)
        ReplyGump(0x38920abd, 16)
        WaitForGump(0x38920abd, 2000)

elif Skill('carpentry') < 70:
    if UseType(0x1034, 0x0, 'backpack'):
        WaitForGump(0x38920abd, 15000)
        ReplyGump(0x38920abd, 36)
        WaitForGump(0x38920abd, 15000)
        ReplyGump(0x38920abd, 58)
        WaitForGump(0x38920abd, 15000)

elif Skill('carpentry') < 75:
    if UseType(0x1034, 0x0, 'backpack'):
        WaitForGump(0x38920abd, 15000)
        ReplyGump(0x38920abd, 8)
        WaitForGump(0x38920abd, 15000)
        ReplyGump(0x38920abd, 72)
        WaitForGump(0x38920abd, 20000)

elif Skill('carpentry') < 90:
    if UseType(0x1034, 0x0, 'backpack'):
		WaitForGump(0x1cc, 5000)
		ReplyGump(0x1cc, 9004)
		WaitForGump(0x1cc, 5000)
		ReplyGump(0x1cc, 118)
		WaitForGump(0x1cc, 5000)

elif Skill('carpentry') < 96:
	UseType(0x1034, 0x0, 'backpack')
	WaitForGump(0x1cc, 5000)
	ReplyGump(0x1cc, 9004)
	WaitForGump(0x1cc, 5000)
	ReplyGump(0x1cc, 906)
	WaitForGump(0x1cc, 5000)

elif Skill('carpentry') < 120:
	UseType(0x1034, 0x0, 'backpack')
	WaitForGump(0x1cc, 5000)
	ReplyGump(0x1cc, 9004)
	WaitForGump(0x1cc, 5000)
	ReplyGump(0x1cc, 920)
	WaitForGump(0x1cc, 5000)
	
else:
    HeadMsg('Carpentry completed!')
    Stop()
    
if Contents('backpack') > 20 or DiffWeight() < 20:
    Organizer("CarpTrain")

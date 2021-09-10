# Author: Methril
# Description: Automatic Runebook Cloner from a Library.
# You need to insert the names of each rune on the "Names" List. IT will run over and over if a location is blocked untill it makes it passed too the rune.
#===========================================================
HeadMsg('Select book to be cloned.')
#Select runebook to be cloned
if not FindAlias('ToBeCloned'):
  HeadMsg('Select book to be cloned.')
  PromptAlias('ToBeCloned')

#Select a blank book
if not FindAlias('Blank Runebook'):
  HeadMsg('Select blank book to clone to.')
  PromptAlias('Blank Runebook')

#Lists
if not ListExists('Runes'):
  CreateList('Runes')

if List('Runes') == 0:
  PushList('Runes', 5)
  PushList('Runes', 11)
  PushList('Runes', 17)
  PushList('Runes', 23)
  PushList('Runes', 29)
  PushList('Runes', 35)
  PushList('Runes', 41)
  PushList('Runes', 47)
  PushList('Runes', 53)
  PushList('Runes', 59)
  PushList('Runes', 65)
  PushList('Runes', 71)
  PushList('Runes', 83)
  PushList('Runes', 89)
  PushList('Runes', 95)

if not ListExists('Names'):
  CreateList('Names')

if List('Names') == 0:
  PushList('Names', '1')
  PushList('Names', '2')
  PushList('Names', '3')
  PushList('Names', '4')
  PushList('Names', '5')
  PushList('Names', '6')
  PushList('Names', "7")
  PushList('Names', "8")
  PushList('Names', '9')
  PushList('Names', "10")
  PushList('Names', '11')
  PushList('Names', '12')
  PushList('Names', "13")
  PushList('Names', '14')
  PushList('Names', '15')
  PushList('Names', '16')

if not FindType(0x1f14, -1, 'backpack'):
  SysMessage('Out of blank runes!', 25)
  Pause(100)
  PlaySound(984)
  Pause(100)
  PlaySound(987)
  Pause(100)
  PlaySound(988)
  Pause(100)
  MessageBox('Error', '*No Runes restock & restart*')
  Stop()

ClearJournal()

for 0 in 'Runes':
	while not BuffExists('Active Meditation') or not Mana('self') == MaxMana('self'):
		UseSkill('Meditation')
		Pause(4000)
		while Mana('self') < MaxMana('self'):
			Pause(1000)
    
	Pause(1000)
	UseObject('ToBeCloned')
	WaitForGump(0x554b87f3, 15000)
	Pause(900)
	ReplyGump(0x554b87f3, Runes[0])
	Pause(3500)

	if InJournal('blocked') or InJournal('blocking'):
		SysMessage('Ugg the rune is blocked!', '1999')
		PopList('Names', 'front')
		PopList('Runes', 'front')
		ClearJournal()
		Replay()
    
	if not InRegion('town'):
		GetEnemy('murderer', 'Enemy', 'criminal', 'gray', 'closest')
		while FindObject('enemy', 'any', 'ground', 0, 5):
			SetAbility('secondary', 'on')
			Attack('enemy')
			Pause(250)
      
	if FindType(0x1f14, 0, 'backpack', 1, 2):
		AutotargetObject('found')
		Cast('Mark')
		Pause(3500)
		UseObject('found')
		WaitForPrompt(15000)
		PromptMsg(Names[0])
		Pause(2000)
		MoveItem('found', 'Blank Runebook')
		Pause(2000)
		if InJournal('Names[0]', 'system'):
			PopList('Names', 'front')
			PopList('Runes', 'front')
      
	else:
		PlaySound(984)
		Pause(100)
		PlaySound(987)
		Pause(100)
		PlaySound(988)
		Pause(100)
		MessageBox('Error', '*No Runes restock & restart*')
		Stop()
    
	if InJournal("your concentration is disturbed"):
		ClearJournal()
		if not InRegion('town'):
			GetEnemy('murderer', 'Enemy', 'criminal', 'gray', 'closest')
			while FindObject('enemy', 'any', 'ground', 0, 5):
				SetAbility('secondary', 'on')
				Attack('enemy')
				Pause(250)
				
			if FindType(0x1f14, 0, 'backpack', 1, 2):
				AutotargetObject('found')
				Cast('Mark')
				Pause(3500)
				UseObject('found')
				WaitForPrompt(15000)
				PromptMsg(Names[0])
				Pause(2000)
				MoveItem('found', 'Blank Runebook')
				Pause(2000)
				
				if InJournal('Names[0]', 'system'):
					PopList('Names', 'front')
					PopList('Runes', 'front')
		
			else:
				PlaySound(984)
				Pause(100)
				PlaySound(987)
				Pause(100)
				PlaySound(988)
				Pause(100)
				MessageBox('Error', '*No Runes restock & restart*')
				Stop()
			
SysMessage('Book is done being copied!', 1999)
ClearList('Runes')
ClearList('Names')
UnsetAlias('ToBeCloned')
UnsetAlias('Blank Runebook')
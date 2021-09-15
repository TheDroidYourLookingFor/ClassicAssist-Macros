# Change these as needed
# Med at this amount of missing mana
MissingManaMed = 100
Wait_Time = 1500

def check_mana():
	while Mana('self') < MaxMana('self'):
	    while not BuffExists('Active Meditation') and Mana('self') < (MaxMana('self') - MissingManaMed):
	        UseSkill('Meditation')
	        Pause(4000)
        Pause(1000)

if FindType(0xfbf, -1, 'backpack'):
	UseObject('found')
	WaitForGump(0x1cc, 5000)
	
	# Make Recall Scrolls
	while CountType(0x1f4c, 'backpack') < 10:
		check_mana()
		ReplyGump(0x1cc, 32)
		WaitForGump(0x1cc, 5000)
		Pause(500)
	
	# Make Gate Scrolls
	while CountType(0x1f60, 'backpack') < 10:
		check_mana()
		ReplyGump(0x1cc, 52)
		WaitForGump(0x1cc, 5000)
		Pause(500)
		
	loop_amt = range(3)
	for i in loop_amt:
		ReplyGump(0x1cc, 694)
		WaitForGump(0x1cc, 5000)
		Pause(500)
else:
	HeadMsg("Out of scribes pens", 'self')
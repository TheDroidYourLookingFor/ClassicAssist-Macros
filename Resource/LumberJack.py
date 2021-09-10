hand = 'TwoHanded'
logs = [0x1bdd, 0x07da, 0x04a7, 0x04a8, 0x04a9, 0x04aa, 0x047f]  # colors

ClearJournal()

def cut_logs():
    for log in logs:
        while FindType(log, -1, 'backpack'):
            Pause(500)
            UseLayer(hand)
            WaitForTarget(5000)
            Target('found')
            Pause(1000)


def check_hatchet():
    if not FindLayer(hand):
        if FindType(0xf43, -1, 'backpack'):
            EquipItem('found', 2)
            SetAlias("currentaxe", 'found')
        else:
            SysMsg('You have run out of hatchets!', 24)


def chop_logs():
	if FindLayer(hand):
		SetAlias("currentaxe", 'found')
	TargetByResource('currentaxe', 'Wood')
	Pause(3050)


while not InJournal('enough wood'):
    check_hatchet()
    chop_logs()
    cut_logs()
    ClearJournal()

if FindType('0xf39', 'any', 'backpack', 'any', '2'):
  UseType('0xf39', '0' , 'backpack', '1', 1)
elif FindType('0xe86',, 'any', 'backpack', 'any', '2'):
  UseType('0xe86', 'any', 'backpack', 'any', '2')

WaitForTarget(5000)
if Direction() == 0:
  TargetTileOffset(0, -1, 0)
elif Direction() == 1:
  TargetTileOffset(1, -1, 0)
elif Direction() == 2:
  TargetTileOffset(1, 0, 0)
elif Direction() == 3:
  TargetTileOffset(1, 1, 0)
elif Direction() == 4:
  TargetTileOffset(0, 1, 0)
elif Direction() == 5:
  TargetTileOffset(-1, 1, 0)
elif Direction() == 6:
  TargetTileOffset(-1, 0, 0)
elif Direction() == 7:
  TargetTileOffset(-1, -1, 0)
else:
  HeadMsg('No Tools Found!')

Pause(600)
if InJournal('no, metal', 'system'):
  HeadMsg('Time, to, Move')
  Pause(2000)
  ClearJournal()

while Weight() >= 380
  HeadMsg('Time, to, Smelt')
  Pause(1000)

while FindType('0x19b9' 'any' 'backpack' 'any' '2', and, Weight(), >=, 300)
  MoveItem('found', 'mount')
  Pause(600)

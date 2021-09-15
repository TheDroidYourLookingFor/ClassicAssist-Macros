if not TimerExists('curse_weapon'):
  CreateTimer('curse_weapon')

if not InRegion('town'):
	current_enemy = GetEnemy(['Murderer', 'Enemy', 'criminal', 'gray'], 'Any', 'Closest')
	SetEnemy(current_enemy)
	if FindObject('enemy', 'any', 'ground'):
		if Hits('enemy') == MaxHits('enemy'):
			Target('enemy')
			SetAbility('primary', 'on')
			Attack('enemy')
			Virtue('honor')
			Pause(250)

	if Timer('curse_weapon') > 36000:
		Cast('curse_weapon')
		SetTimer('curse_weapon', 0)
	
	SetAbility('primary', 'on')
	Attack('enemy')

Pause(250)
if not TimerExists('curse_weapon'):
  CreateTimer('curse_weapon')

if not InRegion('town'):
  GetEnemy('murderer' 'Enemy' 'criminal' 'gray' 'closest')
  if Hits('enemy') == MaxHits('enemy'):
    Target('enemy')
    SetAbility('secondary', 'on')
    Attack('enemy')
    Virtue('honor')
    Pause(250)
  
  if Timer('curse_weapon' > 36000:)
    Cast('curse_weapon')
    SetTimer('curse_weapon' 0)
  
  SetAbility('secondary', 'on')
  Attack('enemy')

Pause(250)
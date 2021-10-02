if not TimerExists('curse_weapon'):
    CreateTimer('curse_weapon')


def HonorTarget(target):
    if Hits(target) == MaxHits(target):
        InvokeVirtue('Honor')
        WaitForTarget(5000)
        Target(target, 3)
        Pause(1000)


def CurseWeapon():
    if Timer('curse_weapon') > 36000:
        Cast('curse weapon')
        SetTimer('curse_weapon', 0)


def FindATarget():
    current_enemy = GetEnemy(['Murderer', 'Enemy', 'criminal', 'gray'], 'Any',
                             'Closest')
    SetEnemy(current_enemy)


def AttackTarget():
    if FindObject('enemy'):
        if Hits('enemy') == MaxHits('enemy'):
        	HonorTarget('enemy')
            Target('enemy')
            SetAbility('secondary', 'on')
            Attack('enemy')
            Pause(250)


if not InRegion('town', 'self'):
    FindATarget()
    CurseWeapon()
    AttackTarget()

Pause(250)

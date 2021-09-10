# Name: Bandage Self PvM
# Description: Auto Heal self
# Author: TheDroidUrLookingFor
# Era: Any

ping = 250

if Dead("self"):
    Stop()

while Poisoned('self'):
    Cast('Cure', 'self')
    Pause(750 + ping)

if DiffHits('self') > 10:
    if BuffExists('Protection'):
        Cast('Greater Heal')
        WaitForTargetOrFizzle(5000)
        Target('self')
        Pause(1250 + ping)

    else:
        Cast('Heal')
        WaitForTargetOrFizzle(5000)
        Target('self')
        Pause(500 + ping)

Pause(100)
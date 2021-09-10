# Script variables configuration
ping = 400
faster_casting = 5
faster_cast_recovery = 6
wait_for_target_milliseconds = 2000

class SpellInfo:

    def __init__(self, name, mana_cost, min_skill, delay_in_ms):
        self.name = name
        self.mana_cost = mana_cost
        self.min_skill = min_skill
        self.delay_in_ms = delay_in_ms


# Set mana and spell cast according to your stats
spells = [
    SpellInfo('Cure', 6, 0, 750),
    SpellInfo('Heal', 4, 0, 500),
    SpellInfo('Greater Heal', 11, 24, 1260),
]

#Heal Buddy
if Hits("HealTarget") != MaxHits("HealTarget"):
    if not InRange("HealTarget", 8):
        HeadMsg("Move closer to target!", "HealTarget", 33)
        Pause(500)
    else:
        while Poisoned('HealTarget'):
            Cast('Cure')
            WaitForTarget(wait_for_target_milliseconds)
            Target("HealTarget")
            Pause((spells[0].delay_in_ms + ping) - (faster_cast_recovery * 100))

        if BuffExists('Protection'):
            Cast('Greater Heal')
            WaitForTargetOrFizzle(wait_for_target_milliseconds)
            Target("HealTarget")
            Pause((spells[2].delay_in_ms + ping) - (faster_cast_recovery * 100))

        if not BuffExists('Protection'):
            Cast('Heal')
            WaitForTargetOrFizzle(wait_for_target_milliseconds)
            Target("HealTarget")
            Pause((spells[1].delay_in_ms + ping) - (faster_cast_recovery * 25))



Pause(50)

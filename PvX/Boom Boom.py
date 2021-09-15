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
    # 0
    SpellInfo('Harm', 6, 0, 750),
    # 1
    SpellInfo('Poison', 9, 9, 1000),
    # 2
    SpellInfo('Magic Arrow', 9, 9, 1000),
    # 3
    SpellInfo('Fireball', 9, 9, 1000),
    # 4
    SpellInfo('Energy Bolt', 20, 52, 1750),
    # 5
    SpellInfo('Paralyze', 14, 38, 1500),
    # 6
    SpellInfo('Explosion', 20, 52, 1750),
    # 7
    SpellInfo('Flame Strike', 40, 67, 2000),
]

if not FindAlias('Enemy'):
    HeadMsg('Select our enemy')
    PromptAlias('enemy')
    SetEnemy("enemy")

if TargetExists("Harmful"):
    Target('enemy')


def cast_rotation():
    if InRange('enemy', 1):
        HeadMsg(">> " + spells[0].name + " <<", 'enemy')
        Cast(spells[0].name)
        WaitForTargetOrFizzle(spells[0].delay_in_ms + wait_for_target_milliseconds)
        Target('enemy')
        Pause((spells[0].delay_in_ms + ping) - (faster_cast_recovery * 100))

    else:
        if InRange('enemy', 10):
            HeadMsg(">> " + spells[1].name + " <<", 'enemy')
            Cast(spells[1].name)
            WaitForTargetOrFizzle(spells[1].delay_in_ms + wait_for_target_milliseconds)
            Target('enemy')
            Pause((spells[1].delay_in_ms + ping) - (faster_cast_recovery * 100))
        if InRange('enemy', 10):
            HeadMsg(">> " + spells[7].name + " <<", 'enemy')
            Cast(spells[7].name)
            WaitForTargetOrFizzle(spells[7].delay_in_ms + wait_for_target_milliseconds)
            Target('enemy')
            Pause((spells[7].delay_in_ms + ping) - (faster_cast_recovery * 100))
        if InRange('enemy', 10):
            HeadMsg(">> " + spells[6].name + " <<", 'enemy')
            Cast(spells[6].name)
            WaitForTargetOrFizzle(spells[6].delay_in_ms + wait_for_target_milliseconds)
            Target('enemy')
            Pause((spells[6].delay_in_ms + ping) - (faster_cast_recovery * 100))
        if InRange('enemy', 10):
            HeadMsg(">> " + spells[4].name + " <<", 'enemy')
            Cast(spells[4].name)
            WaitForTargetOrFizzle(spells[4].delay_in_ms + wait_for_target_milliseconds)
            Target('enemy')
            Pause((spells[4].delay_in_ms + ping) - (faster_cast_recovery * 100))


cast_rotation()

# Script variables configuration
ping = 400
faster_casting = 5
faster_cast_recovery = 6
wait_for_target_milliseconds = 2000
AutoMode = True
spell_target = ''


class SpellInfo:

    def __init__(self, name, mana_cost, min_skill, delay_in_ms):
        self.name = name
        self.mana_cost = mana_cost
        self.min_skill = min_skill
        self.delay_in_ms = delay_in_ms


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
    SpellInfo('Flame strike', 40, 67, 2000),
]

if FindAlias('Enemy'):
	UnsetAlias('Enemy')

if not FindAlias('Enemy'):
	if AutoMode:
		spell_target = GetEnemy(['Murderer', 'Enemy', 'criminal', 'gray'], 'Any', 'Closest')
		SetAlias("enemy", spell_target)
	else:
	    HeadMsg('Select our enemy')
	    PromptAlias('enemy')
	    SetEnemy("enemy")
	    spell_target = 'enemy'

if TargetExists("Harmful"):
    Target('enemy')


def cast_harmful(spelltocast):
	global spell_target

	if InRange(spell_target, 10):
		HeadMsg(">> " + spells[spelltocast].name + " <<", spell_target)
		Cast(spells[spelltocast].name)
		WaitForTargetOrFizzle(spells[spelltocast].delay_in_ms + wait_for_target_milliseconds)
		Target(spell_target)
		Pause((spells[spelltocast].delay_in_ms + ping) - (faster_cast_recovery * 100))


cast_harmful(5)

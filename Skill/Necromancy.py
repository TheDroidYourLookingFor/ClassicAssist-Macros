# Name: Magery training to cap
# Description: Train Magery to cap
# Author: Mordor
# Era: Any

class SpellInfo:
    def __init__(self, name, mana_cost, min_skill, delay_in_ms, target=None):
        self.name = name
        self.mana_cost = mana_cost
        self.min_skill = min_skill
        self.delay_in_ms = delay_in_ms
        self.target = target


# When training, target an inanimate object such as anything on the ground or in your backpack to avoid causing damage.
PromptAlias('spell_target')
magery_cap = SkillCap('Necromancy')
ping = 800

while not Dead('self') and Skill('Necromancy') < magery_cap:
    # Set mana and spell cast according to your stats
    spells = [
        SpellInfo('Pain Spike', 5, 40, 1000, GetAlias('spell_target')),
        SpellInfo('Horrific Beast', 11, 50, 1250, None),
        SpellInfo('Wither', 12, 70, 1500, None),
        SpellInfo('Lich Form', 18, 90, 1750, None),
        SpellInfo('Vampiric Embrace', 30, 100, 2000, None),
    ]

    current_spell = None

    for spell in spells:
        if spell.min_skill <= Skill('Necromancy'):
            current_spell = spell

    if Mana('self') > current_spell.mana_cost:
        Cast(current_spell.name)
        if current_spell.target != None:
	        WaitForTarget(3500)
	        Target(current_spell.target)
        Pause(current_spell.delay_in_ms + ping)
    else:
        while Mana('self') < MaxMana('self'):
            if not BuffExists('Active Meditation'):
            	UseSkill('Meditation')
            	Pause(3000)
            	
            	
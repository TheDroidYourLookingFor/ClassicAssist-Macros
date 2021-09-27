# Name: Magery training to cap
# Description: Train Magery to cap
# Author: Mordor
# Era: Any

class SpellInfo:
    def __init__(self, name, mana_cost, min_skill, delay_in_ms):
        self.name = name
        self.mana_cost = mana_cost
        self.min_skill = min_skill
        self.delay_in_ms = delay_in_ms

cap = SkillCap('Chivalry')
ping = 1000

while not Dead('self') and Skill('Chivalry') < cap:
    # Set mana and spell cast according to your stats
    spells = [
        SpellInfo('Consecrate Weapon', 10, 15, 2000),
        SpellInfo('Divine Fury', 15, 45, 3000),
        SpellInfo('Enemy of One', 20, 60, 2000),
        SpellInfo('Holy Light', 10, 70, 2000),
        SpellInfo('Noble Sacrifice', 20, 90, 2000),
    ]

    current_spell = None

    for spell in spells:
        if spell.min_skill <= Skill('Chivalry'):
            current_spell = spell

    if Mana('self') > current_spell.mana_cost:
        Cast(current_spell.name)
        Pause(current_spell.delay_in_ms + ping)
    else:
        while Mana('self') < MaxMana('self'):
            if not BuffExists('Active Meditation'):
            	UseSkill('Meditation')
            	Pause(3000)
            	
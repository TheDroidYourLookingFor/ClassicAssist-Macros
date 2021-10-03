# Name: AutoAttack
# Description: Attacks with melee, chivalry, necromancy, and bushido abilities
# Author: TheDruidUrLookingFor
# Era: Any


SetQuietMode(True)
# Melee Abilities
MeleeSkill = 'Swordsmanship'
MeleePrimary = False
MeleeSecondary = True
# Honor before fight
# Default: True
CastHonor = True
# Buff Vampiric Embrace
# Default: True
CastVampEmbrace = False
# Cast Wither in combat
# Default: False
CastWither = False
# Cast Lightning Strike in combat
# Default: True
CastLightningStrike = True
# Cast Momentum Strike in combat
# Default: False
CastMomentumStrike = False
# Cast Counter Strike in combat
# Default: False
CastCounterAttack = False
# Cast Consecrate Weapon before combat
# Default: True
CastConsecrate = True
# Cast Enemy of One before engaging
# Default: False
CastEnemyOfOne = False
# Run Auto Loot Macro?
# Default: False
DoAutoLoot = False
# Heal/Cure with Chivalry
# Default: True
UseChivalryHealing = True
# Adds a delay if we are looping hte macro
# Default: False
LoopMode = True
# Delay amount when looping
# Default: True
Loop_Delay = 1000


def CheckHealth():
    if UseChivalryHealing:
        if YellowHits('self'):
            Cast('Remove Curse', 'self')
            Pause(1000)

        if YellowHits('self'):
            Cast('Cleanse by Fire', 'self')
            Pause(1000)

        if DiffHits('self') >= 10:
            Cast('Confidence')
            Pause(1000)

        if DiffHits('self') >= 15:
            Cast('Close Wounds')
            Pause(1000)


def FindEnemies():
	UnsetAlias('enemy')
	GetEnemy(['Murderer', 'Enemy', 'criminal', 'gray'], 'Any', 'Closest')
	if not FindObject('enemy', 10):
		UnsetAlias('enemy')
		Stop()

	FoundTarget = 'enemy'
	return FoundTarget


def HonorTarget(target):
    if Hits(target) == MaxHits(target):
        InvokeVirtue('Honor')
        WaitForTarget(5000)
        Target(target, 3)
        Pause(1000)


def AttackTarget(target):
	if CastHonor:
		HonorTarget(target)
	if CastConsecrate:
		Consecrate()
	
	if not War('self'):
		WarMode('on')

	if CastEnemyOfOne:
		EnemyOfOne()
	SetEnemy(target)
	Attack(target)
	Pause(250)
	if CastWither:
	    WitherArea()
	if CastCounterAttack:
	    CounterAttack()
	if CastLightningStrike:
	    LightningStrike()
	if CastMomentumStrike:
	    MomentumStrike()
	if MeleePrimary and Skill(MeleeSkill) >= 70:
	    AttackWithPrimary(target)
	if MeleeSecondary and Skill(MeleeSkill) >= 90:
	    AttackWithSecondary(target)


def CheckInvSpace():
    if Contents('backpack') >= 165:
        HeadMsg("Nearly Full Backpack!!!!", 'self', 1987)


def AutoLoot():
    PlayMacro("Auto Loot")
    Pause(1000)


def AttackWithPrimary(target):
    SetAbility('Primary', 'on')
    Attack(target)
    Pause(1000)


def AttackWithSecondary(target):
    SetAbility('Secondary', 'on')
    Attack(target)
    Pause(1000)


def EnemyOfOne():
    if not BuffExists('Enemy of One'):
        Cast('Enemy of One')
        Pause(1000)


def WitherArea():
    if not InRegion('town', 'self'):
        if FindObject('enemy') and InRange('enemy', 3):
            Cast('Wither')


def LightningStrike():
    if InJournal("lightning precision") or not BuffExists('Lightning Strike'):
        Cast('Lightning Strike')
        Pause(1000)


def MomentumStrike():
    if not BuffExists('Momentum Strike'):
        Cast('Momentum Strike')
        Pause(1000)


def CounterAttack():
    if not BuffExists('Counter Attack'):
        Cast('Counter Attack')
        Pause(1000)


def VampEmbrace():
    if not BuffExists('Vampiric Embrace'):
        Cast('Vampiric Embrace')
        Pause(1000)


def Consecrate():
    if not BuffExists('Consecrate Weapon'):
        Cast('Consecrate Weapon')
        Pause(1000)


def AttackStuff():
    if not InRegion('town', 'self'):
    	ClearTargetQueue()
        FindTarget = FindEnemies()
        AttackTarget(FindTarget)


CheckHealth()
if CastVampEmbrace:
    VampEmbrace()
if DoAutoLoot:
    CheckInvSpace()
    AutoLoot()
AttackStuff()
if LoopMode:
	Pause(Loop_Delay)
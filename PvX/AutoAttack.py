# Name: AutoAttack
# Description: Attacks with melee, chivalry, necromancy, and bushido abilities
# Author: TheDruidUrLookingFor
# Era: Any

SetQuietMode(True)
# Melee Abilities
MeleeSkill = 'Swordsmanship'
MeleePrimary = True
MeleeSecondary = False
# Honor before fight
# Default: True
CastHonor = True
# Buff Vampiric Embrace
# Default: True
CastVampEmbrace = True
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
Loop_Delay = 500
Primary_Reuse = 2000
Secondary_Reuse = 2000
ConfidenceAt = 5
CloseWoundsAt = 15

if not TimerExists('Primary'):
    CreateTimer('Primary')
    SetTimer('Primary', Primary_Reuse)

if not TimerExists('Secondary'):
    CreateTimer('Secondary')
    SetTimer('Secondary', Secondary_Reuse)


def create_timer(timer_name):
    if not TimerExists(timer_name):
        CreateTimer(timer_name)


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
    if MeleePrimary and Skill(MeleeSkill) >= 70 and Timer(
            'Primary') >= Primary_Reuse:
        AttackWithPrimary(target)
        SetTimer('Primary', 0)
    if MeleeSecondary and Skill(MeleeSkill) >= 90 and Timer(
            'Secondary') >= Secondary_Reuse:
        AttackWithSecondary(target)
        SetTimer('Secondary', 0)


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
        #ClearTargetQueue()
        FindTarget = FindEnemies()
        AttackTarget(FindTarget)


def AutoLoot():
    PlayMacro("Auto Loot")
    Pause(1000)


def CheckInvSpace():
    if Contents('backpack') >= 110:
        HeadMsg("Nearly Full Backpack!!!!", 'self', 1987)


def CheckHealth():
    if UseChivalryHealing:
        if YellowHits('self'):
            Cast('Remove Curse', 'self')
            Pause(1000)

        if YellowHits('self'):
            Cast('Cleanse by Fire', 'self')
            Pause(1000)

        if DiffHits('self') >= ConfidenceAt:
            Cast('Confidence')
            Pause(1000)

        if DiffHits('self') >= CloseWoundsAt:
            Cast('Close Wounds', 'self')
            Pause(1000)


def Check_Stuff():
    CheckHealth()
    if CastVampEmbrace:
        VampEmbrace()

    CheckInvSpace()


def AuttoAttack_Startup():
    Check_Stuff()
    AttackStuff()
    if DoAutoLoot:
        AutoLoot()


if LoopMode:
    while not Dead('self'):
        AuttoAttack_Startup()
        Pause(Loop_Delay)
else:
    AuttoAttack_Startup()

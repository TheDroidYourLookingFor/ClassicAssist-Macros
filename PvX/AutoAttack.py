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
# Delay amount when looping
# Default: 1000
Loop_Delay = 1000
# Delay between using melee primary
# Default: 2000
Primary_Reuse = 2000
# Delay between using melee secondary
# Default: 2000
Secondary_Reuse = 2000
# Missing HP to cause us to cast Confidence
# Default: 5
ConfidenceAt = 5
# Missing HP to cause us to cast Close Wounds
# Default: 15
CloseWoundsAt = 15
# Do a Resync() at the end of the macro
# Default: True
Do_Resync = True
# Delay between Resync() commands
# Default: 5000
Resync_Delay = 5000

if not TimerExists('Primary'):
    CreateTimer('Primary')
    SetTimer('Primary', Primary_Reuse)

if not TimerExists('Secondary'):
    CreateTimer('Secondary')
    SetTimer('Secondary', Secondary_Reuse)

if not TimerExists('Resync'):
    CreateTimer('Resync')
    SetTimer('Resync', Resync_Delay)


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
    if MeleePrimary and Skill(MeleeSkill) >= 70 and Timer('Primary') >= Primary_Reuse:
        AttackWithPrimary(target)
        SetTimer('Primary', 0)
    if MeleeSecondary and Skill(MeleeSkill) >= 90 and Timer('Secondary') >= Secondary_Reuse:
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


def Run_Resync():
    if Do_Resync and Timer('Resync') >= Resync_Delay:
        Resync()


def AuttoAttack_Startup():
    Check_Stuff()
    AttackStuff()
    if DoAutoLoot:
        AutoLoot()


AuttoAttack_Startup()
Pause(Loop_Delay)
Run_Resync()

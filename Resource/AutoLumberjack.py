# Name: AutoLJ
# Description: Lumberjacks with one Runic Atlas. Will use the runes randomly
#  and remove from list until out of runes then restart
# Author: TheDroidUrLookingFor

from Assistant import Engine
from System import Array
from System import Random
from random import choice

# settings
# Change This
runes = range(1, 10)
# Shouldnt need to change these
hand = 'TwoHanded'
axes = [0x0f43, 0x1443]
logs = [0x1bdd, 0x07da, 0x04a7, 0x04a8, 0x04a9, 0x04aa, 0x047f]  # colors
to_cont = [
    0x1bdd, 0x1bd7, 0x1bd7, 0x2f5f, 0x318f, 0x3190, 0x3191, 0x3199, 0x5738
]  # dump
cont_serial = 'movecontainer'  # add your container serial to drop stuff
runic_atlas = 'RunicAtlasLJ1'  # home rune must be the first one in first serial
attemptcount = '0'
current_rune = ''
last_rune = ''
# end settings


def startup():
    HeadMsg('Starting up lumberjack Macro', 'self')

    if not FindAlias('RunicAtlasLJ1'):
        HeadMsg('Checking Runic Atlas Alias', 'self')
        PromptAlias('RunicAtlasLJ1')
        runic_atlas = 'RunicAtlasLJ1'

    HeadMsg('Recalling to home rune', 'self')
    recall_home()

    if not FindAlias('movecontainer'):
        HeadMsg('Setting drop off container', 'self')
        PromptAlias('movecontainer')

    HeadMsg('Cutting logs in inventory', 'self')
    cut_logs()
    HeadMsg('Dropping off logs in drop off container', 'self')
    drop_items()


def check_hatchet():
    if not FindLayer(hand):
        for axe in axes:
            if FindType(axe, -1, 'backpack'):
                EquipItem('found', 2)
                Pause(1000)


def recall_home():
    recall('RunicAtlasLJ1', 0)


def recall(runebook, r):
    global attemptcount
    global last_rune
    last_rune = r
    ClearJournal()
    while Mana('self') < 10:
        Pause(100)
    rune_button = r + 50000
    x = X("self")
    y = Y("self")
    atlas_page = r / 16
    UseObject(runebook)
    for i in range(atlas_page):
        WaitForGump(0x1f2, 5000)
        ReplyGump(0x1f2, 1150)
    WaitForGump(0x1f2, 5000)
    ReplyGump(0x1f2, rune_button)
    WaitForGump(0x1f2, 5000)
    ReplyGump(0x1f2, 4000)
    Pause(2000)
    while X("self") == x and Y("self") == y:
        if attemptcount > 3:
            return
        if InJournal("blocking"):
            recall(runebook, r)
            attemptcount += 1
            Pause(1000)
        if InJournal("not yet recovered") or InJournal(
                "ruining thy spell") or InJournal("must wait"):
            recall(runebook, r)
            Pause(1000)
    Pause(1000)


def cut_logs():
    check_hatchet()
    for log in logs:
        while FindType(log, -1, 'backpack'):
            Pause(500)
            UseLayer(hand)
            WaitForTarget(5000)
            Target('found')
            Pause(1000)


def drop_to_home():
    if Weight() <= MaxWeight() - 200:
        Pause(100)
        return
    recall_home()
    drop_items()


def drop_items():
    for items in to_cont:
        while FindType(items, -1, 'backpack'):
            MoveItem('found', cont_serial)
            Pause(1000)


def under_attack():
    if DiffHits('self') > 30:
        x = X('self')
        y = Y('self')
        HeadMsg('Under attacking returning home')
        recall_home()
        while X('self') == x and Y('self') == y:
            if InJournal("blocking") or InJournal("not yet recovered"):
                recall('RunicAtlasLJ1', 0)
                Pause(1000)
            Pause(500)
        Pause(2000)
        Run("East")
        Run("East")
        Run("East")
        Run("North")
        Run("North")
        Run("North")
        Run("North")
        Run("North")
        Run("North")
        Run("North")
        while DiffHits('self') > 10:
            Pause(1000)


def lumber(runebook):
    global current_rune

    if InJournal("blocking", "system"):
        recall(runebook, current_rune)
        lumber(runebook)
    check_hatchet()
    ClearJournal()
    SetTimer("lumber", 8000)
    while Weight() <= MaxWeight():
        if DiffHits('self') > 30:
            under_attack()
            break
        if not TimerExists("lumber"):
            break
        if InJournal("not enough"):
            break
        CancelTarget()
        check_hatchet()
        if FindLayer(hand):
            TargetByResource('found', 'Wood')
            Pause(1000)

    Pause(500)


startup()

while not Dead('self'):
    if not runes:
        HeadMsg('Went through all our runes starting over')
        Replay()
    current_rune = choice(runes)
    runes.Remove(current_rune)
    recall('RunicAtlasLJ1', current_rune)
    Pause(1000)
    lumber('RunicAtlasLJ1')
    cut_logs()
    drop_to_home()
    Pause(100)

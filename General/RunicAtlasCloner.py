# Author: TheDroidUrLookingFor
# Description: Automatic Runebook Cloner from a Library.
# You need to insert the names of each rune on the "Names"
#  List. IT will run over and over if a location is blocked
#  untill it makes it passed too the rune.
#===========================================================
from Assistant import Engine
from System import Array
from System import Random
from random import choice

#Select bag with blank runes
RuneBag = ''
if not FindAlias('Rune_Bag'):
    HeadMsg('Select bag with blank runes.')
    PromptAlias('Rune_Bag')
RuneBag = GetAlias("Rune_Bag")

#Select runebook to be cloned
ClonePrimary = ''
if not FindAlias('ToBeCloned'):
    HeadMsg('Select book to be cloned.')
    PromptAlias('ToBeCloned')
ClonePrimary = GetAlias("ToBeCloned")

#Select a blank book
CloneTarget = ''
if not FindAlias('Blank_RunicAtlas'):
    HeadMsg('Select blank runic atlas to clone to.')
    PromptAlias('Blank_RunicAtlas')
CloneTarget = GetAlias("Blank_RunicAtlas")

# Dont need to change these
attemptcount = ''
last_rune = ''
last_rune_num = ''

# How many runes you want to copy from the Atlas
Runes_Range = range(27)
# Rune Name List
Names = []
#Names.Add('0')
Names.Add('Britain Commons')
#Names.Add('1')
Names.Add('Bucs Den Vault')
#Names.Add('2')
Names.Add('Delucia Vault')
#Names.Add('3')
Names.Add('New Haven Vault')
#Names.Add('4')
Names.Add('New Magincia Vault')
#Names.Add('5')
Names.Add('Minoc Vault')
#Names.Add('6')
Names.Add('Moonglow Vault')
#Names.Add('7')
Names.Add('Papua Vault')

#Names.Add('8')
Names.Add('Trinsic Vault')
#Names.Add('9')
Names.Add('Yew Vault')
#Names.Add('10')
Names.Add('Jhelom Bank')
#Names.Add('11')
Names.Add('Nujelm Bank')
#Names.Add('12')
Names.Add('Skara Brae Bank')
#Names.Add('13')
Names.Add('Serpents Hold Bank')
#Names.Add('14')
Names.Add('Vesper Bank')
#Names.Add('15')
Names.Add('Castle Blackthorn')

#Names.Add('16')
Names.Add('Vela of Cove')
#Names.Add('17')
Names.Add('Wisp of Despise')
#Names.Add('18')
Names.Add('Britain Library')
#Names.Add('19')
Names.Add('Vesper Museum')
#Names.Add('20')
Names.Add('Moonglow Zoo')
#Names.Add('21')
Names.Add('Zento Bank')
#Names.Add('22')
Names.Add('Royal City Bank')
#Names.Add('23')
Names.Add('Moonglow Stables')

#Names.Add('24')
Names.Add('Rune Library')
#Names.Add('25')
Names.Add('Luna Moongate')
#Names.Add('26')
Names.Add('Moonglow Moongate')
#Names.Add('27')
#Names.Add('28')
#Names.Add('29')
#Names.Add('30')
#Names.Add('31')

#Names.Add('32')
#Names.Add('33')
#Names.Add('34')
#Names.Add('35')
#Names.Add('36')
#Names.Add('37')
#Names.Add('38')
#Names.Add('39')

#Names.Add('40')
#Names.Add('41')
#Names.Add('42')
#Names.Add('43')
#Names.Add('44')
#Names.Add('45')
#Names.Add('46')
#Names.Add('47')

# Runes List
Runes = []
Runes.Add(0)
Runes.Add(1)
Runes.Add(2)
Runes.Add(3)
Runes.Add(4)
Runes.Add(5)
Runes.Add(6)
Runes.Add(7)
Runes.Add(8)
Runes.Add(9)
Runes.Add(10)
Runes.Add(11)
Runes.Add(12)
Runes.Add(13)
Runes.Add(14)
Runes.Add(15)
Runes.Add(16)
Runes.Add(17)
Runes.Add(18)
Runes.Add(19)
Runes.Add(20)
Runes.Add(21)
Runes.Add(22)
Runes.Add(23)
Runes.Add(24)
Runes.Add(25)
Runes.Add(26)
Runes.Add(27)
Runes.Add(28)
Runes.Add(29)
Runes.Add(30)
Runes.Add(31)
Runes.Add(32)
Runes.Add(33)
Runes.Add(34)
Runes.Add(35)
Runes.Add(36)
Runes.Add(37)
Runes.Add(38)
Runes.Add(39)
Runes.Add(40)
Runes.Add(41)
Runes.Add(42)
Runes.Add(43)
Runes.Add(44)
Runes.Add(45)
Runes.Add(46)
Runes.Add(47)


# Change these as needed
# Med at this amount of missing mana
MissingManaMed = 100
Recall_Wait_Time = 2500
Wait_Time = 1500
# Do not start at 0
Start_Out_of_Order = False
# Where do we start if not 0 then?
Start_At_Rune = Names[0]
Start_At_RuneNum = Runes[0]

def go_to_safespot():
	PlayMacro("Atlas: Home")


def check_rune_bag():
    if not FindType(0x1f14, -1, RuneBag):
        SysMessage('Out of blank runes!', 25)
        Pause(100)
        PlaySound(984)
        Pause(100)
        PlaySound(987)
        Pause(100)
        PlaySound(988)
        Pause(100)
        MessageBox('Error', '*No Runes restock & restart*')
        Stop()


def recall(ra, r):
    global attemptcount
    global last_rune
    last_rune = r
    ClearJournal()
    check_mana()
    rune_button = r + 50000
    x = X("self")
    y = Y("self")
    UseObject(ra)
    if last_rune >= 0 and last_rune <= 16:
    	WaitForGump(0x1f2, 5000)
        ReplyGump(0x1f2, 4)
        WaitForGump(0x1f2, 5000)
        ReplyGump(0x1f2, 4)
        WaitForGump(0x1f2, 5000)
    if last_rune >= 17 and last_rune <= 32:
    	WaitForGump(0x1f2, 5000)
        ReplyGump(0x1f2, 4)
        WaitForGump(0x1f2, 5000)
        ReplyGump(0x1f2, 4)
        WaitForGump(0x1f2, 5000)
        ReplyGump(0x1f2, 5)
        WaitForGump(0x1f2, 5000)
    if last_rune >= 33:
        WaitForGump(0x1f2, 5000)
        ReplyGump(0x1f2, 5)
        WaitForGump(0x1f2, 5000)
        ReplyGump(0x1f2, 5)
        WaitForGump(0x1f2, 5000)
    ReplyGump(0x1f2, rune_button)
    WaitForGump(0x1f2, 5000)
    ReplyGump(0x1f2, 4000)
    Pause(Recall_Wait_Time)
    while X("self") == x and Y("self") == y:
        if attemptcount > 3:
            return
        if InJournal("blocking"):
            attemptcount += 1
            remove_rune(current_rune)
            recall(ra, r)
            Pause(1000)
        if InJournal("not yet recovered") or InJournal(
                "ruining thy spell") or InJournal("must wait"):
            recall(ra, r)
            Pause(1000)
        Pause(50)
    Pause(1750)


def mark_rune(r, rn):
    check_mana()
    UseObject(RuneBag)
    Pause(1000)
    if FindType(0x1f14, -1, RuneBag):
        Cast('Mark')
        WaitForTargetOrFizzle(5000)
        if InJournal("your concentration is disturbed"):
            ClearJournal()
            mark_rune(r, rn)
        else:
            Target('found')
            Pause(1000)
            UseObject('found')
            WaitForPrompt(15000)
            PromptMsg(rn)
            Pause(1000)
            MoveItem('found', CloneTarget)
            Pause(1000)
    else:
        PlaySound(984)
        Pause(100)
        PlaySound(987)
        Pause(100)
        PlaySound(988)
        Pause(100)
        MessageBox('Error', '*No Runes restock & restart*')
        Stop()


def check_mana():
	while Mana('self') < MaxMana('self'):
	    while not BuffExists('Active Meditation') and Mana('self') < (MaxMana('self') - MissingManaMed):
	        UseSkill('Meditation')
	        Pause(4000)
        Pause(1000)


def begin_clone():
    for current_rune in Runes_Range:
    	last_rune = Names[current_rune]
    	last_rune_num = Runes[current_rune]
        if Start_Out_of_Order:
            if current_rune != Start_At_RuneNum and current_rune < Start_At_RuneNum:
                continue
        recall(ClonePrimary, last_rune_num)
        Pause(Wait_Time)
        mark_rune(last_rune_num, last_rune)
        Pause(Wait_Time)


def clone_startup():
	ClearJournal()
	check_rune_bag()
	check_mana()
	begin_clone()


clone_startup()
Pause(1000)
go_to_safespot()
SysMessage('Runic Atlas is done being copied!', 1999)
UnsetAlias('ToBeCloned')
UnsetAlias('Blank_RunicAtlas')

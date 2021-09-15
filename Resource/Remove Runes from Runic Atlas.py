#Select bag with blank runes
SourceBag = ''
if not FindAlias('Source_Bag'):
    HeadMsg('Select bag with blank runes.')
    PromptAlias('Source_Bag')
SourceBag = GetAlias("Source_Bag")
#Select bag with blank runes
RuneBag = ''
if not FindAlias('Rune_Bag'):
    HeadMsg('Select bag to put blank runes.')
    PromptAlias('Rune_Bag')
RuneBag = GetAlias("Rune_Bag")

#Select runic atlas to empty
RunicAtlas = ''
if not FindAlias('Empty_Target'):
    HeadMsg('Select runic atlas to empty of runes.')
    PromptAlias('Empty_Target')
RunicAtlas = GetAlias("Empty_Target")

MoveRunes = False

while not InJournal("There is no rune to be dropped."):
	UseObject(RunicAtlas)
	WaitForGump(0x1f2, 5000)
	ReplyGump(0x1f2, 2)

ClearJournal()

while FindType(0x1f14, -1, SourceBag) and MoveRunes:
	MoveItem('found', RuneBag)
	Pause(1000)
#Select bag with blank runes
SourceBag = ''
UnsetAlias('Source_Bag')
if not FindAlias('Source_Bag'):
    HeadMsg('Select bag with blank runes.')
    PromptAlias('Source_Bag')
SourceBag = GetAlias("Source_Bag")
#Select bag with blank runes
RuneBag = ''
UnsetAlias('Rune_Bag')
if not FindAlias('Rune_Bag'):
    HeadMsg('Select bag to put blank runes.')
    PromptAlias('Rune_Bag')
RuneBag = GetAlias("Rune_Bag")

while FindType(0x1f14, 0, SourceBag):
	MoveItem('found', RuneBag)
	Pause(1000)
# Set my Primary Runic Atlas
if not FindAlias('RunicAtlas1'):
  PromptAlias('RunicAtlas1')

UseObject('RunicAtlas1')
WaitForGump(0x1f2, 5000)
ReplyGump(0x1f2, 4000)

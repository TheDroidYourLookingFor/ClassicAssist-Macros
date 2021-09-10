# Set my Primary Runic Atlas
if not FindAlias('RunicAtlas1'):
  PromptAlias('RunicAtlas1')
#Make sure your home rune is the first rune in the book  
UseObject('RunicAtlas1')
WaitForGump(0x1f2, 5000)
ReplyGump(0x1f2, 4)
WaitForGump(0x1f2, 5000)
ReplyGump(0x1f2, 50025)
WaitForGump(0x1f2, 5000)
ReplyGump(0x1f2, 4000)

#Note: NEVER set a looping clickscreen
#
# Finds a boat in pack and uses it to start boat placment
UseType(0x14f4, 'any', 'backpack')
# Lil Pause to allow above to exacute
Pause(300)
# Click screen has 4 params  the first two are the X and Y pos
#using your monitors resoulution as the X and Y  of where on
#screen you want to click / place boat. The third Param is the
#type of click either single or double, and lastly which mouse
#button left or right..
#
# Below is what you would need to place the boat , however you
#will need to change the X and Y pos and designe the macro
#from a hard coded player position ..
clickscreen(756, 620, 'single', 'left')
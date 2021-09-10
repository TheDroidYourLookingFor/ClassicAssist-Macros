#Pet List
if not ListExists('PetList'):
  CreateList('PetList')
  #add an entry for each pet you use:
  PushList('PetList', '0x64296c3') # A
  PushList('PetList', '0x623968b') # B
  
# Feed Pets in List
for i in 'PetList':
  if FindObject(List('PetList[i]')):
    if Graphic('Found' == 0x2f0):
      Feed(List('PetList[i]'), '0x78', 'any', 1)
      HeadMsg('Feeding Pet')
      Pause(750)
    else:
      Feed(List('PetList[i]'), 'Meat', 'any', 1)
      HeadMsg('Feeding Pet Meat')
      Pause(750)

HeadMsg('Done feeding all pets in the list!', 1998)
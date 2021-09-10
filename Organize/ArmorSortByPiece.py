#Experience
#Armor Organizer(2.0)
if not ListExists('NonMedHelm'):
  CreateList('NonMedHelm')
  PushList('NonMedHelm', 0x1451) #Bone, Helmet
  PushList('NonMedHelm', 0x1408) #Close, Helmet
  PushList('NonMedHelm', 0x1412) #Plate, Helm)
  PushList('NonMedHelm', 0x140a) #Helmet
  PushList('NonMedHelm', 0x140c) #Bascinet
  PushList('NonMedHelm', 0x140e) #Norse, Helm
  PushList('NonMedHelm', 0x13bb) #Chainmail, Coif

if not ListExists('NonMedGorget'):
  CreateList('NonMedGorget')
  PushList('NonMedGorget', 0x1413) #Plate, Gorget)
  PushList('NonMedGorget', 0x13d6) #Studded, Gorget)

if not ListExists('NonMedTunic'):
  CreateList('NonMedTunic')
  PushList('NonMedTunic', 0x144f) #Bone, Tunic)
  PushList('NonMedTunic', 0x1415) #Plate, Chest)
  PushList('NonMedTunic', 0x13bf) #Chainmail, Tunic)
  PushList('NonMedTunic', 0x13ec) #Ringmail, Tunic)
  PushList('NonMedTunic', 0x13db) #Studded, Tunic)
  PushList('NonMedTunic', 0x1c04) #Female, Plate)
  PushList('NonMedTunic', 0x1c0c) #Female Studded, Bustier)
  PushList('NonMedTunic', 0x1c02) #Female Studded, Armor)

if not ListExists('NonMedSleeve'):
  CreateList('NonMedSleeve')
  PushList('NonMedSleeve', 0x144e) #Bone, Sleeves)
  PushList('NonMedSleeve', 0x1410) #Platemail, Arms)
  PushList('NonMedSleeve', 0x13ee) #Ringmail, Sleeves)
  PushList('NonMedSleeve', 0x13dc) #Studded, Sleeves)

if not ListExists('NonMedGlove'):
  CreateList('NonMedGlove')
  PushList('NonMedGlove', 0x1414) #Platemail, Gloves)
  PushList('NonMedGlove', 0x13eb) #Ringmail, Gloves)
  PushList('NonMedGlove', 0x13d5) #Studded, Gloves)
  PushList('NonMedGlove', 0x1450) #Bone, Glove)

if not ListExists('NonMedLeg'):
  CreateList('NonMedLeg')
  PushList('NonMedLeg', 0x1452) #Bone, Legs)
  PushList('NonMedLeg', 0x1411) #Platemail, Legs)
  PushList('NonMedLeg', 0x13be) #Chainmail, Leggins)
  PushList('NonMedLeg', 0x13f0) #Ringmail, Leggins)
  PushList('NonMedLeg', 0x13da) #Studded, Leggings)

#Medible Parts
if not ListExists('MedHelm'):
  CreateList('MedHelm')
  PushList('MedHelm', 0x1db9) #Leather, Cap)

if not ListExists('MedGorget'):
  CreateList('MedGorget')
  PushList('MedGorget', 0x13c7) #Leather, Gorget)

if not ListExists('MedTunic'):
  CreateList('MedTunic')
  PushList('MedTunic', 0x13cc) #Leather, Tunic)
  PushList('MedTunic', 0x1c06) #Female Leather, Armor)
  PushList('MedTunic', 0x1c0a) #Female Leather, Bustier)

if not ListExists('MedSleeve'):
  CreateList('MedSleeve')
  PushList('MedSleeve', 0x13cd) #Leather, Sleeves)

if not ListExists('MedGlove'):
  CreateList('MedGlove')
  PushList('MedGlove', 0x13c6) #Leather, Gloves)

if not ListExists('MedLeg'):
  CreateList('MedLeg')
  PushList('MedLeg', 0x13cb) #Leather, Pants)
  PushList('MedLeg', 0x1c00) #Female Leather, Shorts)
  PushList('MedLeg', 0x1c08) #Female Leather, Skirt)

if not FindObject('Medable, Hat'):
  HeadMsg('Select Bag/Chest for, Medable, Hat')
  PromptAlias('Medable Hat')

if not FindObject('Non-Med, Hat'):
  HeadMsg('Select Bag/Chest for, Non-Med, Hat')
  PromptAlias('Non-Med Hat')

if not FindObject('Medable, Gorget'):
  HeadMsg('Select Bag/Chest for, Medable, Gorget')
  PromptAlias('Medable Gorget')

if not FindObject('Non-Med, Gorget'):
  HeadMsg('Select Bag/Chest for, Non-Med, Gorget')
  PromptAlias('Non-Med Gorget')

if not FindObject('Medable, Tunic'):
  HeadMsg('Select Bag/Chest for, Medable, Tunic')
  PromptAlias('Medable Tunic')

if not FindObject('Non-Med, Tunic'):
  HeadMsg('Select Bag/Chest for, Non-Med, Tunic')
  PromptAlias('Non-Med Tunic')

if not FindObject('Medable, Sleeve'):
  HeadMsg('Select Bag/Chest for, Medable, Sleeve')
  PromptAlias('Medable Sleeve')

if not FindObject('Non-Med, Sleeve'):
  HeadMsg('Select Bag/Chest for, Non-Med, Sleeve')
  PromptAlias('Non-Med Sleeve')

if not FindObject('Medable, Glove'):
  HeadMsg('Select Bag/Chest for, Medable, Glove')
  PromptAlias('Medable Glove')

if not FindObject('Non-Med, Glove'):
  HeadMsg('Select Bag/Chest for, Non-Med, Glove')
  PromptAlias('Non-Med Glove')

if not FindObject('Medable, Leg'):
  HeadMsg('Select Bag/Chest for, Medable, Leg')
  PromptAlias('Medable Leg')

if not FindObject('Non-Med, Leg'):
  HeadMsg('Select Bag/Chest for, Non-Med, Leg')
  PromptAlias('Non-Med Leg')

if not FindAlias('Sort Bag'):
  HeadMsg('Select Bag, to, sort')
  PromptAlias('Sort Bag')

for 0 to 'NonMedHelm'
  while MoveType(NonMedHelm[], 'Sort Bag', 'Non-Med, Hat')
    Pause(600)
  

for 0 to 'MedHelm'
  while MoveType(MedHelm[], 'Sort Bag', 'Medable, Hat')
    Pause(600)
  

for 0 to 'NonMedGorget'
  while MoveType(NonMedGorget[], 'Sort Bag', 'Non-Med, Gorget')
    Pause(600)
  

for 0 to 'MedGorget'
  while MoveType(MedGorget[], 'Sort Bag', 'Medable, Gorget')
    Pause(600)
  

for 0 to 'NonMedTunic'
  while MoveType(NonMedTunic[], 'Sort Bag', 'Non-Med, Tunic')
    Pause(600)
  

for 0 to 'MedTunic'
  while MoveType(MedTunic[], 'Sort Bag', 'Medable, Tunic')
    Pause(600)
  

for 0 to 'NonMedSleeve'
  while MoveType(NonMedSleeve[], 'Sort Bag', 'Non-Med, Sleeve')
    Pause(600)
  

for 0 to 'MedSleeve'
  while MoveType(MedSleeve[], 'Sort Bag', 'Medable, Sleeve')
    Pause(600)
  

for 0 to 'NonMedGlove'
  while MoveType(NonMedGlove[], 'Sort Bag', 'Non-Med, Glove')
    Pause(600)
  

for 0 to 'MedGlove'
  while MoveType(MedGlove[], 'Sort Bag', 'Medable, Glove')
    Pause(600)
  

for 0 to 'NonMedLeg'
  while MoveType(NonMedLeg[], 'Sort Bag', 'Non-Med, Leg')
    Pause(600)
  

for 0 to 'MedLeg'
  while MoveType(MedLeg[], 'Sort Bag', 'Medable, Leg')
    Pause(600)
  

HeadMsg('No More to Sort')
Stop()
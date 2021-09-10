#Get Enemy Grey Only
GetEnemy('gray', 'criminal', 'closest')
if FindObject('enemy'):
  TargetObject! 'enemy'
  if Criminal('enemy'):
    Attack('enemy')
    Target('enemy')
    CancelTarget()
    Stop()
  
  if gray 'enemy':
    Attack('enemy')
    Target('enemy')
    CancelTarget()
    Stop()

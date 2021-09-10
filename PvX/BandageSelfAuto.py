while not dead
  if not TimerExists('BandageTimer'):
    CreateTimer('BandageTimer')
    SetTimer('BandageTimer' 10250)
  
  # Check the Bandage(Timer(to see if enough time has elapsed)):
  if Timer('BandageTimer' < 10250):
    # Small delay to slow down the loop. 100 milliseconds means we will not miss
    # a bandage.
    Pause(100)
    # We need to wait for our current Bandage(to finish so start the while)
    # loop from the beginning
    continue
  
  # if we are Poisoned(or don't have full health):
  if Poisoned('self' or Hits() < MaxHits()):
    # Enough time has elapsed lets apply a bandage.
    BandageSelf()
    # Reset the timer.
    SetTimer('BandageTimer' 0)

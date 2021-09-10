if not FindAlias('Enemy'):
    HeadMsg('Select our enemy')
    PromptAlias('enemy')
    SetEnemy("enemy")

if TargetExists("Harmful"):
    Target('enemy')

if InRange('enemy', 1):
    Cast('harm')
    WaitForTargetOrFizzle(3500)
    Target('enemy')
    Pause(1250)

else:
    if InRange('enemy', 10):
        Cast('Explosion')
        WaitForTargetOrFizzle(3500)
        Target('enemy')
        Pause(1250)

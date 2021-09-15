ClearList('Buddy')
if not ListExists('Buddy'):
  CreateList('Buddy')

ClearList('Pet')
if not ListExists('Pet'):
  CreateList('Pet')

# Friend One
if not InList('Buddy', 0x0000000):
  PushList('Buddy', 0x0000000)
# Friend Two
if not InList('Buddy', 0x0000000):
  PushList('Buddy', 0x0000000)

# Pets
# Pet One
if not InList('Pet', 0x0000000):
  PushList('Pet', 0x0000000)
# Pet Two
if not InList('Pet', 0x0000000):
  PushList('Pet', 0x0000000)
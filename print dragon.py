dragon_body = ['  @   ', ' / \  ', '(    )', '|""""|', '\(__)/']
fire_parts = ['   *   ', '  ***  ', ' ***** ', '*******', ' ***** ', '  ***  ', '   *   ']

for part in dragon_body:
    print(part)

print()  # Adding a blank line for separation

for i in range(len(fire_parts)):
    if i % 2 == 0:
        print(' ' * (len(dragon_body[0]) // 2 - len(fire_parts[i]) // 2) + fire_parts[i])
    else:
        print(fire_parts[i])


dragon = [
    "                  __/ \\__",
    "                 / -   - \\",
    "             ___|       |___",
    "           /      |     |   \\",
    "        __/       /\\_     |  \\__",
    "     __/   /\\_    \\    /\\__    \\__",
    "    /  _/       \\__ \\_ \\_      \\",
    "   / __/ \\__       \\_/    \\__     \\",
    " _/ /         \\__  \\__     \\__   \\_",
    "/ /         /       \\       \\ \\__  \\__",
    "\\ \\_____/           \\_____/     \\__/",
    "   \\________________________/"
]

fire = [
    "                (  ( ( ",
    "                 ) ) ) ",
    "                (  ( ( ",
    "      ________  ) ) ) ",
    "                (  ( (",
    "                 ) ) ) ",
    "                (  ( ( ",
]

# Print the dragon
for line in dragon:
    print(line)

# Print the fire
for line in fire:
    print(line)

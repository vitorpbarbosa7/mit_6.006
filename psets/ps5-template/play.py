from solve_tilt import move, board_str

B = (
    ('#', '#', '.', '.', '.'),
    ('.', 'o', '#', '.', '.'),
    ('.', '.', 'o', '.', '.'),
    ('.', '.', '.', '.', '.'),
    ('#', '#', '#', '.', '.')
)

moves = ['left', 'down', 'right','down', 'left']

for m in moves:
    B = move(B, m)
    S = board_str(B)
    print(S)

# output
# +-----+
# |##...|
# |o.#..|
# |o....|
# |.....|
# |###..|
# +-----+
# +-----+
# |##...|
# |..#..|
# |o....|
# |o....|
# |###..|
# +-----+
# +-----+
# |##...|
# |..#..|
# |....o|
# |....o|
# |###..|
# +-----+
# +-----+
# |##...|
# |..#..|
# |.....|
# |....o|
# |###.o|
# +-----+
# +-----+
# |##...|
# |..#..|
# |.....|
# |o....|
# |###o.|
# +-----+

grid = [
    "################",
    "#S.............#",
    "#.####.T.#####.#",
    "#......#.......#",
    "#####.T.######.#",
    "#..............#",
    "################",
]

start_location = None
task_locations = []

for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if char == 'S':
            start_location = (r, c)
        elif char == 'T':
            task_locations.append((r, c))

print("Start 'S' at:", start_location)
print("Tasks 'T' at:", task_locations)

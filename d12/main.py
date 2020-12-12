
with open('input.txt', 'r') as inp:
    instructions = [(line[0], int(line[1:])) for line in inp]

# Ship starts at 0,0 facing East(zero degrees)
ship = {'x': 0,
        'y': 0,
        'heading': 0}

# Compass (axis, degrees)
#             N(y+, 270)
#             |
# W(x-, 180)--0--E(x+, 0)
#             |
#             S(y-, 90)

for inst, val in instructions:
    if inst == 'N':
        ship['y'] += val
    if inst == 'S':
        ship['y'] -= val
    if inst == 'E':
        ship['x'] += val
    if inst == 'W':
        ship['x'] -= val
    if inst == 'F':
        direction = ship['heading'] % 360
        if direction == 0:
            ship['x'] += val
        elif direction == 90:
            ship['y'] -= val
        elif direction == 180:
            ship['x'] -= val
        elif direction == 270:
            ship['y'] += val
        else:
            print("NON RIGHT ANGLE HEADING")
            exit()
    if inst == 'L':
        if ship['heading'] == 0:
            ship['heading'] = 360
        ship['heading'] -= val
    if inst == 'R':
        ship['heading'] += val

print(ship)
print('Part 1: ', abs(ship['x']) + abs(ship['y']))

# Ship starts at 0,0 facing East(zero degrees)
ship = {'x': 0,
        'y': 0,
        'heading': 0}


waypoint = {'x': 10,
        'y': 1}

for inst, val in instructions:
    if inst == 'N':
        waypoint['y'] += val
    if inst == 'S':
        waypoint['y'] -= val
    if inst == 'E':
        waypoint['x'] += val
    if inst == 'W':
        waypoint['x'] -= val
    if inst == 'F':
        ship['x'] += waypoint['x'] * val
        ship['y'] += waypoint['y'] * val
    if inst == 'R':
        # What do you mean no trigo?
        for i in range(0, val//90):
            waypoint['x'], waypoint['y'] = waypoint['y'], -waypoint['x']
    if inst == 'L':
        for i in range(0, val//90):
            waypoint['x'], waypoint['y'] = -waypoint['y'], waypoint['x']

print('Part 2: ', abs(ship['x']) + abs(ship['y']))
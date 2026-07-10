def can_stack(cubes):
    last = float('inf')
    possible = True

    while cubes:
        if cubes[0] >= cubes[-1]:
            current = cubes.pop(0)
        else:
            current = cubes.pop()

        if current > last:
            possible = False
            break

        last = current

    return possible
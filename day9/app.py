def main():
    input = open("input.txt").readlines()

    part1(input)
    part2(input)


def part1(input):
    VISITED_SET = set()

    head_coordinates = (0, 0)
    tail_coordinates = (0, 0)

    VISITED_SET.add(tail_coordinates)

    for i in input:
        direction, steps = i.split(' ')

        for x in range(int(steps)):
            head_coordinates, tail_coordinates, _ = \
                get_new_position(*head_coordinates, *tail_coordinates,
                                 direction)

            VISITED_SET.add(tail_coordinates)

    print("Part 1:", len(VISITED_SET))


def part2(input):
    VISITED_SET = set()
    NUM_LINKS = 10

    position = [(0, 0) for x in range(NUM_LINKS)]

    VISITED_SET.add(position[-1])

    for i in input:
        direction, steps = i.split(' ')

        for x in range(int(steps)):
            is_head = True
            for y in range(NUM_LINKS - 1):
                front_position = position[y]
                back_position = position[y + 1]

                position[y], position[y + 1], has_changed = \
                    get_new_position(
                        *front_position, *back_position,
                        direction, is_head
                    )

                if not has_changed:
                    break

                is_head = False

            VISITED_SET.add(position[-1])

    print("Part 2:", len(VISITED_SET))


def get_new_position(head_x_coord, head_y_coord, tail_x_coord,
                     tail_y_coord, direction, is_head=True):
    if not is_head:
        new_head = (head_x_coord, head_y_coord)
    elif direction == "R":
        new_head = (head_x_coord + 1, head_y_coord)
    elif direction == "L":
        new_head = (head_x_coord - 1, head_y_coord)
    elif direction == "U":
        new_head = (head_x_coord, head_y_coord + 1)
    elif direction == "D":
        new_head = (head_x_coord, head_y_coord - 1)

    new_tail = check_move(*new_head, tail_x_coord, tail_y_coord)

    has_changed = False if new_tail == (tail_x_coord, tail_y_coord) else True

    return new_head, new_tail, has_changed


def check_move(head_x_coord, head_y_coord, tail_x_coord, tail_y_coord):
    if abs(head_x_coord - tail_x_coord) <= 1 \
            and abs(head_y_coord - tail_y_coord) <= 1:
        new_tail = (tail_x_coord, tail_y_coord)
    else:
        if head_y_coord == tail_y_coord:
            new_tail_x = (head_x_coord + tail_x_coord) // 2
            new_tail = (new_tail_x, tail_y_coord)
        elif head_x_coord == tail_x_coord:
            new_tail_y = (head_y_coord + tail_y_coord) // 2
            new_tail = (tail_x_coord, new_tail_y)
        else:
            new_tail_x = tail_x_coord + 1 if head_x_coord >\
                tail_x_coord else tail_x_coord - 1
            new_tail_y = tail_y_coord + 1 if head_y_coord >\
                tail_y_coord else tail_y_coord - 1
            new_tail = (new_tail_x, new_tail_y)

    return new_tail


if __name__ == "__main__":
    main()

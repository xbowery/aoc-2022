def main():
    input = open("input.txt", "r").readlines()

    part1(input)
    part2(input)


def part1(input):
    count = 0
    register = 1
    temp = 0
    results = []

    for i in input:
        if "noop" in i:
            count += 1
            if count in [20, 60, 100, 140, 180, 220]:
                results.append(count * register)
        elif "addx" in i:
            temp = int(i.split(' ')[1])

            count += 1
            if count in [20, 60, 100, 140, 180, 220]:
                results.append(count * register)

            count += 1
            if count in [20, 60, 100, 140, 180, 220]:
                results.append(count * register)

            register += temp

    print(sum(results))


def part2(input):
    sprite_pos = [
        "#", "#", "#", ".", ".", ".", ".", ".", ".", ".",
        ".", ".", ".", ".", ".", ".", ".", ".", ".", ".",
        ".", ".", ".", ".", ".", ".", ".", ".", ".", ".",
        ".", ".", ".", ".", ".", ".", ".", ".", ".", "."
    ]
    cur_sprite_pos = 0

    crt_msg = ""

    count = 0

    for i in input:
        if "noop" in i:
            if sprite_pos[count % 40] == "#":
                crt_msg += "#"
            else:
                crt_msg += "."
            count += 1
            if count % 40 == 0:
                crt_msg += "\n"
        else:
            temp = int(i.split(' ')[1])

            if sprite_pos[count % 40] == "#":
                crt_msg += "#"
            else:
                crt_msg += "."

            count += 1

            if count % 40 == 0:
                crt_msg += "\n"

            if sprite_pos[count % 40] == "#":
                crt_msg += "#"
            else:
                crt_msg += "."

            count += 1

            if count % 40 == 0:
                crt_msg += "\n"

            sprite_pos[cur_sprite_pos % 40] = "."
            sprite_pos[(cur_sprite_pos+1) % 40] = "."
            sprite_pos[(cur_sprite_pos+2) % 40] = "."

            cur_sprite_pos += temp

            sprite_pos[cur_sprite_pos % 40] = "#"
            sprite_pos[(cur_sprite_pos+1) % 40] = "#"
            sprite_pos[(cur_sprite_pos+2) % 40] = "#"

    print(crt_msg)


if __name__ == "__main__":
    main()

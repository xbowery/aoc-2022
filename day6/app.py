def main():
    input = open("input.txt").readlines()[0].strip("\n\r")

    part1(input)
    part2(input)


def part1(input):
    arr = [input[3], input[2], input[1], input[0]]

    if (unique_values(arr)):
        print("Part 1: 4")

    for i in range(4, len(input)):
        arr.pop()
        arr.insert(0, input[i])

        if (unique_values(arr)):
            print(f"Part 1: {i + 1}")
            return


def part2(input):
    arr = []
    for i in range(14):
        arr.insert(0, input[i])

    if (unique_values(arr)):
        print("Part 1: 14")

    for i in range(14, len(input)):
        arr.pop()
        arr.insert(0, input[i])

        if (unique_values(arr)):
            print(f"Part 1: {i + 1}")
            return


def unique_values(arr):
    s = set()
    for x in arr:
        if x in s: return False
        s.add(x)
    return True


if __name__ == "__main__":
    main()
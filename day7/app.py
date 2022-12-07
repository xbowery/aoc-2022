from collections import defaultdict


def main():
    input = open("input.txt", "r").read().splitlines()

    DIRECTORY_SIZE = defaultdict(int)
    DIRECTORY_LIST = []

    for i in input:
        temp = i.split(' ')
        if temp == ["$", "cd", ".."]:
            DIRECTORY_LIST.pop()
        elif temp[0] == "$" and temp[1] == "cd":
            if temp[-1] == "/":
                DIRECTORY_LIST = [""]
            else:
                path_after = f"{DIRECTORY_LIST[-1]}/{temp[-1]}"
                DIRECTORY_LIST.append(path_after)
        elif temp[0] == "dir" or (temp[0] == "$" and temp[1] == "ls"):
            continue
        else:
            for dir in DIRECTORY_LIST:
                DIRECTORY_SIZE[dir] += int(temp[0])

    p1_result = part1(DIRECTORY_SIZE)
    print(f"Part 1: {p1_result}")

    p2_result = part2(DIRECTORY_SIZE)
    print(f"Part 2: {p2_result}")


def part1(dict):
    TOTAL_SIZE = 100000

    result = 0

    for file_sizes in dict.values():
        if file_sizes <= TOTAL_SIZE:
            result += file_sizes

    return result


def part2(dict):
    TOTAL_SIZE = 70000000
    REQUIRED_SIZE = 30000000

    result = REQUIRED_SIZE

    unused_size = TOTAL_SIZE - dict[""]
    size_to_clear = REQUIRED_SIZE - unused_size

    if size_to_clear <= 0:
        return 0

    for sizes in dict.values():
        if sizes >= size_to_clear and sizes < result:
            result = sizes

    return result


if __name__ == "__main__":
    main()

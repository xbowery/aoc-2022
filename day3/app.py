import math
from collections import Counter


def main():
    file = open("input.txt").readlines()

    input = [r.strip('\n\r') for r in file]

    part1(input)
    part2(input)


def part1(input: list):
    sum = 0

    for i in input:
        length = len(i) - 1
        half_len = math.floor(length / 2)

        counter1 = Counter(i[:half_len+1])
        counter2 = Counter(i[half_len+1:])

        intersect = counter1 & counter2
        keys = list(intersect.keys())

        for k in keys:
            sum += getASCIIValueChar(k)

    print(f"Part 1: {sum}")


def part2(input: list):
    sum = 0

    for i in range(0, len(input), 3):
        counter1 = Counter(input[i])
        counter2 = Counter(input[i+1])
        counter3 = Counter(input[i+2])

        intersect = (counter1 & counter2) & counter3
        keys = intersect.keys()

        for k in keys:
            sum += getASCIIValueChar(k)

    print(f"Part 2: {sum}")


def getASCIIValueChar(k):
    if k >= 'a' and k <= 'z':
        return (ord(k) - 96)
    elif k >= 'A' and k <= 'Z':
        return (ord(k) - 38)


if __name__ == "__main__":
    main()

def main():
    # Read file
    file = open("input.txt", "r").readlines()

    # Regex to filter out file input
    input = [r.strip('\n\r') for r in file]

    elf_dict = {}
    counter = 1
    int_max = 0

    for i in input:
        if (i != ''):
            int_max += int(i)
        else:
            int_max = 0
            counter += 1
        elf_dict[counter] = int_max

    values = list(elf_dict.values())
    values.sort()
    print(f"Part 1: {max(values)}")
    print(f"Part 2: {values[-1] + values[-2] + values[-3]}")


if __name__ == "__main__":
    main()
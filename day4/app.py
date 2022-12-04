def main():
    file = open("input.txt").readlines()

    input = [r.strip('\n\r') for r in file]

    part1_result = 0
    part2_result = 0

    for i in input:
        elf1 = i.split(",")[0]
        elf2 = i.split(",")[1]

        num1_elf1 = int(elf1.split("-")[0])
        num2_elf1 = int(elf1.split("-")[1])
        num1_elf2 = int(elf2.split("-")[0])
        num2_elf2 = int(elf2.split("-")[1])

        if (num1_elf1 <= num1_elf2 and num2_elf1 >= num2_elf2):
            part1_result += 1
            part2_result += 1

        elif (num1_elf1 >= num1_elf2 and num2_elf1 <= num2_elf2):
            part1_result += 1
            part2_result += 1

        elif (num2_elf1 >= num1_elf2 and num1_elf1 <= num1_elf2):
            part2_result += 1

        elif (num2_elf2 >= num1_elf1 and num1_elf2 <= num1_elf1):
            part2_result += 1

    print(f"Part 1: {part1_result}")
    print(f"Part 2: {part2_result}")


if __name__ == "__main__":
    main()

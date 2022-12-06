def main():
    file = open("input.txt").readlines()[10:]

    input = [r.strip('\n\r') for r in file]

    part1(input)
    part2(input)


def generate_input():
    stack1 = ['R', 'N', 'F', 'V', 'L', 'J', 'S', 'M']
    stack2 = ['P', 'N', 'D', 'Z', 'F', 'J', 'W', 'H']
    stack3 = ['W', 'R', 'C', 'D', 'G']
    stack4 = ['N', 'B', 'S']
    stack5 = ['M', 'Z', 'W', 'P', 'C', 'B', 'F', 'N']
    stack6 = ['P', 'R', 'M', 'W']
    stack7 = ['R', 'T', 'N', 'G', 'L', 'S', 'W']
    stack8 = ['Q', 'T', 'H', 'F', 'N', 'B', 'V']
    stack9 = ['L', 'M', 'H', 'Z', 'N', 'F']

    return stack1, stack2, stack3, stack4, stack5, stack6,\
           stack7, stack8, stack9


def part1(input):
    stack1, stack2, stack3, stack4, stack5,\
    stack6, stack7, stack8, stack9 = generate_input()
    for i in input:
        number_to_move = int(i.split(' ')[1])
        move_from = i.split(' ')[3]
        move_to = i.split(' ')[5]

        stack_dict = {'1': stack1, '2': stack2, '3': stack3, '4': stack4,
                      '5': stack5, '6': stack6, '7': stack7, '8': stack8,
                      '9': stack9}

        for num in range(number_to_move):
            stack_dict[move_to].append(stack_dict[move_from].pop())

    print("Part 1: " + stack1[-1] + stack2[-1] + stack3[-1] + stack4[-1]
          + stack5[-1] + stack6[-1] + stack7[-1] + stack8[-1]
          + stack9[-1])


def part2(input):
    stack1, stack2, stack3, stack4, stack5,\
    stack6, stack7, stack8, stack9 = generate_input()

    for i in input:
        number_to_move = int(i.split(' ')[1])
        move_from = i.split(' ')[3]
        move_to = i.split(' ')[5]

        stack_dict = {'1': stack1, '2': stack2, '3': stack3, '4': stack4,
                      '5': stack5, '6': stack6, '7': stack7, '8': stack8,
                      '9': stack9}

        temp = stack_dict[move_from][-number_to_move:]
        del stack_dict[move_from][-number_to_move:]

        for element in temp:
            stack_dict[move_to].append(element)

    print("Part 2: " + stack1[-1] + stack2[-1] + stack3[-1] + stack4[-1]
          + stack5[-1] + stack6[-1] + stack7[-1] + stack8[-1]
          + stack9[-1])


if __name__ == "__main__":
    main()

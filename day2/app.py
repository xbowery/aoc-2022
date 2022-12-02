part1_scoreboard = {'X': {'A': 4, 'B': 1, 'C': 7},
                    'Y': {'A': 8, 'B': 5, 'C': 2},
                    'Z': {'A': 3, 'B': 9, 'C': 6}}
part2_scoreboard = {'A': {'X': 3, 'Y': 4, 'Z': 8},
                    'B': {'X': 1, 'Y': 5, 'Z': 9},
                    'C': {'X': 2, 'Y': 6, 'Z': 7}}


def main():
    # Read file
    file = open("input.txt").readlines()

    # Regex to filter out file input
    input = [r.strip('\n\r') for r in file]

    part1_points = 0
    part2_points = 0

    for i in input:
        opponent_choice = i.split(' ')[0]
        my_choice = i.split(' ')[1]
        part1_points += part1_sum_points(opponent_choice, my_choice)
        part2_points += part2_sum_points(opponent_choice, my_choice)

    print(f"Part 1 - Points: {part1_points}")
    print(f"Part 2 - Points: {part2_points}")


def part1_sum_points(opponent_choice, my_choice):
    return part1_scoreboard[my_choice][opponent_choice]


def part2_sum_points(opponent_choice, my_choice):
    return part2_scoreboard[opponent_choice][my_choice]


if __name__ == "__main__":
    main()

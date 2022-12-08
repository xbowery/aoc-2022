# import numpy

# def main():
#     f = open("input.txt").readlines()

#     input = [r.strip("\n\r") for r in f]

#     custom_list = []
#     boolean_list = []

#     length = len(input)

#     for i in range(length):
#         new_cust_list = []
#         new_boolean_list = []
#         for j in range(length):
#             new_cust_list.append(int(input[i][j]))
#             if i == 0 or i == length - 1 or j == 0 or j == length - 1:
#                 new_boolean_list.append(True)
#             else:
#                 new_boolean_list.append(False)
#         custom_list.append(new_cust_list)
#         boolean_list.append(new_boolean_list)

#     part1(custom_list, boolean_list, length)
#     part2(custom_list, length)


# def part1(custom_list, boolean_list, length):
#     count = 1

#     for i in range(length):
#         new_list = []
#         for j in range(length):
#             if i == 0 or i == length - 1 or j == 0 or j == length - 1:
#                 new_list.append(custom_list[i][j])

#     while count <= length // 2:
#         for i in range(count, length-count):
#             for j in range(count, length-count):
#                 if custom_list[i][j] == 0:
#                     boolean_list[i][j] = False
#         count += 1

#     # Top Approach
#     curr_max = []
#     for i in range(1, length-1):
#         curr_max.append(custom_list[0][i])

#     for i in range(1, length-1):
#         for j in range(1, length-1):
#             if (custom_list[i][j] > curr_max[j-1]):
#                 curr_max[j-1] = custom_list[i][j]
#                 boolean_list[i][j] = True

#     # Left Approach
#     curr_max = []
#     for i in range(1, length-1):
#         curr_max.append(custom_list[i][0])

#     for i in range(1, length-1):
#         for j in range(1, length-1):
#             if (custom_list[i][j] > curr_max[i-1]):
#                 curr_max[i-1] = custom_list[i][j]
#                 boolean_list[i][j] = True

#     # Bottom Approach
#     curr_max = []
#     for i in range(1, length-1):
#         curr_max.append(custom_list[-1][i])

#     for i in range(1, length-1):
#         for j in range(1, length-1):
#             if (custom_list[-i][j] > curr_max[j-1]):
#                 curr_max[j-1] = custom_list[-i][j]
#                 boolean_list[-i][j] = True

#     # Right Approach
#     curr_max = []
#     for i in range(1, length-1):
#         curr_max.append(custom_list[i][-1])

#     for i in range(1, length-1):
#         for j in range(1, length-1):
#             if (custom_list[i][-j] > curr_max[i-1]):
#                 curr_max[i-1] = custom_list[i][-j]
#                 boolean_list[i][-j] = True

#     result = 0
#     for i in range(length):
#         for j in range(length):
#             if (boolean_list[i][j] == True):
#                 result += 1

#     print("Part 1:", result)


def build_tree_view(row, col, inp, is_part1):
    curr_height = inp[row][col]
    top = [curr_height > line[col] for line in inp[:row]]
    bottom = [curr_height > line[col] for line in inp[row + 1:]]
    left = [curr_height > inp[row][i] for i in range(col)]
    right = [curr_height > inp[row][i] for i in range(col + 1, len(inp[row]))]

    if is_part1:
        return check_visible(top, bottom, left, right)
    else:
        return check_score(top, bottom, left, right)


def check_visible(top, bottom, left, right):
    return all(top) or all(bottom) or all(left) or all(right)


def check_score(top, bottom, left, right):
    top_scene = top[::-1].index(False) + 1 if False in top else len(top)
    bottom_scene = bottom.index(False) + 1 if False in bottom else len(bottom)
    left_scene = left[::-1].index(False) + 1 if False in left else len(left)
    right_scene = right.index(False) + 1 if False in right else len(right)

    return top_scene * bottom_scene * left_scene * right_scene


def part1(inp):
    # Start off with the outer layer
    p1_result = len(inp) * 2 + len(inp[0]) * 2 - 4

    for i in range(1, len(inp) - 1):
        for j in range(1, len(inp[0]) - 1):
            if build_tree_view(i, j, inp, True):
                p1_result += 1

    return p1_result


def part2(inp):

    p2_result = 0

    for i in range(1, len(inp) - 1):
        for j in range(1, len(inp[0]) - 1):
            p2_result = max(p2_result, build_tree_view(i, j, inp, False))

    return p2_result


def main():
    inp = open("input", "r").read().splitlines()

    for i, row in enumerate(inp):
        inp[i] = [int(char) for char in row]

    p1_result = part1(inp)
    print(f"Part 1: {p1_result}")

    p2_result = part2(inp)
    print(f"Part 2: {p2_result}")


if __name__ == "__main__":
    main()

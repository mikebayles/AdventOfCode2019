with open('day2.txt') as f:
    content = f.readlines()[0]
original_input = list(map(lambda x: int(x), content.split(',')))


def part1(input):
    i = 0
    while True:
        if input[i] == 99:
            break
        elif input[i] == 1:
            input[input[i + 3]] = input[input[i + 1]] + input[input[i + 2]]
            i += 4
        elif input[i] == 2:
            input[input[i + 3]] = input[input[i + 1]] * input[input[i + 2]]
            i += 4

    return input[0]


def part2():
    while True:
        for i in range(99):
            for j in range(99):
                this_try = original_input.copy()
                this_try[1] = i
                this_try[2] = j
                if part1(this_try) == 19690720:
                    return this_try

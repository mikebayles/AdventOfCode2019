with open('day1.txt') as f:
    content = f.readlines()


def part1():
    sum = 0
    for line in content:
        mass = int(line)

        sum += ((mass // 3) - 2)

    print(sum)


def part2():
    sum = 0
    for line in content:
        mass = int(line)

        sum += process(mass)

    print(sum)


def process(mass):
    if mass <= 0:
        return 0

    required = ((mass // 3) - 2)
    if required <= 0:
        return 0

    return required + process(required)

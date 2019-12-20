import sys
from collections import defaultdict

with open('day3.txt') as f:
    content = f.readlines()


def part1():
    points = defaultdict(int)
    intersects = []
    allowIntersections = False
    for line in content:
        x = 0
        y = 0

        commands = line.strip().split(',')
        for command in commands:
            distance = int(command[1:])
            for i in range(distance):
                if command[0] == 'U':
                    y += 1
                if command[0] == 'D':
                    y -= 1
                if command[0] == 'L':
                    x -= 1
                if command[0] == 'R':
                    x += 1

                key = f'{x},{y}'
                if points[key] and allowIntersections:
                    intersects.append((x, y))
                points[key] += 1

        allowIntersections = True

    answer = sys.maxsize
    for (x, y) in intersects:
        answer = min(answer, abs(x) + abs(y))

    print(answer)


def part2():
    points = defaultdict(int)
    intersects = []
    allowIntersections = False
    for line in content:
        x = 0
        y = 0

        totalSteps = 0

        commands = line.strip().split(',')
        for command in commands:
            distance = int(command[1:])
            for i in range(distance):
                totalSteps += 1
                if command[0] == 'U':
                    y += 1
                if command[0] == 'D':
                    y -= 1
                if command[0] == 'L':
                    x -= 1
                if command[0] == 'R':
                    x += 1

                key = f'{x},{y}'
                if points[key] and allowIntersections:
                    intersects.append((x, y, totalSteps + points[key]))
                points[key] = totalSteps

        allowIntersections = True

    answer = sys.maxsize
    for (x, y, totalSteps) in intersects:
        answer = min(answer, totalSteps)

    print(answer)

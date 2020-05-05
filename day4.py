from collections import defaultdict


def part1(min: int, max: int) -> int:
    ret = 0
    current = min
    while current <= max:
        previous = -1
        has_double = False
        decreased = False

        for c in str(current):
            if previous == c:
                has_double = True
            if int(c) < int(previous):
                decreased = True
                break
            previous = c

        if has_double and not decreased:
            ret += 1
        current += 1
    return ret


def part2(min: int, max: int) -> int:
    ret = 0
    current = min
    while current <= max:
        previous = -1
        decreased = False

        matches = defaultdict(int)

        for c in str(current):
            if previous == c:
                matches[c] += 1
            if int(c) < int(previous):
                decreased = True
                break
            previous = c

        has_double = len(list(filter(lambda v: v == 1, matches.values()))) > 0
        if not decreased and has_double:
            ret += 1
        current += 1
    return ret

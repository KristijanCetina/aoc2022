def part1(pair: list):
    score: int = 0
    for p in pair:
        elf, me = p[0], p[2]
        if me == "Y" and elf == "A":
            score += 6
        if me == "Z" and elf == "B":
            score += 6
        if me == "X" and elf == "C":
            score += 6

        if me == "Z" and elf == "C":
            score += 3
        if me == "X" and elf == "A":
            score += 3
        if me == "Y" and elf == "B":
            score += 3

        # scores for shape:
        if me == "X":
            score += 1
        if me == "Y":
            score += 2
        if me == "Z":
            score += 3
    return score


def part2(pair: list):
    score: int = 0
    for p in pair:
        elf, me = p[0], p[2]

        if me == "X" and elf == "B":
            score += 1
        if me == "Y" and elf == "A":
            score += 1
        if me == "Z" and elf == "C":
            score += 1

        if me == "X" and elf == "C":
            score += 2
        if me == "Y" and elf == "B":
            score += 2
        if me == "Z" and elf == "A":
            score += 2

        if me == "X" and elf == "A":
            score += 3
        if me == "Y" and elf == "C":
            score += 3
        if me == "Z" and elf == "B":
            score += 3

        if me == "X":
            score += 0
        if me == "Y":
            score += 3
        if me == "Z":
            score += 6
    return score


with open("input.txt", "r") as inputfile:
    pair = [d for d in inputfile.read().strip().split("\n")]

print(part1(pair))
print(part2(pair))

with open("input.txt", "r") as inputfile:
    items = [d for d in inputfile.read().strip().split("\n")]

alphabetValues = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,
                  'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52, }


commonItems = []
for item in items:
    first, second = item[:len(item)//2], item[len(item)//2:]
    commonItems.append(set(first) & set(second))

# print(commonItems)
score1 = 0
for c in commonItems:
    c = str(c).replace("'", "").replace("{", "").replace("}", "")
    score1 += (alphabetValues[c])

print(score1)


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


commonBadge = []
group = list(chunks(items, 3))
for g in group:
    commonBadge.append(set(g[0]) & set(g[1]) & set(g[2]))

score2 = 0
for c in commonBadge:
    c = str(c).replace("'", "").replace("{", "").replace("}", "")
    score2 += (alphabetValues[c])

print(score2)

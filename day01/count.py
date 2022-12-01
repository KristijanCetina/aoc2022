with open("input.txt", "r") as inputfile:
    calories = [d for d in inputfile.read().strip().split("\n\n")]

test = []
for cal in calories:
    a = 0
    t = (' '.join(cal.split("\n")))
    for x in cal.split("\n"):
        a += int(x)
    test.append(a)

print(max(test))
# print(test)
test.sort(reverse=True)
# print(test)
print(int(test[0])+int(test[1])+int(test[2]))

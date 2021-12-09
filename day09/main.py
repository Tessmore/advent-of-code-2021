
L = 0
heatmap = []

while True:
    try:
        line = [int(x) for x in input()]

        # Pad heatmap with 9s
        heat = [9] + line + [9]
        L = len(heat)

        heatmap.extend(heat)

    except EOFError:
        break

index = 0

# Pad 9s in top and bottom
heatmap = heatmap + (L*[9])
bigmap = (L*[9]) + heatmap + (L*[9])


# Part 1
total = []

for index, value in enumerate(heatmap, start = 0):
    if bigmap[index] == 9:
        continue

    me = bigmap[index]
    left = bigmap[index - 1]
    right = bigmap[index + 1]
    top = bigmap[index - L]
    bottom = bigmap[index + L]

    if me == left or me == right or me == top or me == bottom:
        continue

    lowest = min(me, left, right, top, bottom)

    if me == lowest:
        total.append(lowest + 1)

print("SUM", sum(total))

S = input()

counts = dict()
for s in S:
    if s in counts:
        counts[s] += 1
    else:
        counts[s] = 1
counts = list(counts.items())

all = 0
for i in range(len(counts)):
    for j in range(i+1,len(counts)):
        all += counts[i][1] * counts[j][1]

for i in range(len(counts)):
    if counts[i][1] > 1:
        all += 1
        break

print(int(all))
S = input()

if(len(set(S)) == 1):
    print(1)
    exit()

k = len(S)

all = k * (k - 1) // 2

counts = dict()
for s in S:
    if s in counts:
        counts[s] += 1
    else:
        counts[s] = 1

for key in counts:
    sub = counts[key] * (counts[key] - 1) // 2
    all -= sub

for key in counts:
    if counts[key] > 1:
        all += 1
        break

print(int(all))
N = int(input())

X = []
Y = []

for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

for i in range(N):
    maxDist = 0
    ans = -1
    for j in range(N):
        if i == j:
            continue
        dist = (X[i]-X[j])**2 + (Y[i]-Y[j])**2
        if maxDist < dist:
            maxDist = dist
            ans = j
    print(ans + 1)
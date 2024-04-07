N = int(input())

C = dict()

for i in range(N):
    a, c = map(int, input().split())

    if c in C:
        if C[c] > a:
            C[c] = a
    else:
        C[c] = a

max = 0

for k, v in C.items():
    if max < v:
        max = v

print(max)
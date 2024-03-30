N, A, B = list(map(int, input().split()))
D = list(map(int, input().split()))

S = A + B
D = list(map(lambda x: x % S, D))
Da = list(map(lambda x: x + S, D))
D.extend(Da)
D = sorted(list(set(D)))
# print(D)

res = False
for i in range(len(D)-1):
    if (D[i+1] - D[i] > B):
        res = True
        break

if (res):
    print("Yes")
else:
    print("No")
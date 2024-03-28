N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
L = int(input())
C = list(map(int, input().split()))
Q = int(input())
X = list(map(int, input().split()))

res = dict()

for a in range(len(A)):
    for b in range(len(B)):
        for c in range(len(C)):
            res[A[a]+B[b]+C[c]] = True

for i in range(len(X)):
    if X[i] in res:
        print("Yes")
    else:
        print("No")
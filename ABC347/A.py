N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

res = []
for i in range(N):
    if (A[i] % K == 0):
        res.append(A[i]//K)

print(*res)
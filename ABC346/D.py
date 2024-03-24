import sys

N = int(input())
S = input()
C = list(map(int, input().split()))

if N == 2:
    if S[0] != S[1]:
        print(min(C))
    else:
        print(0)
    exit()

dp01 = [0] * (N+1)
dp10 = [0] * (N+1)
dp01l = [0] * (N+1)
dp10l = [0] * (N+1)

for i in range(N):
    ck1 = "0" if i % 2 == 0 else "1"
    ck2 = "1" if i % 2 == 0 else "0"
    
    dp01[i+1]=dp01[i] + (C[i] if S[i] == ck2 else 0)
    dp10[i+1]=dp10[i] + (C[i] if S[i] == ck1 else 0)

# print(dp01)
# print(dp10)

ans = sys.maxsize
for i in range(1, N-1):
    cand1 = dp01[i] + dp10[-1] - dp10[i+1]
    cand2 = dp10[i] + dp01[-1] - dp01[i+1]
    ans = min(ans, cand1, cand2)

print(int(ans))


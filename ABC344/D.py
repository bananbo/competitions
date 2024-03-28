T = input()
N = int(input())

dp = [dict() for _ in range(N + 1)]
dp[0][""] = 0

for i in range(N):
    A = list(input().split())

    # 現在分
    items = list(dp[i].items())
    for k, v in items:
        current = k
        dp[i+1][current] = v

    # 次の分
    for j in range(1, len(A)):
        for k, v in items:
            next = k + str(A[j])
            if len(next) > 100:
                continue
            if T.find(next) == -1:
                continue
            if next not in dp[i+1]:
                dp[i+1][next] = v + 1
            else:
                dp[i+1][next] = min(v + 1, dp[i+1][next])

if T in dp[N]:
    print(dp[N][T])
else :
    print(-1)
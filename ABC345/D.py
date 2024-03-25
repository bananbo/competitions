N, H, W = list(map(int, input().split()))

if H > W:
    H, W = W, H

A, B = [], []
for i in range(N):
    a, b = list(map(int, input().split()))
    if a <= b:
        A.append(a)
        B.append(b)
    else:
        A.append(b)
        B.append(a)

# 三重の配列
dp = [[[0] * (21) for _ in range(21)] for _ in range(1<<N)]

for i in range(N):
    dp[1<<i][A[i]][B[i]] = 1
    dp[1<<i][B[i]][A[i]] = 1

for h in range(1, H+1):
    for w in range(1, W+1):
        for k in range(0, 1<<N): # 現在の使用したタイル
            if dp[k][h][w] == 0:
                continue
            for ka in range(0, 1<<N): # 追加したいタイル
                if k & ka != 0:
                    continue
                next = k | ka
                for ha in range(1, H+1):
                    if dp[ka][ha][w] != 0:
                        dp[next][h+ha][w] = max(dp[next][h+ha][w], dp[ka][ha][w])
                for wa in range(1, W+1):
                    if dp[ka][h][wa] != 0:
                        dp[next][h][w+wa] = max(dp[next][h][w+wa], dp[ka][h][wa])

ans = False
for i in range(0, 1<<N):
    if dp[i][H][W] == 1:
        ans = True
        break

# print(dp)

if ans:
    print("Yes")
else:
    print("No")

N, Q = list(map(int, input().split()))
x = list(map(int, input().split()))
x = [i-1 for i in x]

A = [0] * N
sums = [0] * (Q+1)

S = dict()
for i in range(Q):
    if x[i] in S:
        # 削除するケース
        # 結果を加算する
        sum = sums[i] - sums[S[x[i]]]
        A[x[i]] += sum
        
        S.pop(x[i])
    else:
        # 追加するケース
        S[x[i]] = i

    # 累積和用
    sums[i+1] = len(S) + sums[i]

for i in range(N):
    if i in S:
        sum = sums[Q] - sums[S[i]]
        A[i] += sum

print(*A)

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
A = filter(lambda x: x <= K, A)
A = list(set(A)) # N^2?

maxx = K * (1 + K) // 2
all = sum(A)

print(int(maxx - all))
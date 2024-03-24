N = input()
A = list(map(int, input().split()))

B = []
for i in range(len(A)-1):
    b = A[i] * A[i+1]
    B.append(b)


print(*B)
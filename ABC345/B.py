X = int(input())

ans = X // 10

if X % 10 > 0:
    ans += 1

print(ans)
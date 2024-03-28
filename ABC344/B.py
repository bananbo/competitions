res = []
while True:
    n = int(input())
    res.append(n)
    if n == 0:
        break

for i in range(len(res)):
    print(res[len(res) - i - 1])
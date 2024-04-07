N = int(input())

ret = ""

for i in range(1, N + 1):
    if i % 3 == 0:
        ret += "x"
    else:
        ret += "o"

print(ret)
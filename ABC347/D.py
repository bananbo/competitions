a, b, c = list(map(int, input().split()))

def popcount(x):
    return bin(x).count("1")

cp = popcount(c)
cc = []
for i in range(61):
    if 2**i & c == 2**i:
        cc.append(i)

resa = 0
resb = 0
ok = False
for k in range(61):
    kasanari = k
    tanpin_a = a - kasanari
    tanpin_b = b - kasanari
    if tanpin_a + tanpin_b == cp:
        ok = True
        break

if not ok or a + b < cp:
    print(-1)
    exit()

for i in range(61):
    if i in cc:
        if tanpin_a > 0:
            resa += 2**i
            tanpin_a -= 1
        elif tanpin_b > 0:
            resb += 2**i
            tanpin_b -= 1
    else:
        if kasanari > 0:
            resa += 2**i
            resb += 2**i
            kasanari -= 1
                
if tanpin_a > 0 or tanpin_b > 0 or kasanari > 0:
    print(-1)
    exit()
print(resa, resb)

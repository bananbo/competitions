H, W, M = list(map(int, input().split()))

T, A, X = [], [], []
for i in range(M):
    t, a, x = list(map(int, input().split()))
    T.append(t)
    A.append(a)
    X.append(x)

h = H
w = W
hdict = dict() # ある行における使われた行の数 
wdict = dict() # ある列における使われた列の数
colorDict = dict() # 結果を保存する辞書
for i in range(M):
    index = M - i - 1
    t = T[index]
    a = A[index]
    x = X[index]
    
    if t == 1:
        if a not in hdict:
            # 結果が追加される
            hdict[a] = 1
            if x in colorDict:
                colorDict[x] += w
            else:
                colorDict[x] = w
            h -= 1

    if t == 2:
        if a not in wdict:
            # 結果が追加される
            wdict[a] = 1
            if x in colorDict:
                colorDict[x] += h
            else:
                colorDict[x] = h
            w -= 1
s = 0
for item in colorDict:
    if item != 0:
        s += colorDict[item]

white = H * W - s
colorDict[0] = white
if white == 0:
    colorDict.pop(0)

colorDict = list(filter(lambda x: x[1] != 0, sorted(colorDict.items(), key=lambda x: x[0])))

print(len(colorDict))
for item in colorDict:
    print(item[0], item[1])
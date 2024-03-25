# 結構実装大変系かな？
# 最初の全探索方針は間違っていなかったが、面倒がって辞めてしまった。
# DP方式も悪くはなかったが、例外ケースが存在したので、見通しが甘かった。

import itertools

N, H, W = list(map(int, input().split()))

A, B = [], []
for i in range(N):
    a, b = list(map(int, input().split()))
    A.append(a)
    B.append(b)

permutations = list(itertools.permutations(range(N)))

def canPutTile(h, w, rot, tiles, currentBoard):
    if len(tiles) == 0:
        return False
    
    # currentBoard = [list(row) for row in currentBoard]
    tiles = list(tiles)
    nextTile = tiles.pop(0)

    # このタイルおける？
    a = A[nextTile]
    b = B[nextTile]
    if rot:
        a, b = b, a

    for i in range(a):
        for j in range(b):
            if currentBoard[h + i][w + j] == 1:
                return False
            
    for i in range(a):
        for j in range(b):
            currentBoard[h + i][w + j] = 1 # 書き込む

    hn, wn = -1, -1
    for i in range(h, H):
        for j in range(0, W):
            if currentBoard[i][j] == 0:
                hn, wn = i, j
                break
        if hn != -1:
            break

    if hn == -1 and wn == -1:
        return True

    # 横向きで置けるか？
    if canPutTile(hn, wn, False, tiles, currentBoard):
        return True
    
    # 縦向きで置けるか？
    if canPutTile(hn, wn, True, tiles, currentBoard):
        return True

    for i in range(a):
        for j in range(b):
            currentBoard[h + i][w + j] = 0 # 戻す
    return False
    

# 全探索
for perm in permutations:
    matrix = [[1] * (2*W+1) for _ in range(2*H+1)]
    for i in range(H):
        for j in range(W):
            matrix[i][j] = 0
    if canPutTile(0, 0, False, perm, matrix):
        print("Yes")
        exit()
    if canPutTile(0, 0, True, perm, matrix):
        print("Yes")
        exit()

print("No")

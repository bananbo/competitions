W, B = list(map(int, input().split()))

text = "wbwbwwbwbwbw" * 50

for i in range(len(text)):
    for j in range(i+1, len(text)):
        part = text[i:j]
        w_count = part.count("w")
        b_count = part.count("b")
        if w_count == W and b_count == B:
            print("Yes")
            exit()
print("No")
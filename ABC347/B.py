S = input()

types = dict()

for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        s = S[i:j]
        # print(s)
        types[s] = 1

print(len(types))


rect = []
with open(0) as f:
    for line in f:
        rect.append(line.strip('\n'))

XMAS = "XMAS"
h = len(rect)
w = len(rect[0])
count = 0
for i in range(h):
    for j in range(w):
        for di, dj in [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]:
            for k in range(4):
                l = i + k*di
                c = j + k*dj
                if 0 <= l < h and 0 <= c < w:
                    if rect[l][c] != XMAS[k]:
                        break
                else:
                    break
            else:
                #print(i,j,di, dj)
                count += 1

print(count)
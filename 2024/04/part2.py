

rect = []
with open(0) as f:
    for line in f:
        rect.append(line.strip('\n'))

h = len(rect)
w = len(rect[0])
count = 0
for i in range(1, h-1):
    for j in range(1, w-1):
        if rect[i][j] == 'A':
            if ((rect[i+1][j+1] == 'M' and rect[i-1][j-1] == 'S') or
                (rect[i+1][j+1] == 'S' and rect[i-1][j-1] == 'M')):
                if ((rect[i+1][j-1] == 'M' and rect[i-1][j+1] == 'S') or
                    (rect[i+1][j-1] == 'S' and rect[i-1][j+1] == 'M')):
                    count += 1

print(count)
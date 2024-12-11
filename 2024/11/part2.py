from math import log10
from functools import cache


inp = []
with open(0) as f:
    inp = list(map(int, f.read().strip().split()))

@cache
def blink(num, n):
    if n == 0:
        return 1
    
    if num == 0:
        return blink(1, n-1)

    size = int(log10(num))+1
    if size % 2 == 0:
        aux = 10**(size//2)
        left = num // aux
        right = num % aux
        return blink(left, n-1) + blink(right, n-1)
    
    return blink(num * 2024, n-1)

tot = 0
for x in inp:
    tot += blink(x, 75)

print(tot)
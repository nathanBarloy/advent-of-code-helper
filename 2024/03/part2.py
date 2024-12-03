import re

mul_re = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"

with open(0) as f:
    inp = f.read()

matches = re.findall(mul_re, inp)

tot = 0
enabled = True
for match in matches:
    if match == "do()":
        enabled = True
    elif match == "don't()":
        enabled = False
    elif enabled:
        a, b = tuple(map(int, match[4:-1].split(',')))
        tot += a*b


print(tot)
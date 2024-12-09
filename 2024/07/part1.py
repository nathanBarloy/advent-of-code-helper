from itertools import product

def compute(nums, ops):
    tot = nums[0]
    for i, op in enumerate(ops):
        num = nums[i+1]
        if op == 0:
            tot += num
        else:
            tot *= num
    return tot


with open(0) as f:
    tot = 0
    for line in f:
        goal, l = line.split(': ')
        goal = int(goal)
        l = list(map(int, l.split()))
        for ops in product([0,1], repeat=len(l)-1):
            if compute(l, ops) == goal:
                tot += goal
                break
    print(tot)
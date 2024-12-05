from functools import cmp_to_key

order = set()

def is_update_ok(update):
    for i, x in enumerate(update):
        for y in update[i+1:]:
            if (x,y) not in order:
                return False
    return True

def my_cmp(a, b):
    if (a,b) in order:
        return -1
    if (b,a) in order:
        return 1
    return 0

def sort_update(update):
    return sorted(update, key=cmp_to_key(my_cmp))
    

    
with open(0) as f:
    p1, p2 = f.read().split('\n\n')
    for line in p1.split('\n'):
        x, y = line.split('|')
        x = int(x)
        y = int(y)
        order.add((x,y))
    
    tot = 0
    for line in p2.split('\n'):
        pages = list(map(int, line.split(',')))
        if not is_update_ok(pages):
            ordered = sort_update(pages)
            tot += ordered[len(ordered)//2]
    
    print(tot)




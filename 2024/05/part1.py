
order = set()

def is_update_ok(update):
    for i, x in enumerate(update):
        for y in update[i+1:]:
            if (x,y) not in order:
                return False
    return True

    
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
        if is_update_ok(pages):
            tot += pages[len(pages)//2]
    
    print(tot)




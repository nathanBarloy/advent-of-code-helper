
def report_ok(rep):
    n = len(rep)
    if rep[0] < rep[1]:
        for i in range(n-1):
            if not (rep[i] < rep[i+1] <= rep[i] + 3):
                return False
        return True
    
    else:
        for i in range(n-1):
            if not (rep[i] > rep[i+1] >= rep[i] - 3):
                return False
        return True

with open(0) as f:
    tot = 0
    for line in f:
        report = list(map(int, line.split()))
        tot += report_ok(report)

print(tot)


def report_ok(rep):
    n = len(rep)
    if rep[0] < rep[1]:
        #print("asc")
        for i in range(n-1):
            if not (rep[i] < rep[i+1] <= rep[i] + 3):
                return i
        return -1
    
    else:
        #print("desc")
        for i in range(n-1):
            if not (rep[i] > rep[i+1] >= rep[i] - 3):
                return i
        return -1


def report_almost(rep):
    n = len(rep)
    if report_ok(rep[1:]) == -1:
        return True
    if report_ok([rep[0]]+rep[2:]) == -1:
        return True
    ierr = report_ok(rep)
    #print(ierr)
    del rep[ierr+1]
    return report_ok(rep)==-1



with open(0) as f:
    tot = 0
    for line in f:
        report = list(map(int, line.split()))
        res = report_almost(report)
        #print(res)
        tot += res

print(tot)

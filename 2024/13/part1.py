

with open(0) as f:
    inp_list = []
    for aux in f.read().split("\n\n"):
        inp = []
        lines = aux.split('\n')
        s, t = lines[0].split(", ")
        inp.append(int(s[12:]))
        inp.append(int(t[2:]))
        s, t = lines[1].split(", ")
        inp.append(int(s[12:]))
        inp.append(int(t[2:]))
        s, t = lines[2].split(", ")
        inp.append(int(s[10:]))
        inp.append(int(t[2:]))
        inp_list.append(inp)
    
    tot = 0
    for inp in inp_list:
        tot += solve(inp)
    print(tot)


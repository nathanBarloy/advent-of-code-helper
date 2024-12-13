

def solve(inp):
    a1, a2, b1, b2, c1, c2 = inp
    #print(a1, a2, b2, b2, c1, c2)
    det = b1*a2 - a1*b2
    aux = c1*a2 - a1*c2
    #print(det, aux)
    if det == 0:  # The 2 equations are colinear
        if aux == 0:  # The results are OK
            # We must choose the optimal solution
            fact = a1 / a2
            raise NotImplementedError("oupsi")
        else:
            return 0
    else:
        if aux % det == 0:
            y = aux // det
        else:
            return 0  # y is not an integer
        aux2 = c1 - b1*y
        if aux2 % a1 == 0:
            x = aux2 // a1
        else:
            return 0  # x is not an integer
        
        if 0 <= x <= 100 and 0 <= y <= 100:
            return 3 * x + y
        else:
            # not in range
            return 0




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
        inp.append(int(s[9:]))
        inp.append(int(t[2:]))
        inp_list.append(inp)
    
    tot = 0
    for inp in inp_list:
        tot += solve(inp)
    print(tot)


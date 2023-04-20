def batata(l):
    for c in range(0, l):
        if c % 2 == 0:
            l[c] = 0
    print(l)

batata([1,2,3,4])
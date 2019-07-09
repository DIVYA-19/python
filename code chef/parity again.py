import numpy
T = int(input())
for _ in range(T):
    Q = int(input())
    S = set()
    for _ in range(Q):
        X = int(input())
        s = list(S)
        if X not in S:       
            for i in s:
                S.add(i^X)
        S.add(X)
        print(S)
        b = list(map(bin,S))
        print(b)
        parity = [sum(map(int,list(item[2:]))) for item in b]
        print(parity)
        odd = numpy.sum(numpy.array(parity)%2)
        even = len(parity) - odd
        print(even,odd)

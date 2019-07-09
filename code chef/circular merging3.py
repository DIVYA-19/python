import numpy as np
T = int(input())
for _ in range(T):
    N = int(input())
    A = np.array(sorted(list(map(int, input().split()))))

    m = [i for i in range(N-1,0,-1)]
    m.insert(0,N-1)
    print(m)
    m = np.array(m)
    res = m*A
    print(np.sum(res))

import numpy as np
from itertools import permutations
import numpy as np

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    m = [i for i in range(1,N)]
    m.append(N-1)
    print(m)
    pers = permutations(m)
    per = list(pers)
    per = np.array(per)
    final = per * np.array(A)
    res = np.min(np.sum(final,1))
    print(res)

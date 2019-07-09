import numpy as np
from itertools import permutations

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    score = float("inf")
    m = [i for i in range(N-1,0,-1)]
    m.insert(0,N-1)
    a_pers = permutations(A)
    pers = list(a_pers)
    for i in pers:
        current = np.sum(np.array(i)*np.array(m))
        score = min(score,current)
    print(score)
        
    

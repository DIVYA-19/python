T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    U = input()
    score = 0
    flag=0
    for i in range(N):
        if flag == 1:
            flag = 0
            continue
        if S[i] == U[i]:
            score +=1
        elif U[i] != S[i] and U[i] != 'N':
            flag = 1
    print(score)

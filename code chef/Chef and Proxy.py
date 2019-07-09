T = int(input())
for _ in range(T):
    D = int(input())
    S = input()
    p_count = list(S).count('P')
    per = (p_count / D) * 100
    count = 0
    if per >= float(75):
        print(count)
    else:
        k = 0
        for i in range(2,D-2):
            if S[i] == 'A':
                if (S[i-1]=='P' or S[i-2]=='P') and (S[i+1]=='P' or S[i+2]=='P'):
                    count += 1
                    p_count+=1
                    per = (p_count / D) * 100
                    if per >= float(75):
                        k = 1
                        break
        if k==1:
            print(count)
        else:
            print(-1)

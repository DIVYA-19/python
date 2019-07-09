T = int(input())
for _ in range(T):
    N,K = map(int,input().split())
    A = list(map(int,input().split()))

    for i in range(N-1):
        for j in range(i+1,N):
            if A[i] + A[j] == K:
                print("Yes")
                break
        else:
            continue
        break
    else:
        print("No")
    
                

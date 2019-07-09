import numpy
T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    #for i in range(N):
     #   if A[i]%2==0:
      #      for j in range(i+1,N):
       #         if A[j]%2==1:
        #            count+=1

    b = numpy.array(A)%2
    for i in range(N):
        if b[i]==0:
            count+=numpy.sum(b[i+1:])
    
    print(count)
            

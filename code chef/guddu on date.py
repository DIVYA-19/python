T = int(input())
for _ in range(T):
    N = input()
    sum = 0
    for i in N:
        sum += int(i)
    print(N,end='')
    if sum%10:
        print(10-(sum%10))
    else:
        print('0')

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    m = sum(A)/N
    if m in A:
        print(A.index(m)+1)
    else:
        print("Impossible")

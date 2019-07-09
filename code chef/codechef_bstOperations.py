#2*p 2*p+1
N = int(input())
l= [None for _ in range(N*2)]
for j in range(N):
    i,x = input().split()
    if i == 'i':
        if all([v == None for v in l]):
            l[0] = int(x)
            print(1)
        else:
            child = 0
            while(l[child]!=None):
                if int(x)<l[child]:
                    child = ((child+1)*2)-1
                else:
                    child = ((child+1)*2)
            l[child] = int(x)
            print(child+1)
        print(l)
    else:
        for k in range(len(l)):
            if l[k] == int(x):
                node = k
                while (True):   #
                    print(node)
                    if l[(node+1)*2]!=None:
                        l[node] = l[(node+1)*2]
                        node = (node+1)*2
                    elif l[((node+1)*2)-1] != None:
                        l[node] = l[((node+1)*2)-1]
                        node = ((node+1)*2)-1
                    elif (l[(node+1)*2]==None and l[(node+1)*2-1]==None):
                        l[node] = None
                        break
        print(l)

n = input()

while(n != '#'):
    n = int(n)

    temp = 0
    track = '9'
    mem = []
    i = 1
    #mem.append(int(track))
    #temp += int(track) * i
    ne = 0

    while(temp<n):
        ne = int(track) - sum(mem)
        mem.append(int(ne))
        temp += int(ne) * i
        i+=1
        track += '9'

    temp -= int(ne) * (i-1)
    rem = n-temp
    rem = rem/(i-1)
    if int(rem) == rem:
        print(int(sum(mem[:-1])+rem))
    else:
        print("Impossible!")
    n = input()

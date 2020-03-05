n = 5
a = [1,2,3,4,5]

noOfSubs = 1 << n

subs = []

for i in range(0,noOfSubs):
    pos = n-1
    bit = i
    temp = []
    while(bit>0):
        if bit & 1 == 1:
            temp.append(a[pos])
            pass
        bit >>= 1
        pos -= 1
    subs.append(temp)
print(subs)
    
    

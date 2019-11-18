i = int(input())

#i did two approaches

#recursion
def palindrome(p,i,j):
    if(j>i):
        return
    if(int(p)==0):
        print(1)
    else:
        print(p+str(j)+p[::-1])
    palindrome(str(int(p)*10+j),i,j+1)
palindrome('0',i,1)

#loop
val = ''
for j in range(1,i+1):
    print(val+str(j)+val[::-1])
    val = val+str(j)

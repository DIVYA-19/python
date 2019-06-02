import re
s1 = "I am waiting"
s2 ="I have been waiting"
re_s = re.compile(r'(\S+)')
s1 = re_s.split(s1)
s2 = re_s.split(s2)

memo = [[-1] * len(s2) for _ in range(len(s1))]

def LSS(s1,s2,i1,i2,memo): #Longest Sub Sequence
    if i1 == len(s1) or i2 == len(s2):
        return ''
    if memo[i1][i2] != -1:
        return memo[i1][i2]
    if s1[i1] == s2[i2]:
        memo[i1][i2] = s1[i1] + LSS(s1,s2,i1+1,i2+1,memo)
        return memo[i1][i2]
    resultA = LSS(s1,s2,i1+1,i2,memo)
    resultB = LSS(s1,s2,i1,i2+1,memo)
    if len(resultA) > len(resultB):
        memo[i1][i2] = resultA
        return resultA
    else:
        memo[i1][i2] = resultB
        return resultB

res = LSS(s1,s2,0,0,memo)
print(res)

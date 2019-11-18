import re

t = int(input())


exp = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'

for i in range(t):
    email = input()

    if re.match(exp,email)!=None:
        print(email)
    

import math
t = int(input())
month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
leap_days = [31,29,31,30,31,30,31,31,30,31,30,31]
def leap(year):
    if (year%4 == 0 and year%100 != 0) or year%400 ==0:
        return True
    return False
for _ in range(t):
    year,month,day = list(map(int,input().split(':')))
    o_month = month
    o_day = day
    if leap(year):
        month_days[1] = 29
    else:
        month_days[1] = 28
    current_day = day
    current_month = month
    if current_day%2==0:
        check = 0
    else:
        check = 1
    count = 1           
    if current_day == month_days[month-1]:
        month += 1
        current_day = 2

    while(current_day<=month_days[month-1]):
        if current_day%2 == check:
            count +=1
        else:
            break         
        if current_day == month_days[month-1]:
            month += 1
            current_day = 2
        current_day +=2
    print(count)
    count = 0
    while(True):
        count = count + math.floor((month_days[o_month-1]-o_day)/2 + 1)
        if count != (month_days[o_month-1]-o_day)/2 + 1:
            if o_day%2 == 1:
                o_day = 1
                o_month += 1
            else:
                break
        else:
            if o_day%2 == 0:
                o_day = 2
                o_month += 1
            else:
                break
    print(count)
        
                
    

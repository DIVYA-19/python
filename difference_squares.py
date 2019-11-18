i = int(input())

a = [*range(1,i+1)]

sum_of_squares = sum([num*num for num in a])

sqaure_of_sum = sum(a)**2

dif = sqaure_of_sum - sum_of_squares

print(dif)



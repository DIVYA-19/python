

def secondLargest(nums):
    #initialize values to zero: helps for comparision
    first = 0
    second = 0

    for i in nums:
        #we compare current element with first
        #if it's bigger, then we store current element in first
        #and store value in first to second
        if first < i:
            second = first
            first = i
    return second

if __name__ == "__main__":
    #taking input eg: 2 3 4
    #split() splits the input t ' ' to list
    #input always takes string, So convert str to int using map
    #then convert map to list
    nums = list(map(int, input().split()))
    
    print('second largest: ', secondLargest(nums))
   

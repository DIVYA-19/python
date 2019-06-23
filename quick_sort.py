data = [1,2,4,8,4,3,6,3]

def QuickSort(data):
    if len(data) < 1:
        return data
    pivot = data[0]
    left = []
    right = []

    for i in data[1:]:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)
    return QuickSort(left) + [pivot] + QuickSort(right)

data = QuickSort(data)
print(data)

l = [2,2,5,50,1]
single = list(set(l))
frequencies = []
for i in single:
    frequencies.append(l.count(i))
m = min(frequencies)
ma = 0
for i in range(len(single)):
    if frequencies[i] == m and ma<single[i]:
        ma = single[i]
print(ma)

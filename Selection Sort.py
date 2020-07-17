array = [12, 11, 13, 5, 6, 7]

for i in range(0, len(array)-1):
    j = i+1
    while(j < len(array)):
        if array[i] >= array[j]:
            array[j], array[i] = array[i], array[j]
        j += 1

print(array)
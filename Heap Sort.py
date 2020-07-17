def Heapify(a, n, i):
    largest = i
    l = 2*i 
    r = 2*i + 1
    if (l <= n-1 and a[l] > a[i]):
        largest = l
    if (r <= n-1 and a[r] > a[largest]):
        largest = r
    if (largest != i):
        a[largest], a[i] = a[i], a[largest]
        Heapify(a, n, largest)


array = [12, 11, 13, 5, 6, 7]
for i in range(0, len(array)//2):
    Heapify(array, len(array), i)

print()


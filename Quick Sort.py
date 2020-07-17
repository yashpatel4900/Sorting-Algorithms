def QuickSort(A, p, i, j):
    e = j
    while i < j:
        while A[i] <= A[p] and i < e:
            i += 1
        else:
            if i<e and A[i] <= A[p]:
                i += 1
        
        while A[j] > A[p] and j > 0:
            j -= 1
        else:
            if j>0 and A[j] > A[p]:
                j -= 1

        if i<j:
            A[i], A[j] = A[j], A[i]

        if i >= j:
            A[p], A[j] = A[j], A[p]
            QuickSort(A, p, p, j-1)
            QuickSort(A, i, i, len(A)-1)


A = [12, 11, 13, 5, 6, 7,-3,7,10,93,-100]
QuickSort(A, 0, 0, len(A)-1)
print(A)

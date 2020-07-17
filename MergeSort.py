def Merge(A, i, mid, j):
    s=i
    s1=mid+1
    e=j
    C=[]
    while i <= mid and s1 <= j:
        if A[i] <= A[s1]:
            C.append(A[i])
            i += 1
        else:
            if A[i] > A[s1]:
                C.append(A[s1])
                s1 += 1
    else:
        while i <= mid:
            C.append(A[i])
            i += 1
        while s1 <= j:
            C.append(A[s1])
            s1 += 1

    counter=0
    for x in range(s,e+1):
        if counter<len(C):
            A[x]=C[counter]
            counter+=1


def MergeSort(A, i, j):
    if i < j:
        mid = (i+j)//2
        MergeSort(A, i, mid)
        MergeSort(A, mid+1, j)
        Merge(A, i, mid, j)


A = [12, 11, 13, 5, 6, 7, -3, 7, 10, 93, -100]
MergeSort(A, 0, len(A)-1)
print(A)
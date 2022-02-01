#shellsort function
def shellsort(arr):
    gap = len(arr)//2

    while gap>0:
        for i in range(gap, len(arr)):
            anchor = arr[i]
            j = i
            while j>=gap and arr[j-gap] > anchor:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor 
        gap = gap//2

#applying shellsort to list
elements = [89,78,61,53,23,21,17,12,9,7,6,2,1]
shellsort(elements)
print(elements)

#shellsort function
#function to sort a list using shell sort
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
print("Original list:")
print(elements)
shellsort(elements)
print("Sorted List:")
print(elements)

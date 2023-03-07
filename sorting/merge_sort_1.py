def merge_sort(arr, p, r):
    """Merge sort given unsorted list
    Args:
        arr: unsorted list
        p: start index
        r: last index
    """
    if p<r:
        mid = (p+r) // 2            # () is necessary, otherwise it will give RecursionError
        merge_sort(arr, p, mid)
        merge_sort(arr, mid+1, r)
        merge(arr, p, mid, r)
    

def merge(arr, p, mid, r):
    """Merge two sorted sublist
    Args:
        arr: sorted list
        p: start index
        mid: middle index
        r: last index
    """

    # arr is divided into list
    L = arr[p: mid+1]
    R = arr[mid+1: r+1] 
    # indexes
    i = 0
    j = 0
    k = p

    # merging of two sorted sublists
    while i<len(L) and j<len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i +=1
        else:
            arr[k] = R[j]
            j +=1
        k += 1

    # putting back remaing elements
    while i<len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j<len(R):
        arr[k] = R[j]
        j += 1
        k += 1

# now arrary(arr) is sorted so printing them
def get_sorted_list(arr):
    sorted_list = []
    for i in range(len(arr)):
        sorted_list.append(arr[i])
    return sorted_list
        
if __name__ == "__main__":
    arr = [43, 5, 39, 33, 90, 22, 30, 32, 44, 53]
    n = len(arr)
    merge_sort(arr, 0, n-1)

    result = get_sorted_list(arr)
    print(result)

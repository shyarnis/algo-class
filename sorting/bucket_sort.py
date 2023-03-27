# References:
#   CLRS 3e
#   https://www.programiz.com/dsa/bucket-sort

def bucket_sort(A):
    bucket = []
    n = len(A)
    
    # create empty buckets
    bucket = [[] for _ in range(n)]
    
    # insert elements into their respective buckets
    for i in A:
        index = int(10 * i)
        bucket[index].append(i)
    
    # sort elements of each bucket
    for i in range(n):
        bucket[i].sort()

    # get the sorted elements
    k = 0
    for i in range(n):
        for j in range(len(bucket[i])):
            A[k] = bucket[i][j]
            k += 1
    
    return A


if __name__ == "__main__":
    A = [.78, .17, .39, .26, .72, .94, .21, .12, .23, .68]
    bucket_sort(A)
    print(A)

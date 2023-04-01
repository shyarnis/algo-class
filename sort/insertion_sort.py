def insertion_sort(array):
    n = len(array)
    for j in range(1, n):
         
        key = array[j]
        i = j-1
        
        while i>=0 and array[i]>key:
            array[i+1] = array[i]
            i = i-1
        
        array[i+1] = key
        
    return array

# input
input_array = [5, 4, 3, 2, 1]

# ouput
print(insertion_sort(input_array))
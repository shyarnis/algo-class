import random

def get_random_array():
    random_array = []
    for _ in range(1_000):
        random_array.append(random.randint(10_000, 50_000))
    return random_array

def insertion_sort(array):
    for j in range(1, len(array)):
        
        key = array[j]
        i = j-1
        
        while i>=0 and array[i]>key:
            array[i+1] = array[i]
            i = i-1
        
        array[i+1] = key
        
    return array

unsorted_array = get_random_array()
sorted_array = insertion_sort(unsorted_array)

print(sorted_array)
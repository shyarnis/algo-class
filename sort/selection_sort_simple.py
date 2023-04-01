def selection_sort(array):
    length = len(array)
    for i in range(length-1):
        # index of minimum element
        minimum_index = i  

        # find minimum element index in unsorted sublist(right tira ko)
        for j in range(i+1, length):
            if array[j] < array[minimum_index]:
                minimum_index = j
        # endfor

        # swapping of minimum elements
        temp = array[i]
        array[i] = array[minimum_index]
        array[minimum_index] = temp
    # endfor

    return array


if __name__ == "__main__":
    input_array = [12, 30, 42, 12, 22, 56, 21]
    print(selection_sort(input_array))
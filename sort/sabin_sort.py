import random as rnd 
import time as time 
 
def rndNumGenerator(): 
    randomNumbers = [] 
 
    rnd.seed(time.time()) 
    for x in range(100): 
        randNum = rnd.randint(1, 1000) 
        randomNumbers.append(randNum) 
 
    return randomNumbers 
 
def insertionSort(listToSort): 
    sortedList = listToSort 
    for j in range(2, len(listToSort)): 
        key = listToSort[j] 
        i=j-1 
        while i>=0 and listToSort[i] > key: 
            listToSort[i+1] = listToSort[i] 
            i=i-1 
        listToSort[i+1]=key 
 
    return sortedList 
 
def selectionSort(listToSort): 
    sortedList = listToSort 
    for i in range(1, len(listToSort) - 1): 
        m = i 
        for j in range(i + 1, len(listToSort)): 
            if(sortedList[j] < sortedList[m]): 
                m=j 
            
            temp = sortedList[i] 
            sortedList[i] = sortedList[m] 
            sortedList[m] = temp 
    return sortedList 
 
def printList(listToPrint): 
    for i in listToPrint: 
        print(i) 
 
# def main(): 
randomList = rndNumGenerator() 
 
print("** Random Numbers ****") 
printList(randomList) 
 
startTime = time.time() 
sortedList = insertionSort(randomList) 
endTime = time.time() 
totalTimeInsertionSort = endTime - startTime 
print("** Sorted Numbers (insertion sort) ****") 
printList(sortedList) 
print("Total time taken: (Insertion Sort)", totalTimeInsertionSort, " ms") 
 
 
 
startTime = time.time() 
sortedList = selectionSort(randomList) 
endTime = time.time() 
totalTimeSelectionSort = endTime - startTime 
print("** Sorted Numbers (selection sort) ****") 
printList(sortedList) 
print("Total time taken: (Selection Sort)", totalTimeSelectionSort, " ms") 
 
 
# if name == "main": 
# main()
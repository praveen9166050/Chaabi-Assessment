# Q1. Implement selection sort algorithm in python. The function accepts a
# list in the input and returns a sorted list.

def selectionSort(arr):
    for i in range(len(arr) - 1):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

arr = [5,416,54,21,6135,15,741]
print(selectionSort(arr))
def bubble_sort(arr: list):
    while 1 == 1:
        swap_count = 0
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                swap_count += 1 
        if swap_count == 0:
            break
    return arr

def selection_sort(arr: list):
    for i in range(len(arr)):
        min = arr[i]
        min_idx = i
        for j in range(i, len(arr)):
            if arr[j] < min:
                min = arr[j]
                min_idx = j
        arr[i], arr[min_idx] = min, arr[i]
    return arr

def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

def quick_sort(arr: list):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less_than_pivot = [x for x in arr[1:] if x <= pivot]
    greater_than_pivot = [x for x in arr[1:] if x > pivot]
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)
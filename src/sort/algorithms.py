from typing import List
import random



def in_order(arr: List[int]) -> bool:
    return all([arr[i] <= arr[i+1] for i in range(len(arr)-1)])

def bogo_sort(arr: List[int]) -> List[int]:
    while not in_order(arr):
        random.shuffle(arr)
    return arr



def bubble_sort(arr: List[int]) -> List[int]:
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr



def cocktail_sort(arr: List[int]) -> List[int]:
    len_arr = len(arr)
    swapped = True
    start = 0
    end = len_arr - 1

    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        
        if not swapped:
            break

        swapped = False
        end -= 1
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        start += 1
    
    return arr



def comb_sort(arr: List[int]) -> List[int]:
    COMB_SORT_COSTANT = 1.3
    len_arr = len(arr)
    gap = len_arr
    swapped = True

    while gap != 1 or swapped:
        gap = int(gap / COMB_SORT_COSTANT) if int(gap / COMB_SORT_COSTANT) >= 1 else 1

        swapped = False

        for i in range(0, len_arr - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
    return arr



def selection_sort(arr: List[int]) -> List[int]:
    for i in range(len(arr)):
        min_idx = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr



def gnome_sort(arr: List[int]) -> List[int]:
    len_arr = len(arr)
    pointer = 0
    while pointer != len_arr - 1:
        if arr[pointer] > arr[pointer+1]:
            arr[pointer], arr[pointer+1] = arr[pointer+1], arr[pointer]
            pointer = pointer - 1 if pointer > 0 else pointer + 1
        pointer = pointer + 1
    return arr



def insertion_sort(arr: List[int]) -> List[int]:
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]



def bucket_sort(arr: List[int]) -> List[int]:
    len_arr = len(arr)
    max = arr[0]
    for i in range(len_arr):
        max = arr[i] if arr[i] > max else max
    size = int(max / len_arr) if int(max / len_arr) != 0 else 1
    buckets = [[] for _ in range(size)]

    for num in arr:
        i = int(num / size)
        if i != size and size != 1:
            buckets[i].append(num)
        else:
            buckets[size-1].append(num)
    
    for i in range(size):
        insertion_sort(buckets[i])
        
    return arr



def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less_than_pivot = [x for x in arr[1:] if x <= pivot]
    greater_than_pivot = [x for x in arr[1:] if x > pivot]
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)
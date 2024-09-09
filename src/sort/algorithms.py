from typing import List
import random

def in_order(arr: List[int]) -> bool:
    return all([arr[i] <= arr[i+1] for i in range(len(arr)-1)])

def bongo_sort(arr: List[int]) -> List[int]:
    while not in_order(arr):
        random.shuffle(arr)
    return arr



def bubble_sort(arr: List[int]) -> List[int]:
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr



def selection_sort(arr: List[int]) -> List[int]:
    for i in range(len(arr)):
        min = arr[i]
        min_idx = i
        for j in range(i, len(arr)):
            if arr[j] < min:
                min = arr[j]
                min_idx = j
        arr[i], arr[min_idx] = min, arr[i]
    return arr



def insertion_sort(arr: List[int]) -> List[int]:
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]



def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less_than_pivot = [x for x in arr[1:] if x <= pivot]
    greater_than_pivot = [x for x in arr[1:] if x > pivot]
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)
from .modules import sort_test
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        value = arr[i]
        pointer = i - 1
        while pointer >= 0 and arr[pointer] > value:
            arr[pointer+1] = arr[pointer]
            pointer -= 1
        arr[pointer+1] = value
    return arr

start_time = time.time()
sort_test.test(insertion_sort)
end_time = time.time()

print(f'実行時間: {end_time - start_time}秒')
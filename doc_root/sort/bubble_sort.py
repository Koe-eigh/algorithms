from modules import sort_test
import time

def bubble_sort(arr: list):
    length: int = len(arr)
    for i in range(1, length):
        for j in range(1, length-i):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

start_time = time.time()
sort_test.test(bubble_sort)
end_time = time.time()
print(f'実行時間: {end_time - start_time}秒')
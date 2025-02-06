from modules import sort_test
import time

def selection_sort(arr):
    arr_length = len(arr)
    for i in range(arr_length):
        min_index = i
        for j in range(i+1, arr_length):
            if arr[j] < arr[min_index]:
                arr[j], arr[min_index] = arr[min_index], arr[j]
    return arr

start_time = time.time()
sort_test.test(selection_sort)
end_time = time.time()

print(f'所要時間: {end_time - start_time}秒')

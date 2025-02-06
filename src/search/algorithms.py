from typing import List

def linear_search(nums: List[int], value: int) -> int:
    for i in range(len(nums)):
        if nums[i] == value:
            return i
    return -1

def binary_search(nums: List[int], value: int) -> int:
    """
    int配列の中から値のindexを返します。値が存在しない場合は-1を返します。
    @params nums: List[int], value: int
    return index: int
    """
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == value:
            return mid
        elif nums[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    return -1
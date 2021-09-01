# 给定数组A 目标值T 查找T在A中位置
def binary_search(arr, key):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = int((start + end) / 2)
        if arr[mid] < key:
            start = mid + 1
        elif arr[mid] > key:
            end = mid - 1
        else:

            return mid

    return -1

list1 = [i for i in range(100)]
print(list1)
b = binary_search(list1, 5)


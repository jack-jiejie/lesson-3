__author__ = "yin"
__data__ = "2020/4/9 9:57"

def bubble(arr):
    # 循环多少次， 循环判断列表的长度
    for i in range(len(arr)):
        for j in range(0, len(arr)-1):
            # 比较相邻元素的大小
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


a = [1, 5, 2, 7, 0, 12, 6]
arr = bubble(a)
print(arr)




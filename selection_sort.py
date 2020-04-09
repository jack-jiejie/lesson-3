__author__ = "yin"
__data__ = "2020/4/9 10:12"

def selectionSort(arr):
    for i in range(0, len(arr)-1):
        # 记录最小的索引
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j


        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]

    return arr

a = [1, 5, 2, 7, 0, 12, 6]
arr = selectionSort(a)
print(arr)






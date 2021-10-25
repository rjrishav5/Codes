def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j-=1
        arr[j + 1] = key

    print(arr)

arr = [2,1,7,6,5,3,4,9,8]
insertion_sort(arr)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == 0:
            break


if __name__ == "__main__":
    arr = [9, 5, 8, 7, 4, 2, 6, 11, 21, 13, 19, 12]
    bubble_sort(arr)
    print(arr)

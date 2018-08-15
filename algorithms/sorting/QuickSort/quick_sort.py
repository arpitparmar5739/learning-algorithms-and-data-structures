from partition import partition


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)


if __name__ == "__main__":
    A = [9, 5, 8, 7, 4, 2, 6, 11, 21, 13, 19, 12]
    quick_sort(A, 0, len(A)-1)
    print(A)

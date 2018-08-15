def partition(A, p, r):
    x = A[r]
    i = p-1

    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[r], A[i+1] = A[i+1], A[r]
    return i+1


if __name__ == "__main__":
    A = [9, 5, 8, 7, 4, 2, 6, 11, 21, 13, 19, 12]
    partition(A, 0, len(A)-1)
    print(A)

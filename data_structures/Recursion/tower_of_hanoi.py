def move(x, y):
    A[x] -= 1
    A[y] += 1


def TOH(n, x, y, z):
    print(A)
    if n >= 1:
        # Move n-1 disks from tower x to tower y
        TOH(n-1, x, z, y)

        # Move the largest disk present at tower x to tower y
        move(x, y)

        # Move disks remaining (n-1) at tower z to tower y through tower of hanoi
        TOH(n-1, z, y, x)


n = int(input("Enter number of disks on first disks: "))
A = [n, 0, 0]   # Global array of tower and number of disks on them.
TOH(n, 0, 1, 2)

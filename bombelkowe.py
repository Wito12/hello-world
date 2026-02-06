def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
              
    return arr


przyklad1 = [64, 34, 25, 12, 22, 11, 90]

print("Przed sortowaniem:", przyklad1)
bubble_sort(przyklad1)
print("Po sortowaniu:", przyklad1)

przyklad2 = [5, 1, 4, 2, 8]

print("\nPrzed sortowaniem:", przyklad2)
bubble_sort(przyklad2)
print("Po sortowaniu:", przyklad2)

przyklad3 = [3, 0, 2, 5, -1, 4, 1]

print("\nPrzed sortowaniem:", przyklad3)
bubble_sort(przyklad3)
print("Po sortowaniu:", przyklad3)

from random import randint


def bin_search(arr, num, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == num:
        return mid
    elif arr[mid] < num:
        return bin_search(arr, num, mid + 1, high)
    else:
        return bin_search(arr, num, low, mid - 1)


try:
    arr = []
    for i in range(100):
        arr.append(randint(0, 100))
    print(arr)

    arr.sort()
    print(arr)

    num = int(input("Введите, что искать: "))
    res = bin_search(arr, num, 0, len(arr) - 1)

    if res != -1:
        print(f"Элемент найден и находится под индексом {res}")
    else:
        print("Элемент не найден")
except Exception as e:
    print(f"\n[-] Произошла ошибка: {e}")

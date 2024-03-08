from random import randint


def bin_search(arr, num, low, high):
    if low > high:
        return None

    mid = (low + high) // 2
    for i in range(len(arr[mid])):
        if arr[mid][i] == num:
            return (mid, i)
        elif arr[mid][i] < num:
            continue
        else:
            break
    if num > arr[mid][-1]:
        return bin_search(arr, num, mid + 1, high)
    elif num < arr[mid][0]:
        return bin_search(arr, num, low, mid - 1)


try:
    arr = []
    cols = 3
    rows = 10
    for i in range(rows):
        a = []
        for j in range(cols):
            a.append(randint(0, 100))
        arr.append(a)

    arr = [j for i in arr for j in i]
    arr.sort()
    matrix = []
    for i in range(rows):
        row = arr[i * cols : (i + 1) * cols]
        matrix.append(row)

    print(f"Отсортированный двумерный массив:  {matrix}")

    num = int(input("Введите, что искать: "))
    res = bin_search(matrix, num, 0, len(matrix) - 1)

    if res is not None:
        print(f"Элемент найден и находится под индексом {res}")
    else:
        print("Элемент не найден")
except Exception as e:
    print(f"\n[-] Произошла ошибка: {e}")

from random import randint
import time


def bubble_sort_asc(arr):
    size = len(arr)
    for i in range(size - 1):
        for j in range(size - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def bubble_sort_desc(arr):
    size = len(arr)
    for i in range(size - 1):
        for j in range(size - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def selection_sort_asc(arr):
    size = len(arr)
    for i in range(size - 1):
        lowest = i
        for j in range(i + 1, size):
            if arr[j] < arr[lowest]:
                lowest = j
        arr[i], arr[lowest] = arr[lowest], arr[i]


def selection_sort_desc(arr):
    size = len(arr)
    for i in range(size - 1):
        lowest = i
        for j in range(i + 1, size):
            if arr[j] > arr[lowest]:
                lowest = j
        arr[i], arr[lowest] = arr[lowest], arr[i]


def insertion_sort_asc(arr):
    size = len(arr)
    for i in range(1, size):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def insertion_sort_desc(arr):
    size = len(arr)
    for i in range(1, size):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def quick_sort_asc(arr):
    if len(arr) <= 1:
        return arr

    key = arr[len(arr) // 2]

    left = [x for x in arr if x < key]
    middle = [x for x in arr if x == key]
    right = [x for x in arr if x > key]

    return quick_sort_asc(left) + middle + quick_sort_asc(right)


def quick_sort_desc(arr):
    if len(arr) <= 1:
        return arr

    key = arr[len(arr) // 2]

    left = [x for x in arr if x > key]
    middle = [x for x in arr if x == key]
    right = [x for x in arr if x < key]

    return quick_sort_desc(left) + middle + quick_sort_desc(right)


arr = []
while True:
    try:
        chooseAlg = int(
            input(
                f"\n[?] Choose sorting algorithm: \n [1] Bubble Sort \n [2] Selection Sort \n [3] Insertion Sort \n [4] Quick Sort \n Enter: "
            )
        )
        if chooseAlg in range(1, 5):
            break
        else:
            print(f"\n[-] Sorry, I couldn't understand {chooseAlg}")
            time.sleep(1)
    except ValueError:
        print(f"\n[-] Enter Integer value!")
        time.sleep(1)
while True:
    try:
        chooseDir = int(
            input(
                f"\n[?] Choose sorting direction: \n [1] Ascending \n [2] Descending \n Enter: "
            )
        )
        if chooseDir in range(1, 3):
            break
        else:
            print(f"\n[-] Sorry, I couldn't understand {chooseDir}")
            time.sleep(1)
    except ValueError:
        print(f"\n[-] Enter Integer value!")
        time.sleep(1)
while True:
    try:
        size = int(input(f"\n[?] Select array length: "))
        for i in range(size):
            arr.append(randint(0, 99))
        break
    except ValueError:
        print(f"\n[-] Enter Integer value!")
        time.sleep(1)

    # case 2:
    #     arr = input("\n[?] Enter your values separated by spaces: ").split()

print(f"\n[+] Initial array: {arr}")

match chooseDir:
    case 1:
        match chooseAlg:
            case 1:
                bubble_sort_asc(arr)
            case 2:
                selection_sort_asc(arr)
            case 3:
                insertion_sort_asc(arr)
            case 4:
                arr = quick_sort_asc(arr)
    case 2:
        match chooseAlg:
            case 1:
                bubble_sort_desc(arr)
            case 2:
                selection_sort_desc(arr)
            case 3:
                insertion_sort_desc(arr)
            case 4:
                arr = quick_sort_desc(arr)
    case _:
        print(f"\n[-] An error occurred")
        time.sleep(1)
        exit()

print(f"[+] Array after sorting: {arr}")

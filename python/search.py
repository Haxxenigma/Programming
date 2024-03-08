from random import randint
import time


def linear_search(li, elem):
    for i in range(len(li)):
        if li[i] == elem:
            return i
    return None


li = []

for i in range(10):
    li.append(randint(0, 10))

while True:
    try:
        elem = int(
            input("\n[?] Enter element to find it's first occurrence in random array: ")
        )
        break
    except ValueError:
        print("\n[-] Enter Integer value!")
        time.sleep(1)

print(f"\n[+] List: {li}")
res = linear_search(li, elem)

if res != None:
    print(f"[+] Index of the first occurrence of the element: ", res)
else:
    print(f"[-] Index of the first occurrence of the element: ", res)

def translate(num, base):
    res = []
    hex_dict = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    while num > 0:
        res_piece = num % base
        if res_piece > 9 and base == 16:
            res.append(hex_dict[res_piece])
        else:
            res.append(res_piece)
        print(res_piece)
        num //= base
    return "".join([str(i) for i in res[::-1]])


try:
    num = int(input("Введите число: "))
    base = int(
        input("Введите, на какую систему счисления вы хотите перевести [2/8/16]: ")
    )

    print(f"\n[+] Преобразованный вид: {translate(num, base)}")
except Exception as e:
    print(f"\n[-] Произошла ошибка: {e}")

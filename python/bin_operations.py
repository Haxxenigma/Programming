def bin2list(bin1, bin2, max_len):
    bin1 = bin1.replace("0b", "")
    bin2 = bin2.replace("0b", "")

    bin1 = bin1.zfill(max_len)
    bin2 = bin2.zfill(max_len)

    bin1 = [int(i) for i in bin1]
    bin2 = [int(i) for i in bin2]

    return (bin1, bin2)


def list2bin(bin_list: list):
    return "".join([str(i) for i in bin_list])


def bin_sum(bin1: str, bin2: str):
    res = []
    max_len = max(len(bin1), len(bin2))

    bin1, bin2 = bin2list(bin1, bin2, max_len)

    for i in range(max_len):
        if bin1[-1 - i] == 1 and bin2[-1 - i] == 1:
            temp = [1, 0]
            if len(res) > i:
                if res[-1 - i] == 1:
                    res.insert(0, 1)
            else:
                res.insert(0, 0)
                res.insert(0, 1)
        else:
            temp = bin1[-1 - i] + bin2[-1 - i]
            if len(res) > i:
                if temp == 1 and res[-1 - i] == 1:
                    res.pop(-1 - i)
                    res.insert(0, 0)
                    res.insert(0, 1)
            else:
                res.insert(0, temp)

    return list2bin(res)


def bin_sub(bin1: str, bin2: str):
    res = []
    max_len = max(len(bin1), len(bin2))
    switched_places = False

    if int(bin1, 2) < int(bin2, 2):
        bin1, bin2 = bin2, bin1
        switched_places = True

    bin1, bin2 = bin2list(bin1, bin2, max_len)

    for _ in range(max_len):
        a = bin1.pop(-1)
        b = bin2.pop(-1)
        temp = a - b
        if temp == -1:
            for index, j in enumerate(bin1[-1::-1]):
                if j == 1:
                    bin1.insert(-1 - index, 0)
                    bin1.pop(-1 - index)
                    temp = 1
                    break
                else:
                    bin1.insert(-1 - index, 1)
                    bin1.pop(-1 - index)
        res.insert(0, temp)

    if switched_places:
        res.insert(0, "-")

    return list2bin(res)


def bin_mult(bin1, bin2):
    res = "0"

    for _ in range(int(bin2, 2)):
        temp = bin_sum("0", bin1)
        res = bin_sum(res, temp)

    return res


def bin_div(dividend, divisor):
    res = "0"

    while int(dividend, 2) >= int(divisor, 2):
        res = bin_sum(res, "1")
        dividend = bin_sub(dividend, divisor)

    return (res, dividend)


def main():
    num1 = bin(int(input("Enter number 1: ")))
    num2 = bin(int(input("Enter number 2: ")))

    sum_res = int(bin_sum(num1, num2), 2)
    sub_res = int(bin_sub(num1, num2), 2)
    mult_res = int(bin_mult(num1, num2), 2)
    div_res, remainder = bin_div(num1, num2)

    print("Addition result:", sum_res)
    print("Subtraction result:", sub_res)
    print("Multiplication result:", mult_res)
    print("Division result:", int(div_res, 2), "| Remainder: ", int(remainder, 2))


if __name__ == "__main__":
    main()

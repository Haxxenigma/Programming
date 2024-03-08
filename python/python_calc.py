cont = "y"
while cont.lower() == "y":
    num_a = int(input("Enter number a: "))
    num_b = int(input("Enter number b: "))
    operator = input("Choose operator (+, -, *, /): ")

    if operator == "+":
        res = num_a + num_b
    elif operator == "-":
        res = num_a - num_b
    elif operator == "*":
        res = num_a * num_b
    elif operator == "/":
        if num_b != 0:
            res = num_a / num_b
        else:
            print("Error: Division by zero")
            break
    else:
        print("Error: Invalid operator")
        break

    print(res)

    cont = input("Continue? (Y/N): ")

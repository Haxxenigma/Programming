import socket

with socket.socket() as client:
    client.connect(("localhost", 8080))
    file = input("Введите название файла: ")
    with open(file, "r") as f:
        data = f.read()

    client.sendall(data.encode())
    data = client.recv(1024).decode()

print(f"Количество слов в файле: {data}")

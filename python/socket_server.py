import socket

with socket.socket() as server:
    server.bind(("localhost", 8080))
    server.listen(1)
    while True:
        con, _ = server.accept()
        with con:
            data = con.recv(1024).decode()
            words = data.split()
            words_count = len(words)

            con.sendall(str(words_count).encode())

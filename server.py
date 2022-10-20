import socket
import threading

sock = socket.socket()
port = 5001

sock.bind(('localhost', port))
sock.listen(1)

def handle(connection, clients, id):
    while True:
        msg = connection.recv(1024).decode()
        print(f'Клиент {id}: {msg}\n')

        if msg == 'exit':
            clients.remove(connection)
            break
        else:
            for i in clients:
                if i != connection:
                    i.send((f'Клиент {id}: ' + msg).encode('utf-8'))

    print(f'Клиент {id} отключился!')
    connection.close()

clients = []
id = 0

try:
    while True:
        con, _ = sock.accept()

        print(f'Клиент ${id} подключен, ждем данных...')
        clients.append(con)

        threading.Thread(target=handle, args=(
            con, clients, id), daemon=True).start()

        print(f'Сейчас подключено клиентов: ${id}')
	id += 1


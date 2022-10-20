import socket, threading

def scanner(ip, port):
	test_sock = socket.socket()

	try:
		connection = test_sock.connect((ip, port))
		print(f"Порт :${port} открыт")
		connection.close()
	except:
		return

N = 2**16 - 1
ip = input("IP адресс для сканирования: ")

for i in range(N):
	thread = threading.Thread(target=scanner, args=(ip, i))
	thread.start()

import socket, threading

HEADER = 64
PORT = 5050
SERVER = "192.168.1.18"
ADDRESS = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

def receive(conn, addr):
	print(f"[NEW CONNECTION] {addr} connected.")

	while True:
		msg_length = conn.recv(HEADER).decode(FORMAT)
		if msg_length:
			msg_length = int(msg_length)
			msg = conn.recv(msg_length).decode(FORMAT)

			print(f"{addr}:  {msg}")
			print("\n\n>> ", end="")


def send(conn, msg):
	message = msg.encode(FORMAT)
	msg_length = len(message)
	send_length = str(msg_length).encode(FORMAT)
	send_length += b' ' * (HEADER - len(send_length))
	conn.send(send_length)
	conn.send(message)


def main():
	server.listen()
	print(f"[LISTENING] Server is listening on {SERVER}")
	conn, addr = server.accept()
	thread = threading.Thread(target=receive, args=(conn, addr))
	thread.start()
	while True:
		send(conn, input(">> "))
		

print("[STARTING] server is starting...")
main()

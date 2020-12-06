import socket, threading

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "71.232.76.201"
ADDR = (SERVER, PORT)


def receive():
	while True:
		msg_length = client.recv(HEADER).decode(FORMAT)
		if msg_length:
			msg_length = int(msg_length)
			msg = client.recv(msg_length).decode(FORMAT)

			print(f"[SERVER]: {msg}")
			print("\n\n>> ", end="")

def send(msg):
	message = msg.encode(FORMAT)
	msg_length = len(message)
	send_length = str(msg_length).encode(FORMAT)
	send_length += b' ' * (HEADER - len(send_length))
	client.send(send_length)
	client.send(message)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
thread = threading.Thread(target=receive)
thread.start()

while True:
	send(input(">> "))
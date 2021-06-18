from socket import *
import base64
import ssl
import getpass

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailServer = 'smtp.gmail.com'
mailPort = 587

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.settimeout(10)
clientSocket.connect((mailServer, mailPort))
recv = clientSocket.recv(1024)

print("After socket tries to connect: ", recv)
if recv[:3] != b'220':

	print('220 reply not received from server.')
print()

#identify herself to the receiver
clientSocket.send(b'EHLO smtp.google.com.\r\n')
recv1 = clientSocket.recv(1024)
print("After EHLO command: ", recv1)
if recv1[:3] != b'250':
	 print('250 reply not received from server.')
print()

#start a TLS connection
clientSocket.send(b'STARTTLS\r\n')
recv2 = clientSocket.recv(1024)
print("After STARTTLS: ", recv2)
print()

## WRAP SOCKET
clientSocket = ssl.wrap_socket(clientSocket, ssl_version=ssl.PROTOCOL_TLSv1_2, ciphers="AES256-SHA")

## AUTHENTICATION
userName = input("Insert username: ")
password = getpass.getpass(prompt= "Insert password: ")

clientSocket.send(('auth login\r\n').encode())
recv3 = clientSocket.recv(1024).decode()
print("After AUTH LOGIN: ", recv3)

clientSocket.send((base64.b64encode((userName).encode())) + ('\r\n').encode())
print(clientSocket.recv(1024).decode())

clientSocket.send((base64.b64encode((password).encode())) + ('\r\n').encode())
print(clientSocket.recv(1024).decode())

mailFrom = "MAIL FROM: <{}> \r\n".format(userName)
print(mailFrom)
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024)
recv2 = recv2.decode()
print("Message after MAIL FROM: ", recv2)

# Send RCPT TO command and print server response.

destinatary = input("Send to: ")
rcptTo = "RCPT TO: <{}>\r\n".format(destinatary)
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024)
recv3 = recv3.decode()
print("Message after RCPT TO: ", recv3)


# Send DATA command and print server response.

data = "DATA" + " \r\n"
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024)
recv4 = recv4.decode()
print("Message after DATA: ", recv4)

# Send message data

#Send subject
clientSocket.send(("Subject: Test with github!" + "\r\n").encode())
#send body
body = "Hello, I'm using my own mail client for this. You can check at github.com/luismomm2110/network-kurose \r\n"
clientSocket.send(body.encode())
# Message ends with a single period.

period = ".\r\n"
clientSocket.send(period.encode())

# Send QUIT command and get server response.

quit = "QUIT\r\n"
clientSocket.send(quit.encode())
recv6 = clientSocket.recv(1024)
recv6 = recv6.decode()
print("Message after quit: ", recv6)
clientSocket.close()

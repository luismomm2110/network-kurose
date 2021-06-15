from socket import *
import ssl

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailServer = 'smtp.gmail.com'
mailPort = 587

# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.settimeout(10)
clientSocket.connect((mailServer, mailPort))
print(clientSocket.recv(1024))

clientSocket.send(b'EHLO smtp.google.com.\r\n')
recv = clientSocket.recv(1024)

clientSocket.send(b'STARTTLS\r\n')
print(clientSocket.recv(1024))

## WRAP SOCKET
clientSocket = ssl.wrap_socket(clientSocket, ssl_version=ssl.PROTOCOL_SSLv23)
#Fill in end

#recv = clientSocket.recv(1024).decode()
#print(recv)

if recv[:3] != '220':

	print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)

if recv1[:3] != '250':
	 print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
# Fill in start
mailFrom = "MAIL FROM: luismomm@gmail.com\r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024)
recv2 = recv2.decode()
print("Message after MAIL FROM: ", recv2)
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
rcptTo = "RCPT TO: <xxxxxx>\r\n"
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024)
recv3 = recv3.decode()
print("Message after RCPT TO: ", recv3)

# Fill in end

# Send DATA command and print server response.
# Fill in start
data = "DATA: <xxxxxx>\r\n"
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024)
recv4 = recv4.decode()
print("Message after DATA: ", recv4)

# Fill in end

# Send message data.

# Fill in start
body = "Hello, I'm using my own mail server for this \r\n"
clientSocket.send(body.encode())

# Fill in end


# Message ends with a single period.

# Fill in start
period = ".\r\n"
clientSocket.send(period.encode())

# Fill in end

# Send QUIT command and get server response.
# Fill in start
quit = "QUIT\r\n"
clientSocket.send(quit.encode())
recv6 = clientSocket.recv(1024)
recv6 = recv6.decode()
print(recv6)
clientSocket.close()
#Fill in end

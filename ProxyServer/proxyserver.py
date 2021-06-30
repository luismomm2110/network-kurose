from socket import *
import sys
import pdb

if len(sys.argv) <= 1:
	print('Usage : "python ProxyServer.py server_ip"\n server_ip : It is the IP Address Of Proxy Server')
	sys.exit(2)
# Create a server socket, bind it to a port and start listening

tcpSerSock = socket(AF_INET, SOCK_STREAM)
serverPort = 8888
tcpSerSock.bind(('', serverPort))
tcpSerSock.listen(1)
while 1:
	# Strat receiving data from the client
	print('Ready to serve...')
	tcpCliSock, addr = tcpSerSock.accept()
	print('Received a connection from:', addr)
	message = tcpCliSock.recv(1024).decode()
        # Fill in start. # Fill in end.
	# Extract the filename from the given message
	print("Second part of message: ", message.split()[1])
	filename = message.split()[1].partition("/")[2]
	print("File name: ", filename)
	fileExist = "false"
	filetouse = "/" + filename
	print("File to use: ", filetouse)
	try: 
		# Check wether the file exist in the cache
		import pdb; pdb.set_trace()
		f = open(filetouse[1:], "r")
		outputdata = f.readlines()
		fileExist = "true"
		# ProxyServer finds a cache hit and generates a response message
		message = "HTTP/1.0 200 OK\r\n"
		tcpCliSock.send(message.encode())
		message = "Content-Type:text/html\r\n"
		tcpCliSock.send(message.encode())
		# Fill in start.
		tcpCliSock.send(filetouse.encode())
		# Fill in end.
		print('Read from cache')
	# Error handling for file not found in cache
	except IOError:
		if fileExist == "false":
			# Create a socket on the proxyserver
			tcpProxyServer = socket(AF_INET, SOCK_STREAM)
			hostn = filename.replace("www.","",1)
			print("Print when fileExist == false :", hostn) 
		try:
			# Connect to the socket to port 80
			# Fill in start.
			tcpProxyServer.connect((hostn, 80))
			print("Socket connected to port 80 in host")
			# Fill in end.
			# Create a temporary file on this socket and ask port 80 for the file requested by the client
			fileobj = tcpProxyServer.makefile('r', None)
			fileobj.write("GET "+"http://" + filename + "HTTP/1.0\n\n")
			print("fileobj: ", fileobj)
		# Read the response into buffer
		# Fill in start.
			responseBuffer = fileobj.readlines()
		# Fill in end.
		# Create a new file in the cache for the requested file.
		# Also send the response in the buffer to client socket and the corresponding file in the cache
			tmpFile = open("./" + filename,"wb")
			tmpFile.write(data)
			tcpCliSock.send(data)
		# Fill in start.
		# Fill in end.
		except:
			print("Illegal request")
		else:
			# HTTP response message for file not found
			# Fill in start.
			tcpCliSock.send("HTTP/1.1 404 Not Found\r\n")
			tcpCliSock.send("\r\n")
			tcpCliSock.send("\r\n")
			# Fill in end.
		# Close the client and the server sockets
			tcpCliSock.close()
tcpSerSock.close()
# Fill in start.
# Fill in end.

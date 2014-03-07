#import socket module
from socket import *
def mysocket():
	serverPort = 9876
	serverSocket = socket(AF_INET, SOCK_STREAM) 
	#Prepare a sever socket
	serverSocket.bind(('',serverPort))
	serverSocket.listen(1)

	while True:
		#Establish the connection
		print 'Ready to serve...'
		connectionSocket, addr = serverSocket.accept()
		try:
			message = connectionSocket.recv(1024)
			filename = message.split()[1]
			f = open(filename[1:])
			outputdata = f.read()
			
			#Send one HTTP header line into socket
			print '200 OK'
			connectionSocket.send('\nHttp/1.1 200 OK\n\n')
			
			#Send the content of the requested file to the client
			#for i in range(0, len(outputdata)):
			#        connectionSocket.send(outputdata[i])
			connectionSocket.send(outputdata)
			connectionSocket.close()
		except IOError:
    		#Send response message for file not found
			pass
			print '404 Not Found'
			connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n')
			#Close client socket 
			connectionSocket.close()

if __name__ == '__main__':
	mysocket()

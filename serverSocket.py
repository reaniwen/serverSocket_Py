#import socket module
from socket import *
def mysocket():
	serverPort = 9876
	serverSocket = socket(AF_INET, SOCK_STREAM) 
	#Prepare a sever socket
	#Fill in start
	serverSocket.bind(('',serverPort))
	serverSocket.listen(1)
	#Fill in end
	while True:
		#Establish the connection
		print 'Ready to serve...'
		connectionSocket, addr = serverSocket.accept()#fill in
		try:
			message = connectionSocket.recv(1024) #Fill in start 	#Fill in end 
			filename = message.split()[1]
			f = open(filename[1:])
			outputdata = f.read()#Fill in start #Fill in end 
			#Send one HTTP header line into socket
			#Fill in start
			print '200 OK'
			connectionSocket.send('\nHttp/1.1 200 OK\n\n')
			#Fill in end
			#Send the content of the requested file to the client
			#for i in range(0, len(outputdata)):
			#        connectionSocket.send(outputdata[i])
			connectionSocket.send(outputdata)
			connectionSocket.close()
		except IOError:
    		#Send response message for file not found
			#Fill in start 
			pass
			print '404 Not Found'
			connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n')
			#Fill in end
			#Close client socket 
			#Fill in start 
			connectionSocket.close()
			#Fill in end

if __name__ == '__main__':
	mysocket()

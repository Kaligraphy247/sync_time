import socket

# initialize the socket
s = socket.socket()

host = input("Please enter the host address of the Sender: ")
port = 19630

s.connect((host, port))
print("Connected!")

filename = input("Please Enter a file name for the incoming file: ")
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()
print(f"{filename} has been received succesfully.")

#with open(filename, 'wb') as file_write:
#    file_write = s.recv(1024)
#    file_write = file_write.write(file_write)
#    print(f"{filename} has been received succesfully.")
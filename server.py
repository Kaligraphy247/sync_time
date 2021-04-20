import socket

# initialize the socket
s = socket.socket()
# set 
host = socket.gethostname()
port = 19630
# bind the host and port
s.bind((host, port))
# listen for any incoming conections
s.listen(1)
print(host)
print("Waiting for any incoming connections ...")
conn, addr = s.accept()
print(addr, "Has connected to the server")

filename = input("Please enter the file name of the file: ")
with open(filename, 'rb') as file_name:
    file_name = file_name.read(1024)
    conn.send(file_name)
    print(f"{filename} has been transfered succesfully.")

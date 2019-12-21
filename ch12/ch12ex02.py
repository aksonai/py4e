# Exercise 2: Change your socket program so that it counts the number of charac-
# ters it has received and stops displaying any text after it has shown 3000 characters.
# The program should retrieve the entire document and count the total number of
# characters and display the count of the number of characters at the end of the
# document.

import socket

try:
    url = input("Enter URL: ")
    host = url.split("/")[2]

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
    cmd = cmd.encode()
    mysock.send(cmd)

    received = b""
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        received += data

    received = received.decode()
    print(received[:3000])
    print(len(received))

    mysock.close()
except:
    print("The URL is improperly formatted or non-existent!")
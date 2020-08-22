# Exercise 5: (Advanced) 
# Change the socket program so that it only shows data after the headers
# and a blank line have been received. Remember that recv receives characters 
# (newlines and all), not lines.
# Test with http://data.pr4e.org/intro-short.txt

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
    pos = received.find(b"\r\n\r\n")
    content = received[pos+4:].decode()
    print(content)
    mysock.close()
except:
    print("The URL is improperly formatted or non-existent!")
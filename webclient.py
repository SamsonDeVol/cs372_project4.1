# Samson DeVol, cs372, project 4.1: Atomic Time, 10-10-22

import os, sys, socket, datetime

def system_seconds_since_1900():
    """
    The time server returns the number of seconds since 1900, but Unix
    systems return the number of seconds since 1970. This function
    computes the number of seconds since 1900 on the system.
    """

    # Number of seconds between 1900-01-01 and 1970-01-01
    seconds_delta = 2208988800

    seconds_since_unix_epoch = int(datetime.datetime.now().strftime("%s"))
    seconds_since_1900_epoch = seconds_since_unix_epoch + seconds_delta

    return seconds_since_1900_epoch


# parse inputs
port_number = 37
server_name = "time.nist.gov"
# ask OS for a socket
s = socket.socket()

# connect the socket
s.connect((server_name,port_number))

# send data
s.sendall("GET / HTTP/1.1\r\nHost: {}\r\nConnection: close\r\n\r\n".format(server_name).encode())
data = b''
while True:
  chunk = s.recv(4096)

  if chunk == b'':
    break

  data += chunk
s.close()
m = int.from_bytes(data, "big")
print("NIST time: ", m)
print("System time: ", system_seconds_since_1900())
# full_message = b''
# # recieve data 4096 bytes at a time and append
# while 1: 
#   d = s.recv(4096)
#   if len(d)==0:
#     break
#   else: 
#     full_message += d
  
# # close
# s.close()
# print(full_message)

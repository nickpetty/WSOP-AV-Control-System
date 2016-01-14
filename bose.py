import socket    # used for TCP/IP communication 
import smtplib   # used to send email report
import time      # used to insert current date in email report
 
# Prepare 3-byte control message for transmission
TCP_IP = '192.168.2.102'
TCP_PORT = 10055
BUFFER_SIZE = 80
MESSAGE = 'SA”Wireless Mic”>2=T<CR>' # Relays 1 permanent off
 
# Open socket, send message, close socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE.encode)
data = s.recv(BUFFER_SIZE)
s.close()
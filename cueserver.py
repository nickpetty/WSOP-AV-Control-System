import socket

class CueServer:
  UDP_IP = None
  UDP_PORT = 52737

  def __init__(self, ip):
    self.UDP_IP = ip

  def cue(self, msg):
      
    print "UDP target IP:", self.UDP_IP
    print "UDP target port:", self.UDP_PORT
    print "message:", msg

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    sock.sendto(msg, (self.UDP_IP, self.UDP_PORT))


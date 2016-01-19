from bose import csp
from binascii import hexlify
import time

bose = csp('192.168.1.102')

#bose.setMute('Wireless Mic Gain', 'toggle')

#bose.preset(1)
#bose.setGainState('Bathrooms', 'T')
#print bose.getGainLevel("Bathrooms")

#bose.setGroupState(1, 'T')
#print bose.getGroupState('1')
print bose.getGroupLevel('7')

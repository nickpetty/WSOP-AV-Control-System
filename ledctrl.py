print 'connecting to cove lighting'
self.units = [0,1,2,3,4,5]
self.units[0] = PowerSupply('192.168.1.101')
self.units[1] = PowerSupply('192.168.1.102')
self.units[2] = PowerSupply('192.168.1.103')
self.units[3] = PowerSupply('192.168.1.104')
self.units[4] = PowerSupply('192.168.1.105')
self.units[5] = PowerSupply('192.168.1.106')

x=0
while x < 510:
    self.units[0].append(FixtureRGB(x))
    self.units[1].append(FixtureRGB(x))
    self.units[2].append(FixtureRGB(x))
    self.units[3].append(FixtureRGB(x))
    self.units[4].append(FixtureRGB(x))
    self.units[5].append(FixtureRGB(x))
    x+=3

def LEDLights(self, state):
	if state == 1:
		for y in range(0,6):
			x=0
			while x <= 75:
				self.units[y][x].rgb = (255,255,255)
				x+=1
			self.units[y].go()
			#time.sleep(1)

	if state == 0:
		for y in range(0,6):
			x=0
			while x <= 75:
				self.units[y][x].rgb = (0,0,0)
				x+=1
			#time.sleep(1)					
			self.units[y].go()
		
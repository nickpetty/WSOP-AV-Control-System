from flask import Flask, render_template
from cueserver import CueServer
#from ledctrl import *
import urllib2

cs = CueServer('127.0.0.1')

app = Flask(__name__)


@app.route('/video/<out>/<source>')
def switch(out, source):
	ip = '127.0.0.1'
	req = 'http://' + str(ip) + ':8181/' + str(out) + '/' +str(source)
	urllib2.urlopen(req)

@app.route('/lights/cmd')
def lights(cmd):
	if cmd == 'ON':
		print 'ON'
		# LEDLights(1)
		# cs.cue('Cue 1 Go') # Set Cue 1 All ON
		pass

	if cmd == 'OFF':
		print 'OFF'
		# LEDLights(0)
		# cs.cue('Cue 2 Go') # Set Cue 2 All OFF
		pass

@app.route('/')
def index():
	pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9191)
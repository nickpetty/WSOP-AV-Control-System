from flask import Flask, render_template, Response
from cueserver import CueServer
#from ledctrl import *
import urllib2

cs = CueServer('192.168.1.92')

app = Flask(__name__)

@app.route('/video/<out>/<source>')
def switch(out, source):
	cmd = 'B' + str(out) + str(source)
	ip = '192.168.137.25'
	req = 'http://' + str(ip) + ':8181/' + str(out) + '/' + str(source)
	urllib2.urlopen(req)
	print 'out: ' + str(out)
	print 'source: ' + str(source)
	return Response(status=200)

@app.route('/lights')
def lightPage():
	return render_template('lights.html')

@app.route('/lights/<cmd>')
def lights(cmd):
	if cmd == 'ON':
		print 'ON'
		# LEDLights(1)
		cs.cue('Cue 1 Go') # Set Cue 1 All ON
		return Response(status=200)

	if cmd == 'OFF':
		print 'OFF'
		# LEDLights(0)
		cs.cue('Channel 1 > 255 At 0') # Set Cue 2 All OFF
		return Response(status=200)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9191)
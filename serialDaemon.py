from flask import Flask, Response
from mondo import Mondo

switch = Mondo('/dev/ttyAMA0')

app = Flask(__name__)

@app.route('/<out>/<source>')
def mustard(out, source):
	switch.set(int(out), int(source))
	return Response(status=200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8181)
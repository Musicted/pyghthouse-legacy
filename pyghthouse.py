from websocket import WebSocket, send, recv
from umsgpack import packb, unpackb
from array import array

class Pyghthouse:
	
	def __init__(self, uname, token):
		self._addr     = "wss://lighthouse.uni-kiel.de/websocket"
		self._data     = {
		'REID' : 0,
		'AUTH' : {'USER' : uname, 'TOKEN' : token},
		'VERB' : 'PUT',
		'PATH' : ['user', uname, 'model'],
		'META' : {},
		'PAYL' : array('B', [255, 0, 0] * 14 * 28).tobytes()
		}
		self.websocket = WebSocket()
	
	def start(self):
		self.websocket.connect(self._addr)
	
	def send(self, img = None, verbose = False):
		if img != None:
			self._data['PAYL'] = array('B', img).tobytes()
		self.websocket.send(packb(self._data))
		if verbose:
			ans = unpackb(self.websocket.recv())
			print("{}, {}".format(ans['RNUM'], ans['RESPONSE']))
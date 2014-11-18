from __future__ import print_function
import websocket,thread,time,json

class client:
	def __init__(self):
		domain = raw_input('Enter server address(enter blank for default)')
		print('connecting to server....')
		if domain:
			self.ws = websocket.create_connection(domain)
		else:
			self.ws = websocket.create_connection('ws://py2pyrpc.herokuapp.com/')
		print('waking up server....')
		time.sleep(3)
		print(self.ws.recv())
		thread.start_new_thread(self.pinger,(),)

	def pinger(self):
		while 1:
			self.ws.send(json.dumps({
					'type' : 'ping'
				}))
			time.sleep(50)

	def show(self,message):
		data = json.loads(message)
		if not data['success']:
			print(data['result'],data['error'])
		else:
			print('success')
			print('result :', data['result'])

	def sha(self,algo,message,hexdigest=True):
		data = json.dumps({
			'type' : 'execute',
			'algo' : algo,
			'hexdigest' : hexdigest,
			'message' : message
		})
		self.ws.send(data)
		data = self.ws.recv()
		self.show(data)

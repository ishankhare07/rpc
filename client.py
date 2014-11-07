from __future__ import print_function
import websocket,thread,time,json

class client:
	def __init__(self):
		websocket.enableTrace(True)
		self.ws = websocket.WebSocketApp('ws://localhost:8000',
					on_open = self.open,
					on_message = self.receive,
					on_error = self.err,
					on_close = self.close
				)

	def open(self):
		print('connected to server')
		thread.start_new_thread(self.pinger,(),)

	def pinger(self):
		while 1:
			self.ws.send(
				json.dumps({
					'type' : 'ping'
				})
			)
			time.sleep(50)

	def receive(self,message):
		data = json.loads(message)
		if not data['success']:
			print(data['result'],data['error'])
		else:
			print('success')
			print('result :', data['result'])

	def err(self,err):
		print('Error!',err)

	def close(self):
		print('good bye!')
		print('connection closed')

	def sha(self,algo,message,hexdigest=True):
		data = json.dumps({
			'type' : 'execute',
			'algo' : algo,
			'hexdigest' : hexdigest,
			'message' : message
		})
		self.ws.send(data)

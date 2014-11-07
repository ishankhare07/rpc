import tornado.web
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import json, hashlib, os

class WsHandler(tornado.websocket.WebSocketHandler):
	def open(self):
		self.write_message('connected')
	def on_message(self,msg):
		data = json.loads(msg)
		'''data = {
			'type' : 'ping/execute',
			'algo' : 'sha256/sha512',
			'hexdigest' : 'True/False',
			'message' : '<string>'
		}
		'''
		if data['type'] == 'ping':
			print 'ping from client'
			return
		algo = data['algo']
		hexdigest = data['hexdigest']
		message = data['message']

		result = self.generate(algo,hexdigest,message)
		self.write_message(result)

	def generate(self,algo,hexdigest,message):
		if algo == 'sha256':
			algo = hashlib.sha256
		elif algo == 'sha512':
			algo = hashlib.sha512
		else:
			return json.dumps({
				'result' : None,
				'error' : 'algorithm not supported',
				'success' : False
			})

		a = algo(message)
		if hexdigest:
			digest = a.hexdigest()
		else:
			digest = a.digest()

		return json.dumps({
			'result' : digest,
			'error' : None,
			'success' : True
		})

app = tornado.web.Application([
		(r'/',WsHandler),
	])
server = tornado.httpserver.HTTPServer(app)
server.listen(os.environ.get('PORT',8000))
print 'server listening on port 8000....'
tornado.ioloop.IOLoop.instance().start()

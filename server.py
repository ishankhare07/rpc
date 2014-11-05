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
			'algo' : 'sha256/sha512',
			'digest' : 'hexdigest/digest',
			'message' : '<string>'
		}
		'''
		algo = data['algo']
		digest = data['digest']
		message = data['message']

		result = self.generate(algo,digest,message)
		self.write_message(result)

	def generate(self,algo,digest,message):
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
		if digest == 'hexdig':
			digest = a.hexdigest()
		else:
			digest = a.digest()

		return json.dumps({
			'result' : digest,
			'error' : None,
			'success' : True
		})

app = tornado.Application([
		(r'/',WsHandler),
	])
server = tornado.httpserver.HTTPServer(app)
server.listen(os.environ.get('PORT',8000))
tornado.ioloop.IOLoop.instance().start()
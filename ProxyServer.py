import tornado.web
import tornado.ioloop
from tornado.options import options,define,parse_command_line

define('port',default=8088,help='run this port',type=int)

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('./a.html')

parse_command_line()
app=tornado.web.Application(
		[
			('/',MainHandler),
		],
		)
app.listen(options.port)
tornado.ioloop.IOLoop.instance().start()
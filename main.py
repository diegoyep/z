import tornado.httpserver
import tornado.web
import tornado.ioloop
import os.path

from tornado.options import define, options
define("port", default=8000, help ="run on given port ", type = int)

class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r"/", IndexHandler)]

        settings = dict(
            template_path = os.path.join(os.path.dirname(__file__), "templates"),
            static_path = os.path.join(os.path.dirname(__file__) , "static"),
            debuf = True,
            )

        tornado.web.Application.__init__(self, handlers, **settings)




class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            "index.html",
            page_title = "Zefira | Development version ",
            header_text = "Welcome"
            )


def main():
    tornado.options.parse_command_line()
    server = tornado.httpserver.HTTPServer(Application())
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()

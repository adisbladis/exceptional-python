from exceptional.contrib.cherrypy import ExceptionalCherry
import cherrypy


class ExceptionalAPI(ExceptionalCherry):

    @cherrypy.expose
    def index(self):
        raise Exception('Hello world')

    @cherrypy.expose
    def fail(self):
        return 'Hello world'


api = ExceptionalAPI()
cherrypy.quickstart(ExceptionalAPI())

import cherrypy,os

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return open("./static/button_web.html",encoding="utf8")

if __name__ == '__main__':
    CP_CONF = {
        'global' : {
        'server.socket_host' : '0.0.0.0',
        'server.socket_port' : 8080
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': os.path.abspath('./static') # staticdir needs an absolute path
            },
        '/css':
        { 'tools.staticdir.on':True,
          'tools.staticdir.dir': os.path.abspath("./static/css")
        }
        }
    cherrypy.quickstart(HelloWorld(),'/',CP_CONF)
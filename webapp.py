
import sys
import os
from algorithms import Algorithms
import tornado
from tornado.web import RequestHandler
from tornado.web import Application


# Version checks, we use features that are supported only in Tornado>=4.3
if tornado.version_info[0] < 4 and tornado.version_info[1] < 3:
    print("Please update your tornado version. Current version is {0}".format(tornado.version))
    sys.exit(1)

algorithmsList = [
            [">Global Estándar","global_estandar"],
            ["--Global Lineal","global_lineal"],
            [">Global con K-Band (no funciona/se pega)","global_kband"],
            ["--Global K-Band Lineal*","kband_lineal"],
            [">Global costo por gap*","global_costogap"],
            [">Semiglobal Estándar","semi_estandar"],
            ["--Semiglobal Lineal","semi_lineal"],
            [">Semiglobal costo por gap*","semi_costogap"],
            [">Local Estándar","local_estandar"],
            ["--Local Lineal","local_lineal"],
            [">Local costo por gap*","local_costogap"],
        ]
    
class MainHandler(RequestHandler):
    def get(self):
        self.render("index.html", results=None, algorithmsList = algorithmsList)
    
    def post(self):
        first_word = self.get_argument("first_word")
        second_word = self.get_argument("second_word")
        type_name = self.get_argument("type")
        kband_value = self.get_argument("kband_value")
        print(kband_value)
        results = Algorithms().get_result(first_word, second_word, type_name, kband_value= kband_value)
        
        self.render("index.html", results=results, algorithmsList = algorithmsList)

class HelpPage(RequestHandler):
    def get(self):
        self.render("index.html", results=None, algorithmsList = [])

def start_web_server():
    application = Application([
        (r"/", MainHandler),
        (r"/help", HelpPage),
    ], debug=True)
    application.listen(os.getenv("PORT", 8080))
    print("Starting web server on port {0}".format(os.getenv("PORT", 8080)))
    tornado.ioloop.IOLoop.current().start()
    
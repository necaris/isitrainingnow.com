"""
isitrainingnow.com -- a single-serving web site thought up at the
DC Python Dojo. This version is expanded and improved from our team
entry.
"""
# Ensure we're running in an entirely green-threaded world
import gevent.monkey
gevent.monkey.patch_all()

# Using Pyramid for the web layer here
from pyramid.config import Configurator

config = Configurator()
config.include('pyramid_jinja2')
config.add_jinja2_renderer('.html')
config.add_jinja2_search_path("./templates")

config.add_route("raw_index", "/")
config.add_route("from_query", "/qs")
config.add_route("from_ip", "/ip")
config.scan("views")

app = config.make_wsgi_app()

if __name__ == '__main__':
    import gevent.pywsgi

    server = gevent.pywsgi.WSGIServer(("127.0.0.1", 8088), app)

    try:
        print("Listening on 127.0.0.1:8088")
        server.serve_forever()
    except KeyboardInterrupt:
        server.stop()

# Ensure we're running in an entirely green-threaded world
import gevent.monkey
gevent.monkey.patch_all()

from pyramid.config import Configurator
from pyramid.view import view_config

# Create our Pyramid app

config = Configurator()
config.include('pyramid_jinja2')
config.add_jinja2_renderer('.html')
config.add_jinja2_search_path("./templates")

config.add_route("raw_index", "/")
config.add_route("from_query", "/qs")
config.add_route("from_ip", "/ip")

#
# View functions
#

@view_config(route_name="raw_index", renderer="templates/index.html")
def index(request):
    """
    Serve the simple index page, which redirects to the more complex index
    page(s) based on whether or not the user's location data is available.
    """
    return {}


@view_config(route_name="from_query", renderer="templates/result.html")
def from_query(request):
    """
    Serve an index page that knows a user's location from their browser,
    details passed in via query parameters.
    """
    return {"raining": True, "meta": {"weather": "More information about the weather", "location": "Your browser said so."}}


@view_config(route_name="from_ip", renderer="templates/result.html")
def from_ip(request):
    """
    Serve an index page that guesses their location based on their IP
    address.
    """
    pass


# Ensure that that @view_config decorations are picked up
config.scan()

app = config.make_wsgi_app()

if __name__ == '__main__':
    import gevent.pywsgi

    server = gevent.pywsgi.WSGIServer(("127.0.0.1", 8088), app)

    try:
        print("Listening on 127.0.0.1:8088")
        server.serve_forever()
    except KeyboardInterrupt:
        server.kill()

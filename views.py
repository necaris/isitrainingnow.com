"""
View functions for the web interface.

Note the use of the @view_config decorator from Pyramid -- for an app of this
size it's just as easy to use `Configurator#add_view`, but I prefer to keep
view configuration close to the functions being configured.
"""
from pyramid.view import view_config
import weather
import utils


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
    with details passed in via query parameters.
    """
    lat = float(request.GET.get("lat", 0.0))
    lon = float(request.GET.get("lon", 0.0))
    conditions = weather.current_conditions(lat, lon)
    raining = weather.is_it_raining_at(lat, lon, conditions)
    return utils.format_result(raining, (lat, lon), conditions,
                               "Location determined from your browser")


@view_config(route_name="from_ip", renderer="templates/result.html")
def from_ip(request):
    """
    Serve an index page that guesses their location based on their IP
    address.
    """
    pass

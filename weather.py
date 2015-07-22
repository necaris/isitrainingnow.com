"""
Weather-related helpers for isitrainingnow.com -- uses the forecast.io API
"""
import os
import forecastio

forecast_api_key = os.getenv("FORECAST_API_KEY")

def current_conditions(lat, lon):
    """
    Fetch the current weather forecast from the forecast.io API, and
    return a dictionary describing the current weather conditions.
    """
    forecast = forecastio.load_forecast(key=forecast_api_key, lat=lat, lng=lon)
    current = forecast.currently()
    # We know the actual weather information is in the `d` dictionary
    return current.d


def is_it_raining_at(lat, lon, conditions=None):
    """
    Determine whether or not it's currently raining at the given coordinates,
    by fetching the current weather conditions and making a decision based on
    the probability of precipitation.
    """
    if not conditions:
        conditions = current_conditions(lat, lon)

    precip_chance = conditions["precipProbability"]
    return (precip_chance > 0.8)

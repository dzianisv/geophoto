
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter


# https://towardsdatascience.com/reverse-geocoding-in-python-a915acf29eb6
_locator = Nominatim(user_agent="Google Chrome", timeout=10)
rgeocode = RateLimiter(_locator.reverse, min_delay_seconds=0.001)

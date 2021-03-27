
import sys

import image
import exif
import geocoding

for file_path in sys.argv[1:]:
    coordinates = exif.get_geo_info(file_path)
    location = geocoding.rgeocode(coordinates)
    country, state, city = location.raw['address']['country'], location.raw['address']['state'], location.raw['address']['city']
    image.add_text(file_path, f"{city}, {state}, {country}")

from GPSPhoto import gpsphoto

def get_geo_info(file_path):
    # Get the data from image file and return a dictionary
    data = gpsphoto.getGPSData(file_path)
    rawData = gpsphoto.getRawData(file_path)
    if 'Latitue' in data:
        return (data['Latitude'], data['Longitude'])
    else:
        return None
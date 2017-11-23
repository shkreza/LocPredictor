import requests

api_key = 'XXX'

def get_address(latitude, longitude):
    ''' Returns the addess associated with the latitude and longitude coordinates (using Google Maps API).
    '''
    
    api_url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key={key}&result_type=premise|street_address|route|neighborhood'

    payload = {
        'latitude': latitude,
        'longitude': longitude,
        'key': api_key
    }

    api_to_call = api_url.format(**payload)
    response = requests.get(api_to_call)
    address = 'EMPTY'
    if(response.ok):
        content = response.json()
        if (len(content['results']) > 0):
            address = content['results'][0]['formatted_address']
    else:
        address = 'NOT FOUND'

    return address

def get_place(latitude, longitude):
    ''' Returns the nearest known location associated with the latitude and longitude coordinates (using Google Maps nearby search API).
    '''
    
    api_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&rankby=distance&key={key}'

    payload = {
        'latitude': latitude,
        'longitude': longitude,
        'key': api_key
    }

    api_to_call = api_url.format(**payload)
    response = requests.get(api_to_call)
    address = 'EMPTY'
    if(response.ok):
        content = response.json()
        if (len(content['results']) > 0):
            address = content['results'][0]['name']
    else:
        address = 'NOT FOUND'

    return address


def main():
    lat = 47.637362
    lon = -122.135648
    print(get_place(lat, lon))


if __name__ == "__main__":
    main()

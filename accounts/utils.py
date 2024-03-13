import string, random
from geopy.geocoders import Nominatim


def get_location(latitude, longitude):
    location = Nominatim(user_agent="my_geocoder").reverse(
        (latitude, longitude), 
        language="ru"
    )
    
    if location and location.address:
        return {
            "city": location.address.split(', ')[-3],
            "country": location.address.split(', ')[-1],
            "address": location.address
        }
    
    return False


def generate_password(password="", length=random.randint(20, 25)):
    all_char = string.ascii_letters + string.digits
    
    while len(password) < length:
        source = " ".join(all_char).split() + ['#', "*", "?", "!", "@"]
        random.shuffle(source)
        password += random.choice(source)
    
    return password

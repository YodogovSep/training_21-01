from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="wazeyes") # Nome do seu aplicativo
location = geolocator.geocode("175 5th Avenue NYC")
print(location.adress)
print((location.latitude, location.longitude))

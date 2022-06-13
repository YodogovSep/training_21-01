from pygeocoder import Geocoder

endereco = 'avenida paulista, 100 Sao Paulo'
resultado = Geocoder().geocode(endereco)
print(resultado)

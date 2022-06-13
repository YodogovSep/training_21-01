from pygeocoder import Geocoder

endereco = '1222, Lins de Vasconcelos, São Paulo, SP'
print(Geocoder('AIzaSyAYqVUOZ2tBCFZyKERkNKR3dLgT5OL-Esk').geocode(endereco).coordinates)
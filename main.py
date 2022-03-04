import googlemaps


gmaps = googlemaps.Client(key='AIzaSyDT_mXcYS-mfpbWs3BV6OPmp87GlyskXYA')
origins = [
    "Paris, France",
    "Gare de Paris Montparnasse, France"
]
destinations = [
    "Perros-Guirec, France",
    "Saint-Brieuc, France"
]
distance_matrix = gmaps.distance_matrix(origins, destinations)



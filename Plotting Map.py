import gmplot
import pandas as pd

df = pd.read_csv('LocationTest.csv')
x_coords = df['X Coordinate'].to_list()
y_coords = df['Y Coordinate'].to_list()

#set coordinates for the competition area
lat_coords = [52.085441, 52.088288, 52.091333, 52.087536]
long_coords = [5.139171, 5.145649, 5.144480, 5.137539]

#initialize the map at a given point (Science Park)
gmap = gmplot.GoogleMapPlotter(52.084223, 5.176004, 13)

#plot the competition area on the map
gmap.polygon(lat_coords, long_coords, color='cornflowerblue')

#plot the location of invasive species
gmap.scatter(x_coords, y_coords, 'cornflowerblue')

#draw map into HTML file
#Note that the map is watermarked with 'For development purposes only'. To get a normal Google Maps view requires a paid API
gmap.draw("invasive species map.html")
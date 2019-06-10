
import folium
import pandas as pd

df = pd.read_csv('Volcanoes.txt')

# center the map around the data by averaging lat and lon data

# take the average
latmean = df['LAT'].mean()
lonmean = df['LON'].mean()

# create a map object
map7 = folium.Map(location=[latmean, lonmean], zoom_start = 6, tiles = 'Stamen Terrain')

# create a function to add different colors for elevation for each mountain
def coloricon(elev):
    if elev in range(0, 1000):
        col = 'green'
    elif elev in range(1001, 1999):
        col = 'blue'
    elif elev in range(2000, 2999):
        col = 'orange'
    else:
        col = 'red'
    return col

# create a for loop to use file dta to create markers
# two iterators in this for loop, and so put them in a zip function
# read as iterator, and then where is df to "grab" that iterators value
for lat, lon, name, elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    folium.Marker(location = [lat, lon], popup = name, icon = folium.Icon(color = coloricon(elev),
    icon = 'cloud')).add_to(map7)

print(map7.save('test.html'))
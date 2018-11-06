

# example file (can be downloaded from http://www.bruggenvanamsterdam.nl/bruggen.kml
KML_SCHEMA = 'bruggen_ams.kml'

from lxml import etree as ET
import geopandas as gpd
from shapely.geometry import Point

tree = ET.parse(PATH_KML_BRUGGEN + KML_SCHEMA)
root = tree.getroot()

print ('root.xpath: {}'.format(root.xpath))
print ('rootnsmap: {}'.format(root.nsmap))

names = root.xpath('//kml:name', namespaces={'kml': "http://earth.google.com/kml/2.1"})
coordinates = root.xpath('//kml:coordinates', namespaces={'kml': "http://earth.google.com/kml/2.1"})

result = []
for name, coords in zip(names, coordinates):
    brug_dict = {}
    brug_dict['name'] = name.text
    brug_dict['x_coord'] = coords.text.split(',')[0]
    brug_dict['y_coord'] = coords.text.split(',')[1]
    
    result.append(brug_dict)
    
# geo dataframe
df = gpd.GeoDataFrame(pd.DataFrame(result))

for col in ['x_coord', 'y_coord']:
    df[col] = df[col].astype(float)
df['geometry'] = [Point(xy) for xy in zip(df['x_coord'], df['y_coord'])]


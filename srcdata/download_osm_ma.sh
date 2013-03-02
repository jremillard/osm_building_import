# script to download current MA OSM data, and replace OSM data in postGIS database
rm massachusetts.osm.bz2
wget http://download.geofabrik.de/openstreetmap/north-america/us/massachusetts.osm.bz2 massachusetts.osm.bz2
rm index.html


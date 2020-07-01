# <img src="https://avatars1.githubusercontent.com/u/29209318?s=32&v=4" width="32" height="32" alt="woeplanet">&nbsp;py-woeplanet-uri

# The Really Short Version

_Forking GeoPlanet one place type at a time_.

# The Short Version

WoePlanet is Where On Earth (AKA WOE, also AKA GeoPlanet) data, smushed up with coordinate and boundary data from Flickr Shapes, Quattroshapes and Natural Earth Data (that's fancy talk for _polygons_) as well as concordances and other metadata rescued from `woe.spum.org` before it died and went offline.

# The Longer Version

Tools for working with URIs for WoePlanet documents.

## Installation

```
sudo pip install .
```

## Usage

### Simple Usage

```
import woeplanet.utils.uri

fname = '12695836.geojson'
woeplanet.utils.uri.is_woe_file('12695836.geojson')
True

id = 12695836
root = '/var/data/woeplanet-data'
woeplanet.utils.uri.id2abspath(root, id)
'/var/data/woeplanet-data/126/958/36/12695836.geojson'

woeplanet.utils.uri.id2relpath(id)
'126/958/36/12695836.geojson'

woeplanet.utils.uri.id2path(id)
'126/958/36'

woeplanet.utils.uri.id2fname(id)
'12695836.geojson'
```

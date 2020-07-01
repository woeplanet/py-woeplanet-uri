import woeplanet.utils.uri as uri

def test_is_woe_file():
    fname = '12695836.geojson'
    assert uri.is_woe_file(fname) == True

def test_is_not_woe_file():
    fname = 'woeplanet.geojson'
    assert uri.is_woe_file(fname) == False

def test_id2abspath():
    id = 12695836
    root = '/var/data/woeplanet-data'
    assert uri.id2abspath(root, id) == '/var/data/woeplanet-data/126/958/36/12695836.geojson'

def test_id2relpath():
    id = 12695836
    assert uri.id2relpath(id) == '126/958/36/12695836.geojson'

def test_id2path():
    id = 12695836
    assert uri.id2path(id) == '126/958/36'

def test_id2fname():
    id = 12695836
    assert uri.id2fname(id) == '12695836.geojson'

import logging
import os
import re

def is_woe_file(path):
    abs_path = os.path.abspath(path)
    fname= os.path.basename(abs_path)

    if re.match(r'^\d+(?:.*)?\.geojson$', fname):
        return True

    return False

def id2abspath(root, id):
    rel = id2relpath(id)
    path = os.path.join(root, rel)
    return path
    
def id2relpath(id):
    fname = id2fname(id)
    parent = id2path(id)
    path = os.path.join(parent, fname)
    return path

def id2fname(id):
    return '%s.geojson' % str(id)

def id2path(id):
    tmp = str(id)
    parts = []

    while len(tmp) > 3:
        parts.append(tmp[0:3])
        tmp = tmp[3:]

    if len(tmp):
        parts.append(tmp)

    return '/'.join(parts)

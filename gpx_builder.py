from xml.etree import ElementTree


def gpx_builder(data):
    gpx = ElementTree.Element('gpx')
    tree = ElementTree.ElementTree(gpx)
    gpx.set('version', '1.0')

    gpxname = ElementTree.SubElement(gpx, 'name')
    gpxname.text = 'PLACEHOLDER'
    rte = ElementTree.SubElement(gpx, 'rte')
    for routepoint in range(len(data)):
        rtept = ElementTree.SubElement(rte, 'rtept')
        current_jump = data[routepoint]
        rtept.set('lat', current_jump['latitude'])
        rtept.set('lon', current_jump['longitude'])

        rtept_name = ElementTree.SubElement(rtept, 'name')
        rtept_name.text = 'Jump n° {}'.format(routepoint)

        rtept_desc = ElementTree.SubElement(rtept, 'desc')
        rtept_desc.text = '{}\nip: {}\nTime: PLACEHOLDER'.format(data[routepoint]['ptr'], data[routepoint]['ip'])

    return tree

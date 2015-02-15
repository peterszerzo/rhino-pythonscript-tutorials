"""

Rhino Python Script Tutorial
Advanced

Exercise 01

Importing GeoData.

"""

import rhinoscriptsyntax as rs
import math

from os import listdir
from os.path import basename

import json

path = rs.DocumentPath()
name = rs.DocumentName()

root_path = path[:-len(name)]
geo_path = root_path + "geo/"


def draw_point(pt):

	"""Draws point."""

	rs.AddPoint([ pt[0], pt[1], 0])


def draw_linestring(ls):

	n = len(ls)

	for i in range(n - 1):

		rs.AddLine([ls[i][0], ls[i][1], 0], [ls[i+1][0], ls[i+1][1], 0])


def draw_polygon(pg):

	"""Draws polygon."""

	for ls in pg:

		draw_linestring(ls)


def draw_multipolygon(mp):

	"""Draws multipolygon."""

	for pg in mp:

		draw_polygon(pg)


draw_dict = {
	
	"Point": draw_point,
	"LineString": draw_linestring,
	"Polygon": draw_polygon,
	"MultiPolygon": draw_multipolygon

}


def import_feature(feature):

	"""Imports single feature from featurecollection."""

	geometry = feature["geometry"]
	coordinates = geometry["coordinates"]

	draw_dict[geometry["type"]](coordinates)


def get_sublayer_name(properties):

	"""Loops through properties hash and returns key meeting the following two criteria:
	1. is not 'name'
	2. does not end in 'id'
	Such keys have many distinct values in a typical featurecollection and would produce many layers (hundrends of thousands, to be precise).
	"""

	for key in properties:

		value = properties[key]

		if (key != "name") and ((len(key) < 2) or (key[-2:] != "id")) and (value is not None):

			return key

	return "_unorganized_";



def import_file(name):

	"""Import file with name specified relative to script path."""

	if (name[-4:] == "json"):

		layer = name[:-5]

		rs.AddLayer(layer)

		rs.CurrentLayer(layer)

		json_file_path = geo_path + name

		with open(json_file_path) as json_file:
			json_data = json.load(json_file)

		features = json_data["features"]

		for feature in features:

			sublayer = get_sublayer_name(feature["properties"])

			rs.AddLayer(sublayer, parent = layer)
			rs.CurrentLayer(layer + '::' + sublayer)

			import_feature(feature)


def Main():

	for f in listdir(geo_path):

		import_file(basename(f))

Main()
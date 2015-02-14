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


def draw_polygon(polygon):

	"""Draws polygon."""

	n = len(polygon)

	for i in range(n - 1):

		rs.AddLine([polygon[i][0], polygon[i][1], 0], [polygon[i+1][0], polygon[i+1][1], 0])


def draw_multipolygon(mp):

	"""Draws multipolygon."""

	for polygon in mp:

		draw_polygon(polygon)


def import_feature(feature):

	"""Imports single feature from featurecollection."""

	geometry = feature["geometry"]
	coordinates = geometry["coordinates"]

	if (geometry["type"] == "Point"):

		draw_point(coordinates)

	elif (geometry["type"] == "LineString"):

		draw_linestring(coordinates)

	elif (geometry["type"] == "Polygon"):

		for coordinate in coordinates:
			draw_polygon(coordinate)

	elif (geometry["type"] == "MultiPolygon"):

		for coordinate in coordinates:
			draw_multipolygon(coordinate)


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

			#sublayer = feature['properties']['name']

			#if sublayer == None:
			#	sublayer = 'no-name'

			#rs.AddLayer(feature['properties']['name'], parent = layer)
			#rs.CurrentLayer(layer + '::' + feature['properties']['name'])

			import_feature(feature)


def Main():

	for f in listdir(geo_path):

		import_file(basename(f))

Main()
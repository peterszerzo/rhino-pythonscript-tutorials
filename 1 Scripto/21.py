"""

Rhino Python Script Tutorial
Exercise 21

Refactor Moebius Strip

"""

import rhinoscriptsyntax as rs

import math

def vector_add(v1, v2):

    return [v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2]]

def vector_scale(v, s = 1):

    return [v[0] * s, v[1] * s, v[2] * s]

def Main():
    
    n = 48

    radius = 3
    width = 1.8
    thickness = 0.1

    # two sets of points are defined
    points_1 = []
    points_2 = []
    points_3 = []
    points_4 = []

    lines_1 = []
    lines_2 = []
    lines_3 = []
    lines_4 = []
        
    for i in range(0, n): # notice how range() accepts variables
    
    	# a little trick here: as i goes from 0 to n-1, k will go from 0 to n / (n-1)
        #   the latter number is just a little under 1, so we don't add repetitive lines
    	k = i / n
    	
    	# traverse the full circle
        angle = k * 2 * math.pi

        v = [radius * math.cos(angle), radius * math.sin(angle), 0]

        v1 = [ -math.sin(angle), math.cos(angle), 0 ]

        v2 = [ math.cos(angle) * math.sin(angle), math.sin(angle) * math.sin(angle), math.cos(angle) ]

        v3 = [ math.cos(angle) * math.cos(angle), math.sin(angle) * math.cos(angle), - math.sin(angle) ]

        point_1 = vector_add(v, vector_add(vector_scale(v3, + width / 2), vector_scale(v2, + thickness / 2)))
        point_2 = vector_add(v, vector_add(vector_scale(v3, + width / 2), vector_scale(v2, - thickness / 2)))
        point_3 = vector_add(v, vector_add(vector_scale(v3, - width / 2), vector_scale(v2, - thickness / 2)))
        point_4 = vector_add(v, vector_add(vector_scale(v3, - width / 2), vector_scale(v2, + thickness / 2)))

        points_1.append(point_1)
        points_2.append(point_2)
        points_3.append(point_3)
        points_4.append(point_4)

    for i in range(0, n):

        lines_1.append(rs.AddLine(points_1[i], points_2[i]))
        lines_2.append(rs.AddLine(points_2[i], points_3[i]))
        lines_3.append(rs.AddLine(points_3[i], points_4[i]))
        lines_4.append(rs.AddLine(points_4[i], points_1[i]))

    rs.AddLoftSrf(lines_1, None, None, 2, 0, 0, True)
    rs.AddLoftSrf(lines_2, None, None, 2, 0, 0, True)
    rs.AddLoftSrf(lines_3, None, None, 2, 0, 0, True)
    rs.AddLoftSrf(lines_4, None, None, 2, 0, 0, True)
        
Main()
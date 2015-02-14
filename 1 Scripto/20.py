"""

Rhino Python Script Tutorial
Exercise 20

Moebius Strip Surface

"""

import rhinoscriptsyntax as rs

import math

def Main():
    
    n = 15

    radius = 3
    width = 1

    # two sets of points are defined
    points_1 = []
    points_2 = []

    lines = []
        
    for i in range(0, n): # notice how range() accepts variables
    
    	# a little trick here: as i goes from 0 to n-1, k will go from 0 to n / (n-1)
        #   the latter number is just a little under 1, so we don't add repetitive lines
    	k = i / n
    	
    	# traverse the full circle
        angle = k * 2 * math.pi


        # first set of points
        radius_p_1 = radius + width / 2 * math.cos(angle)
        height_1 = width / 2 * math.sin(angle)
                        
        point_1 = [radius_p_1 * math.cos(angle), radius_p_1 * math.sin(angle), + height_1]
        points_1.append(point_1)


        # second set of points
        radius_p_2 = radius - width / 2 * math.cos(angle)
        height_2 = - width / 2 * math.sin(angle)

        point_2 = [radius_p_2 * math.cos(angle), radius_p_2 * math.sin(angle), + height_2]
        points_2.append(point_2)

    for i in range(0, n):

        lines.append(rs.AddLine(points_1[i], points_2[i]))

    rs.AddLoftSrf(lines, None, None, 2, 0, 0, True)
        
Main()
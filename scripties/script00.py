# \\\\\\\\**\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\***\\\\\
#
# Hello, this is a series of Rhino Python Scripting tutorials.
#
# Rhino is a 3d modeling software, and Python is a programming language.
# Python is used within Rhino to automate drawing and model things:
#     Computationally. 
#         Uaggh!
#
# Have fun. 
# Learn like a minimalist. 
# Send feedback.
#
# ////////**///////////////////////////////////////////////////***/////

# Notice the little '#' at the beginning of the line?
# These lines are ignored by Python as the script gets executed.
# So are the lines that are within """ triple quotes """, such as the ones below:
    
"""

Rhino Python Script Tutorial
Exercise 00

This is how an empty script file looks like.
If you run it, it does nothing.
However, it is the 'frame' in which all the groovy modeling commands go.

It actually does things, but you don't need to understand this fully yet:
    the rhino script syntax is imported and given a short name (rs).
        [rs will show up for most commands in later scripts]
    the Main() method is defined as 'def Main():'.
    the Main() method is called by simply typing Main().

"""

import rhinoscriptsyntax as rs

import math

def Main():

Main()
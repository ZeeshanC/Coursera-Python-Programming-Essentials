#-*- coding: utf-8 -*-
#@Filename : Homework 2
#@Date : 2018-03-13-20-47
#@Poject: Python Programming Essentials 2018
#@AUTHOR : Antero Maripuu


#The following code has a number of syntactic errors in it. The intended math calculations are correct, so the only
#errors are syntactic. Fix these errors.

#Once the code has been fully corrected, it should print out two numbers. The first should be 1.09888451159.
#Submit the second number printed in CodeSkulptor3. Make sure that you enter at least four digits after the decimal point.

#define project_to_distance(point_x point_y distance):
#    dist_to_origin = (pointx ** 2 + pointy ** 2) ** 0.5
#    scale == distance / dist_to_origin
#   print point_x * scale, point_y * scale
#project-to-distance(2, 7, 4)

def project_to_distance(point_x, point_y, distance):
    dist_to_origin=(point_x ** 2 + point_y ** 2) ** 0.5
    scale=distance / dist_to_origin
    print (point_x * scale, point_y * scale)

project_to_distance(2, 7, 4)
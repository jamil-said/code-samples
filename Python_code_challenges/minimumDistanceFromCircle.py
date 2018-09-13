
""" minimumDistamceFromCircle 
Given a circle centered at the point (0, 0) of a cartesian plan, create a
function that returns the minimum distance (real number) from the perimeter 
of the circle to a given point on the cartesian plan. The input is composed 
of two coordinates (real numbers) that determine the point.
"""

def distCircle(x, y):
    return abs(((x**2)+(y**2))**(1/2)-1)     

    
print(distCircle(1, 1)) # 0.41421356237309515
print(distCircle(-1, -1)) # 0.41421356237309515
print(distCircle(0.5, 0.5)) # 0.2928932188134524
print(distCircle(0, 0)) # 1.0
print(distCircle(0, -3)) # 2.0
print(distCircle(-0.3, 4)) # 3.0112342240263157

from numpy import *
from matplotlib import *
from matplotlib import pyplot as plt
from math import *
class vector:
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle
mag1=float(input("Enter the magnitude of the first vector: "))
ang1=float(input("Enter the angle of the first vector (in degrees): "))
mag2=float(input("Enter the magnitude of the second vector: "))
ang2=float(input("Enter the angle of the second vector (in degrees):"))
v1=vector(mag1,ang1)
v2=vector(mag2,ang2)       
ycomponents=v1.magnitude*sin((v1.angle)*(pi/180))+v2.magnitude*sin((v2.angle)*(pi/180))
xcomponents=v1.magnitude*cos((v1.angle)*(pi/180))+v2.magnitude*cos((v2.angle)*(pi/180))
finalmagnitude=sqrt(xcomponents**2+ycomponents**2)
finalangle=arctan(ycomponents/xcomponents)
finalangledegrees=finalangle*(180/pi)
print("The magnitude of the sum of the vectors is",finalmagnitude, "and the angle is", finalangledegrees)
#plot v1 and v2 and final vector
plt.plot([0,v1.magnitude*cos((v1.angle)*(pi/180))],[0,v1.magnitude*sin((v1.angle)*(pi/180))])
plt.plot([0,v2.magnitude*cos((v2.angle)*(pi/180))],[0,v2.magnitude*sin((v2.angle)*(pi/180))])
plt.plot([0,xcomponents],[0,ycomponents])
plt.show()

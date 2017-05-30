#Projectile motion (2 dimensional)
import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(0,40,50)
m=1
u=200
g=-9.8

def v(t):
	return u+g*t
def a(t):
	return [g]*len(t)

def y(t):
	return u*t+0.5*g*t**2.0
def KE(t):
	return (0.5)*m*v(t)**2.0
def PE(t):
	return -m*g*y(t)
def E(t):
	return KE(t)+PE(t)
	
plt.figure()

plt.subplot(3,1,1)
plt.plot(t,y(t),'bo')
plt.title('2-dimensional Motion Along Y-axis')
plt.xlabel('time ($s$)')
plt.ylabel('displacement($m$)')

plt.subplot(3,1,2)
plt.plot(t,v(t),'ro')
plt.xlabel('time($s$)')
plt.ylabel('velocity($m/s$)')

plt.subplot(3,1,3)
plt.plot(t,a(t),'go')
plt.xlabel('time($s$)')
plt.ylabel('Acceleration($m/s^2$)')



plt.figure()
plt.subplot(3,1,1)
plt.plot(t,KE(t),'bo')
plt.title('Kinetic and Potential Energy')
plt.xlabel('time ($s$)')
plt.ylabel('Kinetic Energy ($J$)')
plt.subplot(3,1,2)
plt.plot(t,PE(t),'ro')
plt.xlabel('time ($s$)')
plt.ylabel('Potential Energy ($J$)')
plt.subplot(3,1,3)
plt.plot(t,E(t),'go')
plt.xlabel('time ($s$)')
plt.ylabel('Total Energy ($J$)')

plt.figure()
plt.plot(t,KE(t),'bo',label="Kinetic Energy")
plt.plot(t,PE(t),'ro',label="Potential Energy")
plt.plot(t,E(t),'g',label="Total Energy")
plt.legend()
plt.show()



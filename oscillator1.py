# Analytical solution of Harmonic Oscillator
#importing numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(0,5,120)  #creating numpy array for time
w=5     #Angular frequency 5 rad/s
A=5     #Amplitude= 5m i.e the position at 5m at t=0
phi=90*(np.pi)/180.0        #Just wanted to add a phase in here, which is not that necessary

# Defining our functions in here
def x(t):
	return A*np.cos(w*t+phi)    #Gives position
def a(t):
	return -w**2*x(t)           #Gives acceleration
def v(t):
	return -A*w*np.sin(w*t+phi) #Gives velocity

	

plt.figure()
plt.plot(t,x(t),'bo-')
plt.title('Undamped simple harmonic oscillator')
plt.xlabel('time ($s$)')
plt.ylabel('displacement($m$)')

plt.figure()
plt.plot(x(t),a(t),'ro-')
plt.title('Acceleration vs displacement')
plt.xlabel('displacement(m)')
plt.ylabel('acceleration($m/s^2$)')
plt.grid()

plt.figure()
plt.plot(t,v(t),'go--')
plt.title("velocity vs time")
plt.xlabel('time(s)')
plt.ylabel('velocity(m/s)')
plt.show()




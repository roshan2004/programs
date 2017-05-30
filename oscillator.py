#Analytical and numerical solution for the motion of a simple harmonic oscillator
import matplotlib.pyplot as plt
import math as m
v=0.0   #initial velocity
h=0.1  #time step
x=5.0   #initial position
w=m.sqrt(10.0)  #sqrt(k/m) where k=10.0 N/m,m=1 Kg

t=0.0
ta,xa,xb,KE,PE,TE=[],[],[],[],[],[]

while t<8.0:
    ta.append(t)
    xa.append(x)
    xb.append(5*m.cos(w*t))  #Analytical solution for the position
    KE.append(0.5*1*v**2.0)       #Kinetic Energy
    PE.append(0.5*10.0*x**2.0)    #Potential Energy
    TE.append(0.5*1*v**2.0+0.5*10.0*x**2.0) #Total Energy
   
    x=x+v*h

    v=v-(10.0/1.0)*x*h    #k=10.0, m=1.0
   
    
    
    
    t=t+h


    
   
    
plt.figure()
plt.title("Analytical and Numerical solution of a"+"\n"+"simple harmonic oscillator")
plt.plot(ta,xa,alpha=7,label="Numerical solution")
plt.plot(ta,xb,'ro--',alpha=0.6,label="Analytical solution")
plt.xlabel('$t(s)$')
plt.ylabel('$x(m)$')
plt.legend()
plt.figure()
plt.plot(ta,KE,'bo-')
plt.plot(ta,PE,'ro-')
plt.plot(ta,TE,'g')
plt.xlabel('$t(s)$')
plt.ylabel('Energy(J)')
plt.show()



from numpy import linspace, sin, loadtxt,cos
from pylab import plot, show,xlabel

x=linspace(0,10,100)
print(x)
y=sin(x)
#plot(x,y)
#show()

a=open("test.dat","w")
for i in range(len(x)):
	a.write("%.2f %.2f\n" % (x[i],y[i]))
a.close()
b=loadtxt("test.dat",float)
plot(b[:,0],b[:,1],"r--")
g=cos(x)
xlabel("Radianes")
plot(x,g,"ko")
show()

from numpy import  loadtxt, linspace,zeros
from pylab import plot, show,xlim,xlabel,ylabel

xlim(0,1000)
x=linespace(0,1000,1)
b=loadtxt("sunspots.txt",float)
xlabel("mes")
ylabel("manchas")
plot(b[:,0],b[:,1],"b")
r=5
l=zeros([1000],float)

for i in range(5,1001):
	s=0
	for n in range(-r,r):
		a=b[i+n,1]
		s=s+a
	g=(s/11)
	l[i-1]=g
plot(x,l)
plot(b[:,0],b[:,1],"r")
show()      


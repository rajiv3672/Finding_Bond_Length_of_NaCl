'''
Rajiv Das
2015 132 036


The equation you gave (U=-(e^2/4πϵr^2)+exp(-r/r0)) was easy to handle by hand but
hard to handle by computer(I found to do so).
So I used a equivalent equation ##U=4ε[(σ/x)^12-(σ/x)^6]## which is Lennard Jones Potential
reff: Introduction to Solid State Physics by Charles Kittel ,p58. Eventually both give same result.
'''

import matplotlib.pyplot as plt#Just for plot.

h=10**-8#Difference of two consecutive x values
ε=4.24#ε=Binding energy at equilibrium measured in eV
σ=2.11#σ=x0/1.12:x0 here is distance of equilibrium
def f(x):#Function for calculating force
    F=-4*ε*((-12)*(σ**12)*(x**-13)-(-6)*(σ**6)*(x**-7))#The force equation derived from F=-dU/dx
    return F
c=0
print("Please don't enter x grater than σ=2.11 Angstrom \notherwise it will give derivative at infinity.")
x=float(input("Input app. root in Angstrom:"))
while(1):
    D=(f(x+h)-f(x))/h#Derivative
    z=x-f(x)/D#Newton-Raphson method
    if(z==x):
        print("Root or bond length is={}Angstrom".format(round(z,6)))
        break
    else:
        x=z
    c=c+1
i=2.2
X=[]
Y=[]
while(i<5):#loop for plot
    i=i+0.001
    X.append(i)
    Y.append(f(i))
print("Iteration number in loop={}".format(c))
plt.axvline(linewidth=1.1,color='b',linestyle='--')
plt.axhline(linewidth=1.1,color='b',linestyle='--')
plt.grid(color='r', linestyle='--', linewidth=.5)
plt.plot(X,Y,'m')
plt.plot(z,f(z),'ko')
plt.xlabel('r in Angstrom→→')
plt.ylabel('Force→→')
plt.title('F vs r curve')
plt.show()
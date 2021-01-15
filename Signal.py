#Cree sur EduPython 3.0
#Par Arial Nathan , en BTS SN
#Le 15/01/2021

from lycee import *
from matplotlib import pyplot

#CARACTÉRISTIQUES :
tmax=0.05 #durée du signal (absice)
T=0.02 #période
ω=2*pi/T #pulsation.
#φ=pi/2 #phase à l'origine
Umax=20/pi #amplitude

repere = pyplot.axes(xlim=(0, tmax), ylim=(-10, 10))
repere.set_xlabel('t')
repere.set_ylabel('tension U')
repere.set_title("Signal sinusoïdal/Carré")

n=500 #nombre d'intervalles

t=[k*tmax/n for k in range(n+1)] #liste des n+1 valeurs de t [0,n] (axe des abscisses)

# la fondamental
# U=[Umax*(sin(ω*t)) for t in t]

# Pour rajouté un harmony "+sin(h*ω*t)/h"
U=[Umax*(sin(ω*t)+sin(3*ω*t)/3+sin(5*ω*t)/5+sin(7*ω*t)/7+sin(9*ω*t)/9+sin(11*ω*t)/11) for t in t] #calcul des n+1 valeurs de U

repere.plot(t,U)
pyplot.show()
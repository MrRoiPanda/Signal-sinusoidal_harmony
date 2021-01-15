# View signal

>Created with [EduPython 3.0](https://edupython.tuxfamily.org/)

## Usage

To run , execute `Signal.py` in EduPython.

## Code

- Librery used
```Python
from lycee import *
from matplotlib import pyplot
```
- Signal characteristic
```Python
tmax=0.05 #durée du signal (absice)
T=0.02 #période
ω=2*pi/T #pulsation.
#φ=pi/2 #phase à l'origine
Umax=20/pi #amplitude
````
```Python
n=500 #nombre d'intervalles

t=[k*tmax/n for k in range(n+1)] #liste des n+1 valeurs de t [0,n] (axe des abscisses)

# la fondamental
# U=[Umax*(sin(ω*t)) for t in t]

# Pour rajouté un harmony "+sin(h*ω*t)/h"
U=[Umax*(sin(ω*t)+sin(3*ω*t)/3) for t in t] #calcul des n+1 valeurs de U

repere.plot(t,U)
pyplot.show()
```

# View signal

>Created with [EduPython 3.0](https://edupython.tuxfamily.org/)

## Usage

To run , execute `Signal.py`

## Code

### Librery used :
```Python
from lycee import *
from matplotlib import pyplot
```
### Signal characteristic :
```Python
tmax=0.05 #durée du signal (absice)
T=0.02 #période
ω=2*pi/T #pulsation.
#φ=pi/2 #phase à l'origine
Umax=20/pi #amplitude
````
### Number of points :
```Python
n=500 #nombre d'intervalles
```
### Square signal generate with one harmony :
```Python
t=[k*tmax/n for k in range(n+1)] #liste des n+1 valeurs de t [0,n] (axe des abscisses)
U=[Umax*(sin(ω*t)+sin(3*ω*t)/3) for t in t] #calcul des n+1 valeurs de U
```

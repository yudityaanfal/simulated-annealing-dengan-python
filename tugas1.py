from math import sin, cos, exp, sqrt
import random

def hitung_E(q,w):
	return -(sin(q)*cos(w)+ (4/5)*exp(1-sqrt(q*q+w*w)))

x1=round((random.uniform(-10,10)),2)
x2=round((random.uniform(-10,10)),2)

E=hitung_E(x1,x2)

best_x1=x1
best_x2=x2
best_E=E

T=10000
while T!=0:
	x1b=round((random.uniform(-10,10)),2)
	x2b=round((random.uniform(-10,10)),2)
	Eb=hitung_E(x1b,x2b)
	delta_E=Eb-E
	if delta_E<0:
		x1=x1b
		x2=x2b
		E=Eb
		if Eb<best_E:
			best_x1=x1b
			best_x2=x2b
			best_E=Eb
	else :
		p=exp(-delta_E/T)
		r=random.randint(0,1)
		if r<p:
			x1=x1b
			x2=x2b
			E=Eb
	delta_T=10	
	T =T/delta_T

print(best_x1,best_x2,best_E)

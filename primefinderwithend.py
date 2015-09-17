#This deserves to die slowly.

def primefinder(end):
	global c
	c,a = -1,1
	while a<end:
		while c == 0:
			a += 1
			for b in range(2,int(a**.5)+1):
				if a%b != 0:
					c = 1
		print(int(a))
		c = 0

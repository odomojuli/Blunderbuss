from operator import mul
from itertools import product

# w,x,y,z = 2,2,3,2
#   for i in range(w*x*y*z):
#       print (i/x/y/z, i%(x*y*z)/y/z, i%(y*z)/z, i%z)

i = 'i'
f = "print "
n = ['w','x','y','z']	# names

#v = [2,2,3,2]
#print ','.join(n) + '=' + ','.join(map(str,v))

print "for %s in range(%s):" % (i, '*'.join(n))
t = ""
for k in range(len(n)):
	t += i 
	if k:
		t += '%'
	if k < len(n)-1:
		if k:
			t += "(%s)" % '*'.join(n[k:])
		t += '/' + '/'.join(n[k+1:])
		t += ', '
	else:
		t += n[k]

print "\t%s(%s)" % (f,t)
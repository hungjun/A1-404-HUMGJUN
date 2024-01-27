
import random
xs = []
ys = []
TOTAL_POINTS = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
RADIUS = 10000000000000000000000000000000000000000000
pt = 0
for i in range(TOTAL_POINTS):
	xs.append(random.randint(0,RADIUS))
	ys.append(random.randint(0,RADIUS))
for i in range(TOTAL_POINTS):
	if (xs[i]*xs[i] + ys[i]*ys[i]) < 1000000:
		pt=pt + 1
monteCarlopi = float(pt)/TOTAL_POINTS * 4.0

print("pi: " + str(monteCarlopi))
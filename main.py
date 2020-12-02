import os, sys, time
from random import random, seed
from math import atan2, cos, hypot, pi, sin, sqrt
os.chdir('/Users/cy4n/Desktop/python/science')
import color, particle

# retro graphics
def ascii2(w, q1, q2, t):
	newq1 = sorted(q1)
	newq2 = sorted(q2)
	newt = sorted(t)
	s = ''
	#l = 0
	for l in xrange(w[0] * w[1]):
		this = ' '
		if newt != []:
			if l == newt[0]:
				this = '.'
				del newt[0]

		if newq1 != []:
			if l == newq1[0]:
				this = '+'
				del newq1[0]

		if newq2 != []:
			if l == newq2[0]:
				this = '@'
				del newq2[0]

		s += this

	print s

def particlegen(str, m, n):
	s = 0
	for i, c in enumerate(str):
		i += 1
		s += 2 ** i * ord(c)

	seed(s)
	particles = [particle.particle(0.06, [0., 0.], [0., 0.])]
	i = 0
	while i < n:
		r = random() * 32
		theta = random() * 2 * pi
		r = [r * cos(theta), r * sin(theta)]
		v = [sqrt(random()) * cos(theta + pi/2) * 0.1, sqrt(random()) * sin(theta + pi/2) * 0.1]
		particles.append(particle.particle((m / n) * random() * 2, r, v))
		i += 1

	return particles

def loadingdots(n, d):
	n %= d
	n += 1
	sys.stdout.write('\rLoading' + ('.' * n) + ' ' * (d - n))
	sys.stdout.flush()

#print particleGen(1)

scale = 14983518130


w = (128, 48)
userseed = raw_input('str seed = ')

usertime = input('int time = ')


particles = particlegen(str(userseed), 0.000014, 200) #seed, 30

i = 0
while i < -2000:
	for particle in particles:
		particle.increment(particle.g(particles))

	if i % 100 == 0:
		loadingdots(i/100, 4)
		for particle in particles:
			if abs(particle.l[0] - 32) > 48 or abs(particle.l[1] - 24 ) > 48:
				particles.remove(particle)
	i += 1

pthing = []
for t in xrange(usertime):
	seed(t)
	for _ in xrange(30):
		sunr = [particles[0].r[0] - 20, particles[0].r[1]]
		for particle in particles:
			particle.increment(particle.g(particles))
			particle.getLoc(w, particles[0].r)
			if particle.trail:
				pthing.append([particle.loc, t + random() * 5])

	ploc1 = []
	ploc2 = []
	ptrail = []
	for particle in particles:
		if abs(particle.l[0] - 32) > 32 or abs(particle.l[1] - 24) > 32:
			particles.remove(particle)

		else:
			if particle.trail:
				ploc2.append(particle.loc)

			else:
				ploc1.append(particle.loc)

	for dot in pthing:
		if dot[1] <= t:
			pthing.remove(dot)

		else:
			ptrail.append(dot[0])

	ascii2(w, set(ploc1), set(ploc2), set(ptrail))

	if len(particles) != 1:
		time.sleep(1./40.)
		t += 1

	else:
		t += 10000000000

for particle in particles:
	print str(particle.getMass()) + ' mE\n',

#ascii2(w, set(ploc1), set(ploc2), set(ptrail))

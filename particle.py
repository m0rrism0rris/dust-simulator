from math import atan2, sin, cos, hypot
class particle:
	def __init__(this, mu, r, v):
		#this.cm = cm
		this.mu = mu
		this.r = r
		this.v = v
		this.l = [0, 0]
		this.loc = 0
		this.trail = False

	def increment(this, a):
		this.v[0] += a[0]
		this.v[1] += a[1]
		this.r[0] += this.v[0]
		this.r[1] += this.v[1]
		#this.loc = (int((this.r[0]) * 2) + (int(this.r[1]) * 128)) % (128*48)

	def getLoc(this, w, o):
		this.l[0] = this.r[0] + w[0]/4 - o[0]
		this.l[1] = this.r[1] + w[1]/2 - o[1]
		this.loc = int(min(max(this.l[0], 0), w[0]/2 - 1) * 2) + int(min(max(this.l[1], 0), w[1] - 1)) * w[0]

	def collide(this, particle):
		m = this.mu + particle.mu
		this.v[0] = (this.v[0] * this.mu + particle.v[0] * particle.mu) / m
		this.v[1] = (this.v[1] * this.mu + particle.v[1] * particle.mu) / m
		this.mu = m
		this.trail = True

	def g(this, particles):
		ax = 0.
		ay = 0.
		for p in particles:
			if p != this:
				rx = p.r[0] - this.r[0]
				ry = p.r[1] - this.r[1]
				r = hypot(rx, ry)
				if r <= .2:
					this.collide(p)
					particles.remove(p)

				else:
					theta = atan2(ry, rx)
					a = p.mu / r ** 2
					ax += a * cos(theta)
					ay += a * sin(theta)

		return [ax, ay]

	def getVelocity(this):
		return hypot(this.v[0], this.v[1]) * 5549100

	def getMass(this):
		return this.mu * 5549100

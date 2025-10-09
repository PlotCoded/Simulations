import pygame, math

pygame.init()

dimensions = pygame.display.get_desktop_sizes()
screen = pygame.display.set_mode((dimensions[0][0], dimensions[0][1]-60))
pygame.display.set_caption("Projectile")

running = True

vectors = {1: 180, 1: 180, 1:180} #Magnitude: Direction

# Positions
HorVects = dimensions[0][0]/2
VerVects = dimensions[0][1]/2-30

# Velicities
HorVel = 0
VerVel = 0

# Scaling
scale = 4

# Resolving horizontal and vertical vectors
for a, b in vectors.items():
	HorVel+=(a*math.cos(math.radians(b)) / scale)
	VerVel-=(a*math.sin(math.radians(b)) / scale)

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill((0,0,0))

	# Drawing/ Ploting graph
	pygame.draw.line(screen, (255,255,255), (0,dimensions[0][1]/2-30), (dimensions[0][0], dimensions[0][1]/2-30)) # X-axis
	pygame.draw.line(screen, (255,255,255), (dimensions[0][0]/2, 0), (dimensions[0][0]/2, dimensions[0][1])) # Y-axis

	# Projectile
	pygame.draw.circle(screen, (255,255,255), (HorVects,VerVects), int(16 / scale), int(16 / scale))

	# Getting resultant vector and its direction
	pygame.draw.line(screen, (255,255,255), (dimensions[0][0]/2, dimensions[0][1]/2-30), (HorVects, VerVects)) # Y-axis
	print("Magnitude of Vector is: ", math.sqrt((HorVel**2) + (VerVel**2)) * scale)
	print("Direction of Vector is: ", math.atan((-1 * VerVel))/HorVel)

	# Moving the ball
	HorVects+=HorVel
	VerVects+=VerVel

	# print(HorVects, VerVects)
	pygame.display.update()
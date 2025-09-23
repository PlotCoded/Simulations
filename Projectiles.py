import pygame, math

pygame.init()

screen = pygame.display.set_mode((900,400))
pygame.display.set_caption("Projectile")

running = True

X = 0+8
Y = 300-8

Degree = 4
Radians = math.radians(Degree)
InitialVelocity = 10 #0.1px per frame <==> 10m/s
HorizontalVelocity = X + InitialVelocity * math.cos(Radians)
VerticalVelocity = Y + InitialVelocity * math.sin(Radians)
Acceleration = 9.81

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill((0,0,0))
	pygame.draw.circle(screen, (255,255,255), (HorizontalVelocity,VerticalVelocity), 8, 8)
	HorizontalVelocity+=0.01 * InitialVelocity * math.cos(Radians)
	# VerticalVelocity-=0.01 * InitialVelocity * math.sin(Radians)
	# pygame.draw.line(screen, (255,255,255), (HorizontalVelocity, VerticalVelocity), (HorizontalVelocity+0.01, VerticalVelocity))
	# screen.draw.fill_circle((0+8,300-8), 8, (255,0,0))
	# pygame.draw.rect(screen, (0,0,0), (0, 300, 900, 100))
	pygame.display.update()
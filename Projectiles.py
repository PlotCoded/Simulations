import pygame, math

pygame.init()

screen = pygame.display.set_mode((1400,800))
pygame.display.set_caption("Projectile")

running = True

#0.01px per frame <==> 1m/s

Degree = -15
Radians = math.radians(Degree)
InitialVelocity = 12 # 1000m/s
HorizontalPosition = 0
VerticalPosition = 0
Acceleration = 0.981 # 9.81m/s^2
time = 0

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill((0,0,0))
	pygame.draw.circle(screen, (255,255,255), (HorizontalPosition,VerticalPosition), 8, 8)
	HorizontalPosition = time * (InitialVelocity * math.cos(Radians)) + 300 # Position (Distance) = Incrementation (px movement per frame) (Time) * Velocity
	VerticalPosition = ((time * InitialVelocity * math.sin(Radians)) + 0.5 * (Acceleration) * (time**2)) + 100 # S = Ut + (1/2)(g)(t^2) + C
	time+=0.02

	print(f"Rate of change of vertical displacement or velocity: {(((time+0.02) * InitialVelocity * math.sin(Radians)) + 0.5 * (Acceleration) * ((time+0.02)**2) + 100)- ((time * InitialVelocity * math.sin(Radians) + 0.5 * (Acceleration) * (time**2) + 100))} at time = {time}")
	V = (((time+0.02) * InitialVelocity * math.sin(Radians)) + 0.5 * (Acceleration) * ((time+0.02)**2) + 100)- ((time * InitialVelocity * math.sin(Radians) + 0.5 * (Acceleration) * (time**2) + 100))
	V2 = (((time+0.04) * InitialVelocity * math.sin(Radians)) + 0.5 * (Acceleration) * ((time+0.04)**2) + 100) - (((time+0.02) * InitialVelocity * math.sin(Radians)) + 0.5 * (Acceleration) * ((time+0.02)**2) + 100)
	
	print(f"Rate of change of rate of change of displacement or Acceleration: {V2 - V}")
	# Drawing angle line
	# screen.draw.fill_circle((0+8,300-8), 8, (255,0,0))
	# pygame.draw.rect(screen, (0,0,0), (0, 300, 900, 100))
	pygame.display.update()
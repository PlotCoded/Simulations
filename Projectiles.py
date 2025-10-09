import pygame, math, time as Time

pygame.init()

dimensions = pygame.display.get_desktop_sizes()
screen = pygame.display.set_mode((dimensions[0][0], dimensions[0][1]-60))
pygame.display.set_caption("Projectile")

running = True

Degree = -45
Radians = math.radians(Degree)
InitialVelocity = 30 # 30 m/s
HorizontalPosition = 0
VerticalPosition = 0
Acceleration = 9.81 # 9.81m/s^2
Acceleration*=0.1
ground = 400
time = 0

Start = Time.time()

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill((0,0,0))

	if VerticalPosition <= ground: 
		pygame.draw.circle(screen, (255,255,255), (HorizontalPosition,VerticalPosition), 8, 8)
		HorizontalPosition = time * (InitialVelocity * math.cos(Radians)) + 300 # Position (Distance) = Incrementation (px movement per frame) (Time) * Velocity
		VerticalPosition = ((time * InitialVelocity * math.sin(Radians)) + 0.5 * (Acceleration) * (time**2)) + ground # S = Ut + (1/2)(g)(t^2) + C
		time+=0.0356

		# Testing
		print(f"Rate of change of vertical displacement or velocity: {(((time+0.02) * InitialVelocity * math.sin(Radians)) + 0.5 * (Acceleration) * ((time+0.02)**2) + 100)- ((time * InitialVelocity * math.sin(Radians) + 0.5 * (Acceleration) * (time**2) + 100))} at time = {time}")
		V = (((time+0.02) * InitialVelocity * math.sin(Radians)) + 0.5 * (Acceleration) * ((time+0.02)**2) + 100)- ((time * InitialVelocity * math.sin(Radians) + 0.5 * (Acceleration) * (time**2) + 100))
		V2 = (((time+0.04) * InitialVelocity * math.sin(Radians)) + 0.5 * (Acceleration) * ((time+0.04)**2) + 100) - (((time+0.02) * InitialVelocity * math.sin(Radians)) + 0.5 * (Acceleration) * ((time+0.02)**2) + 100)
		
		print(f"Rate of change of rate of change of displacement or Acceleration: {V2 - V}")
	else: 
		End = Time.time()
		print(End-Start)

		print(f"The times when it was on the ground are {0.00} and {time}")
		print(f"Time taken to reach Max Height is {time/2}")
		print(f'Horizontal distance is {HorizontalPosition}')
		pygame.draw.circle(screen, (255,255,255), (HorizontalPosition,VerticalPosition), 8, 8)

		running = False #Testing

	# Displaying real world details like time, height, angle, etc

	pygame.draw.line(screen, (255,255,255), (0,ground+8), (dimensions[0][0], ground+8))

	pygame.display.update()
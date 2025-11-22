import pygame, math

pygame.init()

dimensions = pygame.display.get_desktop_sizes()
screen = pygame.display.set_mode((dimensions[0][0], dimensions[0][1]-60))
pygame.display.set_caption("Moments and Torque")

# Creating pivot
pygame.draw.polygon(screen, (255,255,255), ((dimensions[0][0]/2, dimensions[0][1]/2), (dimensions[0][0]/2-30, dimensions[0][1]/2 + 30), (dimensions[0][0]/2+30, dimensions[0][1]/2 + 30)))
lever_image = pygame.image.load("Pivot.png").convert_alpha()
lever_rect = lever_image.get_rect(center=(dimensions[0][0]/2, dimensions[0][1]/2-48))
screen.blit(lever_image, lever_rect)

# Angle and rotation
angle = 0

sum_of_anticlockwise_moments = 5 # Left side
sum_of_clockwise_moments = 4 # Right side

# Note: The length of the lever is 180cm, mass is in kg, distance is in cm, default acceleration is9.8ms^-1, so moments is in Ncm^-1

# Calculating the resulting moments and angular speed at each moment(time)
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill((0,0,0)) # Setting background color

	# Displaying the pivot
	screen.blit(lever_image, lever_rect)
	pygame.draw.polygon(screen, (255,255,255), ((dimensions[0][0]/2, dimensions[0][1]/2), (dimensions[0][0]/2-90, dimensions[0][1]/2 + 90), (dimensions[0][0]/2+90, dimensions[0][1]/2 + 90)))

	# Rotating the lever
	if angle <= 45 and angle >= -45:
		lever_image = pygame.image.load("Pivot.png").convert_alpha()
		lever_image = pygame.transform.rotate(lever_image, angle)
		if sum_of_clockwise_moments > sum_of_anticlockwise_moments:
			# Calculating angular speed
			angle-=0.01
		elif sum_of_clockwise_moments < sum_of_anticlockwise_moments:
			# Calculating angular speed
			angle+=0.01
		else:
			angle = 0
		lever_rect = lever_image.get_rect(center=(dimensions[0][0]/2, dimensions[0][1]/2))
	# pygame.draw.circle(screen, (255,255,255), (dimensions[0][0]/2, dimensions[0][1]/2), 8, 8)

	pygame.display.update()
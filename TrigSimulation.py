import pygame, math, time as Time

pygame.init()

dimensions = pygame.display.get_desktop_sizes()
screen = pygame.display.set_mode((dimensions[0][0], dimensions[0][1]-60))
pygame.display.set_caption("Trig Simulation")

running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill((0,0,0))

	pygame.display.update()
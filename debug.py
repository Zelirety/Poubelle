import pygame
pygame.init()
font = pygame.font.Font(None,30)
""" Permet d'afficher sous forme de texte et a l'écran une variable, expression booléenne, etc..."""


def debug1(info,y = 10, x = 500):
	display_surface = pygame.display.get_surface()
	debug_surf = font.render(str(info),True,'White')
	debug_rect = debug_surf.get_rect(topleft = (x,y))
	pygame.draw.rect(display_surface,'Black',debug_rect)
	display_surface.blit(debug_surf,debug_rect)


def debug2(info,y = 10, x = 60):
	display_surface = pygame.display.get_surface()
	debug_surf = font.render(str(info),True,'White')
	debug_rect = debug_surf.get_rect(topleft = (x,y))
	pygame.draw.rect(display_surface,'Black',debug_rect)
	display_surface.blit(debug_surf,debug_rect)

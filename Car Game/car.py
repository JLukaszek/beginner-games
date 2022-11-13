import pygame
import sys
import random

pygame.init()
screen_width = 770
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Car Game")
clock = pygame.time.Clock()
text_font = pygame.font.Font(None, 40)
game_status = False

# Graphics
# background
menu_surf = pygame.image.load('graphics/main_menu_workshop.png')
road_surf = pygame.image.load('graphics/road.png')
road_surf = pygame.transform.rotozoom(road_surf, 90, 0.5)
road_surf_rect = road_surf.get_rect()
road_surf_x1, road_surf_y1, road_surf_y2 = 0, 0, 0
road_surf_x2 = road_surf_rect.width
scrolling_speed = 3

# cars
blue_car_surf = pygame.image.load('graphics/blue_car.png')
red_car_surf = pygame.image.load('graphics/red_car.png')
green_car_surf = pygame.image.load('graphics/green_car.png')
blue_car_side = pygame.image.load('graphics/car_purple_side.png')
red_car_side = pygame.image.load('graphics/car_red_side.png')
green_car_side = pygame.image.load('graphics/car_green_side.png')
green_car_side_rect = green_car_side.get_rect(center=(385, 300))
cars = [blue_car_surf, green_car_surf, red_car_surf]
final_car_surf = pygame.transform.rotozoom(random.choice(cars), 0, 0.05)

# Car
car_rect = final_car_surf.get_rect(center=(100, 147))
car_position = 0
fuel = 100


# Obstacles
truck_surf = pygame.image.load('graphics/truck.png')
truck_surf = pygame.transform.rotozoom(truck_surf, 90, 1.35)
truck_rect = truck_surf.get_rect(center=(900, random.choice([52, 142, 236])))
obstacle_position_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_position_timer, 1000)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_status:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                car_position -= 8
            if event.type == pygame.KEYUP and event.key == pygame.K_UP:
                car_position = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                car_position += 8
            if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                car_position = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type == obstacle_position_timer:
            fuel -= 2

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_status = True

    if game_status:
        road_surf_x1 -= scrolling_speed
        road_surf_x2 -= scrolling_speed
        if road_surf_x1 <= -road_surf_rect.width:
            road_surf_x1 = road_surf_rect.width
        if road_surf_x2 <= -road_surf_rect.width:
            road_surf_x2 = road_surf_rect.width
        screen.blit(road_surf, (road_surf_x1, road_surf_y1))
        screen.blit(road_surf, (road_surf_x2, road_surf_y2))
        pygame.draw.rect(screen, 'black', (300, 300, 100, 20))
        pygame.draw.rect(screen, 'yellow', (300, 300, fuel, 20))
        # Obstacle movement
        truck_rect.x -= 6
        if truck_rect.right < -20:
            truck_rect.x = 900
            truck_rect = truck_surf.get_rect(center=(1000, (random.choice([52, 142, 236]))))
        screen.blit(truck_surf, truck_rect)

        # Car movement
        car_rect.y += car_position
        if car_rect.top <= 20:
            car_rect.top = 20
            car_position = 0

        if car_rect.bottom >= 270:
            car_rect.bottom = 270
            car_position = 0
        screen.blit(final_car_surf, car_rect)

    else:
        screen.blit(menu_surf, (0, 0))
        screen.blit(green_car_side, green_car_side_rect)

    pygame.display.update()
    clock.tick(60)

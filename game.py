import pygame
from pygame.locals import *
from sprites import Sprite
import sys

def main():
    pygame.init()

    GAME = pygame.display.set_mode((928,793),0,60)
    pygame.display.set_caption('Sword man')
    pygame.display.set_icon(pygame.image.load('assets/img/icon.png'))
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    '''animations''' #https://aamatniekss.itch.io/fantasy-knight-free-pixelart-animated-character, #https://edermunizz.itch.io/free-pixel-art-forest
    #idle
    idle_right = pygame.image.load("assets/img/_idle.png")
    idle_anim_right = Sprite(idle_right)
    idle_left = pygame.image.load("assets/img/_idle_left.png")
    idle_anim_left = Sprite(idle_left)
    idle_frames_right = []
    idle_frames_left = []
    idle_slide = 10
    idle_frame = 0

    #run
    run_right = pygame.image.load("assets/img/_run.png")
    run_anim_right = Sprite(run_right)
    run_left = pygame.image.load("assets/img/_run_left.png")
    run_anim_left = Sprite(run_left)
    run_frames_right = []
    run_frames_left = []

    #attack
    att_right = pygame.image.load("assets/img/_attack.png")
    att_anim_right = Sprite(att_right)
    att_left = pygame.image.load("assets/img/_attack_left.png")
    att_anim_left = Sprite(att_left)
    att_frames_right = []
    att_frames_left = []
    att_slide = 4
    att_frame = 0

    #climb
    climb_up = pygame.image.load("assets/img/_climb.png")
    climb_anim = Sprite(climb_up)
    climb_frames = []
    climb_slide = 7
    climb_frame = 0

    #jump
    jump = pygame.image.load("assets/img/_jump.png")
    jump_anim = Sprite(jump)
    jump_left = pygame.image.load("assets/img/_jump_left.png")
    jump_anim_left = Sprite(jump_left)
    jump_frames = []
    jump_frames_left = []
    jump_slide = 5
    jump_frame = 0
    jumping = False
    GRAVITY = 1
    JUMP_HEIGHT = 12
    VELOCTIY = JUMP_HEIGHT


    #enemy
    enemy = pygame.image.load("assets/img/_enemy_left.png")
    enemy_anim = Sprite(enemy)
    enemy_frames = []
    enemy_slide = 7
    enemy_frame = 0
    enemy_x = 400
    enemy_y = 400
    enemy_init_frame = pygame.time.get_ticks()
    enemy_hitbox = [enemy_x + 25, enemy_y + 11, 29, 52]
    enemy_alive = True

    enemy_death = pygame.image.load("assets/img/_enemy_death_left.png")
    enemy_anim_death = Sprite(enemy_death)
    enemy_frames_death = []
    enemy_slide_death = 5
    enemy_frame_death = 0
    enemy_init_frame_death = pygame.time.get_ticks()

    for x in range(idle_slide):
        idle_frames_right.append(idle_anim_right.get_image(x, 120, 80, 3, BLACK))
        idle_frames_left.append(idle_anim_left.get_image(x, 120, 80, 3, BLACK))
        run_frames_right.append(run_anim_right.get_image(x, 120, 80, 3, BLACK))
        run_frames_left.append(run_anim_left.get_image(x, 120, 80, 3, BLACK))

    for x in range(att_slide):
        att_frames_right.append(att_anim_right.get_image(x, 120, 80, 3, BLACK))
        att_frames_left.append(att_anim_left.get_image(x, 120, 80, 3, BLACK))

    for x in range(climb_slide):
        climb_frames.append(climb_anim.get_image(x, 120, 80, 3, BLACK))

    for x in range(jump_slide):
        jump_frames.append(jump_anim.get_image(x, 120, 80, 3, BLACK))
        jump_frames_left.append(jump_anim_left.get_image(x, 120, 80, 3, BLACK))
    
    for x in range(enemy_slide):
        enemy_frames.append(enemy_anim.get_image(x, 150, 150, 3, BLACK))
        enemy_frames_death.append(enemy_anim_death.get_image(x, 150, 150, 3, BLACK))

    '''cooldowns, frame, global vars'''
    cd = 50
    att_cd = 85
    init_frame = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    run = True
    moving = False
    facing = "right"    
    x = 30
    y = 490
    hitbox = [x - 55, y + 11, 29, 52]

    #music
    music = pygame.mixer.Sound("assets/sounds/bg.wav")
    pygame.mixer.Sound.set_volume(music, 0.2)
    pygame.mixer.Sound.play(music)

    def play_attack():
        swordfx = pygame.mixer.Sound("assets/sounds/sword.wav")
        pygame.mixer.Sound.set_volume(swordfx, 0.35)
        pygame.mixer.Sound.play(swordfx)


    #while game running
    while run:
        
        #background
        bg = pygame.image.load("assets/img/bg2.png")
        GAME.blit(bg, (0, 0))
    
        #fps
        clock.tick(90)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYUP:
                moving = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                moving = False

        if hitbox[0] >= enemy_hitbox[0]:
            enemy_alive = False
    
        #key event dict
        key_pressed_is = pygame.key.get_pressed()

        if key_pressed_is[K_SPACE]:
            jumping = True
            moving = True

        if key_pressed_is[K_LEFT] or key_pressed_is[K_a]:
            x -= 8
            hitbox[0] -= 8
            moving = True
            facing = "left"
            if not jumping:
                curr_frame = pygame.time.get_ticks()
                if curr_frame - init_frame >= cd:
                    idle_frame += 1
                    init_frame = curr_frame
                    if idle_frame >= idle_slide:
                        idle_frame = 1
                GAME.blit(run_frames_left[idle_frame], (x, y))

        elif key_pressed_is[K_RIGHT] or key_pressed_is[K_d]:
            x += 8
            hitbox[0] += 8
            moving = True
            facing = "right"
            if not jumping:
                curr_frame = pygame.time.get_ticks()
                if curr_frame - init_frame >= cd:
                    idle_frame += 1
                    init_frame = curr_frame
                    if idle_frame >= idle_slide:
                        idle_frame = 1
                GAME.blit(run_frames_right[idle_frame], (x, y))

        # elif key_pressed_is[K_UP]:
        #     y -= 5
        #     moving = True
        #     curr_frame = pygame.time.get_ticks()
        #     if curr_frame - init_frame >= cd:
        #         climb_frame += 1
        #         init_frame = curr_frame
        #         if climb_frame >= climb_slide:
        #             climb_frame = 1
        #     GAME.blit(climb_frames[climb_frame], (x, y))

        # elif key_pressed_is[K_DOWN]:
        #     y += 5
        #     moving = True
        #     curr_frame = pygame.time.get_ticks()
        #     if curr_frame - init_frame >= cd:
        #         climb_frame += 1
        #         init_frame = curr_frame
        #         if climb_frame >= climb_slide:
        #             climb_frame = 1
        #     GAME.blit(climb_frames[climb_frame], (x, y))

        #attacking
        elif key_pressed_is[K_e] and not jumping:
            moving = True
            if facing == "right":
                curr_frame = pygame.time.get_ticks()
                if curr_frame - init_frame >= att_cd:
                    if att_frame == 0:
                        play_attack()
                    att_frame += 1
                    init_frame = curr_frame
                    if att_frame >= att_slide:
                        att_frame = 0
                GAME.blit(att_frames_right[att_frame], (x, y))
            if facing == "left":
                curr_frame = pygame.time.get_ticks()
                if curr_frame - init_frame >= att_cd:
                    if att_frame == 0:
                        play_attack()
                    att_frame += 1
                    init_frame = curr_frame
                    if att_frame >= att_slide:
                        att_frame = 0
                GAME.blit(att_frames_left[att_frame], (x, y))
        
        #mouse attacking
        elif event.type == pygame.MOUSEBUTTONDOWN and not jumping:
            moving = True
            if facing == "right":
                curr_frame = pygame.time.get_ticks()
                if curr_frame - init_frame >= att_cd:
                    if att_frame == 0:
                        play_attack()
                    att_frame += 1
                    init_frame = curr_frame
                    if att_frame >= att_slide:
                        att_frame = 0
                GAME.blit(att_frames_right[att_frame], (x, y))
            if facing == "left":
                curr_frame = pygame.time.get_ticks()
                if curr_frame - init_frame >= att_cd:
                    if att_frame == 0:
                        play_attack()
                    att_frame += 1
                    init_frame = curr_frame
                    if att_frame >= att_slide:
                        att_frame = 0
                GAME.blit(att_frames_left[att_frame], (x, y))

        #idle animation
        elif (not moving and not jumping) or (event.type == pygame.MOUSEBUTTONUP and not jumping):
            moving = False
            att_frame = 0
            if facing == "right":
                curr_frame = pygame.time.get_ticks()
                if curr_frame - init_frame >= cd:
                    idle_frame += 1
                    init_frame = curr_frame
                    if idle_frame >= idle_slide:
                        idle_frame = 1
                GAME.blit(idle_frames_right[idle_frame], (x, y))

            if facing == "left":
                curr_frame = pygame.time.get_ticks()
                if curr_frame - init_frame >= cd:
                    idle_frame += 1
                    init_frame = curr_frame
                    if idle_frame >= idle_slide:
                        idle_frame = 1
                GAME.blit(idle_frames_left[idle_frame], (x, y))

        #jump
        if jumping:
            y -= VELOCTIY
            VELOCTIY -= GRAVITY
            if VELOCTIY < -JUMP_HEIGHT:
                jumping = False
                VELOCTIY = JUMP_HEIGHT 
            if facing == "right":
                curr_frame = pygame.time.get_ticks()
                if curr_frame - init_frame >= cd:
                    jump_frame += 1
                    init_frame = curr_frame
                    if jump_frame >= jump_slide:
                        jump_frame = 0
                GAME.blit(jump_frames[jump_frame], (x, y))
            if facing == "left":
                curr_frame = pygame.time.get_ticks()
                if curr_frame - init_frame >= cd:
                    jump_frame += 1
                    init_frame = curr_frame
                    if jump_frame >= jump_slide:
                        jump_frame = 0
                GAME.blit(jump_frames_left[jump_frame], (x, y))

        #enemy
        if enemy_alive:
            curr_frame = pygame.time.get_ticks()
            if curr_frame - enemy_init_frame >= cd:
                enemy_frame += 1
                enemy_init_frame = curr_frame
                if enemy_frame >= enemy_slide:
                    enemy_frame = 1
            GAME.blit(enemy_frames[enemy_frame], (enemy_x, enemy_y))
        else:
            curr_frame = pygame.time.get_ticks()
            if curr_frame - enemy_init_frame_death >= att_cd:
                enemy_frame_death += 1
                enemy_init_frame_death = curr_frame
                if enemy_frame_death >= enemy_slide_death:
                    enemy_frame_death -= 1
                    pass
            GAME.blit(enemy_frames_death[enemy_frame_death], (enemy_x+110, enemy_y))

        pygame.display.update()


if __name__ == '__main__':
    main()
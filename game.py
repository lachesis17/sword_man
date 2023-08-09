import pygame
from pygame.locals import *
from sprites import Sprite

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

    #music
    music = pygame.mixer.Sound("assets/sounds/bg.wav")
    pygame.mixer.Sound.set_volume(music, 0.2)
    pygame.mixer.Sound.play(music)

    #while game running
    while run:
        
        #background
        bg = pygame.image.load("assets/img/bg2.png")
        GAME.blit(bg, (0, 0))
    
        #fps
        clock.tick(120)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            if event.type == pygame.KEYUP:
                moving = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                moving = False
    
        #key event dict
        key_pressed_is = pygame.key.get_pressed()

        if key_pressed_is[K_SPACE]:
            jumping = True
            moving = True

        if key_pressed_is[K_LEFT]:
            x -= 8
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

        elif key_pressed_is[K_RIGHT]:
            x += 8
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
        elif key_pressed_is[K_e]:
            moving = True
            swordfx = pygame.mixer.Sound("assets/sounds/sword.wav")
            pygame.mixer.Sound.set_volume(swordfx, 0.45)
            pygame.mixer.Sound.play(swordfx)
            if facing == "right":
                curr_frame = pygame.time.get_ticks()
                if curr_frame - init_frame >= att_cd:
                    att_frame += 1
                    init_frame = curr_frame
                    if att_frame >= att_slide:
                        att_frame = 0
                GAME.blit(att_frames_right[att_frame], (x, y))
            if facing == "left":
                curr_frame = pygame.time.get_ticks()
                if curr_frame - init_frame >= att_cd:
                    att_frame += 1
                    init_frame = curr_frame
                    if att_frame >= att_slide:
                        att_frame = 0
                GAME.blit(att_frames_left[att_frame], (x, y))
        
        #mouse attacking
        elif event.type == pygame.MOUSEBUTTONDOWN:
            moving = True
            if facing == "right":
                curr_frame = pygame.time.get_ticks()
                if curr_frame - init_frame >= att_cd:
                    att_frame += 1
                    init_frame = curr_frame
                    if att_frame >= att_slide:
                        att_frame = 0
                GAME.blit(att_frames_right[att_frame], (x, y))
            if facing == "left":
                curr_frame = pygame.time.get_ticks()
                if curr_frame - init_frame >= att_cd:
                    att_frame += 1
                    init_frame = curr_frame
                    if att_frame >= att_slide:
                        att_frame = 0
                GAME.blit(att_frames_left[att_frame], (x, y))
            swordfx = pygame.mixer.Sound("assets/sounds/sword.wav")
            pygame.mixer.Sound.set_volume(swordfx, 0.45)
            pygame.mixer.Sound.play(swordfx)

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

        pygame.display.update()


if __name__ == '__main__':
    main()
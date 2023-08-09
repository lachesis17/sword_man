from sprites import Sprite
import pygame
from pygame.locals import *

BLACK = (0, 0, 0)
GRAVITY = 1
JUMP_HEIGHT = 12
VELOCTIY = JUMP_HEIGHT

'''animations''' #https://aamatniekss.itch.io/fantasy-knight-free-pixelart-animated-character, #https://edermunizz.itch.io/free-pixel-art-forest
#https://www.techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/pygame-collision

class Player(object):
    def __init__(self, x, y):
        self.cd = 50
        self.att_cd = 85
        self.init_frame = pygame.time.get_ticks()
        self.moving = False
        self.jumping = False
        self.facing = "right"    
        self.x = 30
        self.y = 490
        self.hitbox = [self.x - 55, self.y + 11, 29, 52]

        '''images'''
        self.idle_right = pygame.image.load("assets/img/_idle.png")
        self.idle_left = pygame.image.load("assets/img/_idle_left.png")
        self.run_right = pygame.image.load("assets/img/_run.png")
        self.run_left = pygame.image.load("assets/img/_run_left.png")
        self.att_right = pygame.image.load("assets/img/_attack.png")
        self.att_left = pygame.image.load("assets/img/_attack_left.png")
        self.climb_up = pygame.image.load("assets/img/_climb.png")
        self.jump = pygame.image.load("assets/img/_jump.png")
        self.jump_left = pygame.image.load("assets/img/_jump_left.png")

        '''fill animation slides'''
        self._idle_anim()
        self._run_anim()
        self._attack_anim()
        self._climb_anim()
        self._jump_anim()


    def _idle_anim(self):
        #idle
        idle_anim_right = Sprite(self.idle_right)
        idle_anim_left = Sprite(self.idle_left)
        idle_frames_right = []
        idle_frames_left = []
        self.idle_slide = 10
        idle_frame = 0

        for x in range(self.idle_slide):
            idle_frames_right.append(idle_anim_right.get_image(x, 120, 80, 3, BLACK))
            idle_frames_left.append(idle_anim_left.get_image(x, 120, 80, 3, BLACK))

    #run
    def _run_anim(self):
        run_anim_right = Sprite(self.run_right)
        run_anim_left = Sprite(self.run_left)
        run_frames_right = []
        run_frames_left = []
        for x in range(self.idle_slide):
            run_frames_right.append(run_anim_right.get_image(x, 120, 80, 3, BLACK))
            run_frames_left.append(run_anim_left.get_image(x, 120, 80, 3, BLACK))

    #attack
    def _attack_anim(self):
        att_anim_right = Sprite(self.att_right)
        att_anim_left = Sprite(self.att_left)
        att_frames_right = []
        att_frames_left = []
        att_slide = 4
        att_frame = 0
        for x in range(att_slide):
            att_frames_right.append(att_anim_right.get_image(x, 120, 80, 3, BLACK))
            att_frames_left.append(att_anim_left.get_image(x, 120, 80, 3, BLACK))

    #jump
    def _jump_anim(self):
        jump_anim = Sprite(self.jump)
        jump_anim_left = Sprite(self.jump_left)
        jump_frames = []
        jump_frames_left = []
        jump_slide = 5
        jump_frame = 0

        for x in range(jump_slide):
            jump_frames.append(jump_anim.get_image(x, 120, 80, 3, BLACK))
            jump_frames_left.append(jump_anim_left.get_image(x, 120, 80, 3, BLACK))

    #climb
    def _climb_anim(self):
        climb_anim = Sprite(self.climb_up)
        climb_frames = []
        climb_slide = 7
        climb_frame = 0
        for x in range(climb_slide):
            climb_frames.append(climb_anim.get_image(x, 120, 80, 3, BLACK))

    def _idle(self):
        pass

    def _run(self):
        pass

    def _attack(self):
        pass

    def _jump(self):
        pass

    def _climb(self):
        pass
    


class Enemy(object):
    def __init__(self, x, y):
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

        for x in range(enemy_slide):
            enemy_frames.append(enemy_anim.get_image(x, 150, 150, 3, BLACK))
            enemy_frames_death.append(enemy_anim_death.get_image(x, 150, 150, 3, BLACK))
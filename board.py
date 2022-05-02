"""
Creates the model behind the Samurai Cheems: Bonsai Bananza game
"""

# Python imports
from typing import List
import time

# Library imports
import pygame
# pymunk imports
import pymunk
import pymunk.pygame_util
from pymunk import Vec2d


class Board():
    """
    Create a class to represent the game board
    for Samurai Cheems: Bonsai Bonanza.
    """
    def __init__(self):
        self.pot_lines = []
        self.tree_lines = []
        self.wall_lines = []
        self.pips = []
        self.pot_x_1 = 0
        self.pot_x_2 = 0

        # Space
        self._space = pymunk.Space()
        self._space.gravity = (0.0, 900.0)

        # Physics
        # Time step
        self.dt = 1.0 / 60.0
        # Number of physics steps per screen frame
        self.physics_steps_per_frame = 1

        # pygame
        pygame.init()
        #self._screen = pygame.display.set_mode((600, 600))
        self._clock = pygame.time.Clock()


        # Balls that exist in the world
        self.balls = []

        self.score = 0

    def draw_background(self):
        """
        Creates the walls around the game board
        """
        #Makes the physics body static
        static_body = self._space.static_body
        #Creates the locations of the wall lines
        self.wall_lines = [
            pymunk.Segment(static_body, (0, 0), (0, 600), 0.0),
            pymunk.Segment(static_body, (600, 0), (600, 600), 0.0),
            pymunk.Segment(static_body, (0, 0), (600, 0), 0.0)
        ]
        #Adds physics parameters for the lines
        for line in self.wall_lines:
            line.elasticity = 0.5
            line.friction = 0.9
        #Adds the wall lines to the space.
        self._space.add(*self.wall_lines)

    def draw_level(self,level_num, level_state):
        """
        Creates the pegs, pot, and tree for each level and stage
        """
        #Clears the previous level
        self.empty_level()
        #Sets the physics type for the level objects
        static_body = self._space.static_body

        pip_radius=5

        #Sets object locations for level 1 stage 1
        pips_1_1 = []
        #for row in range(6):
        #    for col in range(10):
        #        pips_1_1.append(pymunk.Circle(static_body,pip_radius,\
        #            (col*70+35*(row % 2),row*70+100)))

        pot_lines_1_1 = [
            pymunk.Segment(static_body, (200, 600 - 10), (400, 600 - 10), 0.0),\
            pymunk.Segment(static_body, (200.0, 600 - 10), (150.0, 600 - 60), 0.0),\
            pymunk.Segment(static_body, (400.0, 600 - 10), (450.0, 600 - 60), 0.0)]
        tree_lines_1_1 = []

        pips_1_2 = []
        for row in range(4):
            for col in range(10):
                pips_1_2.append(pymunk.Circle(static_body,pip_radius,(col*70+\
                    35*(row % 2),row*120+100)))

        #Sets the parameters for each level and stage
        if level_num == 1:
            if level_state == 1:
                self.pips = pips_1_1
                self.tree_lines = tree_lines_1_1
                self.pot_lines = pot_lines_1_1
                self.pot_x_1 = 200
                self.pot_x_2 = 400
            if level_state == 2:
                self.pips = pips_1_2
                self.tree_lines = tree_lines_1_1
                self.pot_lines = pot_lines_1_1
                self.pot_x_1 = 200
                self.pot_x_2 = 400

        #Adds the physics for each object and
        #adds the object to the physics space
        for pip in self.pips:
            pip.elasticity = 0.95
            pip.friction = 0.9
        self._space.add(*self.pips)
        for line in self.tree_lines:
            line.elasticity = 0.5
            line.friction = 0.9
        self._space.add(*self.tree_lines)
        for line in self.pot_lines:
            line.elasticity = 0.5
            line.friction = 0.9
            line.collision_type = 2
        self._space.add(*self.pot_lines)

    def empty_level(self):
        """
        Clears the level of any previous pegs, pot lines, or tree lines
        """
        #Remove pips
        self._space.remove(*self.pips)
        self.pips = []

        #Remove the bonsai sprout
        self._space.remove(*self.tree_lines)
        self.tree_lines = []

        #Remove the pot
        self._space.remove(*self.pot_lines)
        self.pot_lines = []

    def check_if_scored(self):
        """
        Create/remove balls as necessary. Call once per frame only.
        :return: None
        """
        # Remove balls that fall into bonsai pot and increase score
        score_collision = self._space.add_collision_handler(1,2)
        if len(self.balls) > 0:
            ball = self.balls[0]
            score_collision.begin = self.scores
            time.sleep(0.01)
            #ball.collision_type = 3

        # Remove balls that fall out of bounds
        balls_to_remove = [ball for ball in self.balls if ball.body.position.y > 590]
        for ball in balls_to_remove:
            self._space.remove(ball, ball.body)
            self.balls.remove(ball)

    def scores(self,arbiter,space,data):
        self.score += 1
        self._space.remove(self.balls, self.balls.body)
        self.balls.remove(self.balls)
        return True
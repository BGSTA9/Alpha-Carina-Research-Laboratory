from manim import *

class Calibrate(Scene):
    def construct(self):
        # 1. Create the grid
        grid = NumberPlane()
        grid.add_coordinates() # This is the correct method for v0.19.1
        self.add(grid)
        
        # 2. Uncomment below to see your image behind the grid
        # img = ImageMobject("Alpha_Carina.jpg").scale(2)
        # self.add(img)
        
        self.wait(10)
from manim import *

class AlphaCarinaLogo(Scene):
    def construct(self):
        # 1. Create the background "Shroud" shape (AnnularSector)
        # This replicates the curved black block in your image
        shroud = AnnularSector(
            inner_radius=2.5, 
            outer_radius=5.5, 
            angle=70*DEGREES, 
            start_angle=110*DEGREES, 
            color="#000000",
            fill_opacity=1
        ).shift(RIGHT * 2 + DOWN * 2)

        # 2. Define the Coordinates for the constellation
        pts = [
            np.array([3.5, 2.2, 0]),   # Top Right Large Star
            np.array([0.5, 1.3, 0]),   
            np.array([-0.8, 1.1, 0]),    
            np.array([-1.4, 2.5, 0]),  
            np.array([-1.7, -0.3, 0]), 
            np.array([-0.4, -1.8, 0]),   
            np.array([-1.7, -2.6, 0]), 
            np.array([-3.0, -1.3, 0]), # Target Star (dashed ring)
            np.array([-2.8, -0.4, 0]), 
            np.array([-2.5, 0.1, 0]), 
        ]

        # 3. Create the dots and lines
        dots = VGroup(*[Dot(p, radius=0.08, color=WHITE) for p in pts])
        dots[0].scale(3) # Primary star
        
        dashed_circle = DashedVMobject(Circle(radius=0.25, color=WHITE), num_dashes=15)
        dashed_circle.move_to(pts[7])

        lines = VGroup()
        for i in range(len(pts) - 1):
            lines.add(Line(pts[i], pts[i+1], stroke_width=3, color=GRAY_B))

        # 4. The Text
        text_top = Text("ALPHA CARINA", weight=BOLD).scale(0.7)
        text_bottom = Text("RESEARCH\nLABORATORY", line_spacing=0.8).scale(0.5)
        text_group = VGroup(text_top, text_bottom).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        text_group.move_to(RIGHT * 2.5 + DOWN * 1.5)

        # 5. ANIMATION SEQUENCE
        # Draw background first
        self.play(FadeIn(shroud), run_time=1)
        
        # Draw constellation
        self.play(
            Create(lines), 
            Succession(*[GrowFromCenter(d) for d in dots]),
            run_time=3,
            rate_func=smooth # Use 'smooth' to avoid NameErrors
        )
        
        # Reveal UI elements
        self.play(
            Create(dashed_circle),
            Write(text_group),
            run_time=1.5
        )
        self.wait(2)
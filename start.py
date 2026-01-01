from manim import *

class AlphaCarinaResearch(Scene):
    def construct(self):
        # 1. Coordinate Mapping (REVERSED to start at -1.84, 1.48)
        # Sequence: Cluster -> Path -> High Star (5.19, 2.5)
        coords = [
            [-1.84, 1.48, 0],   # START POINT
            [-2.37, -0.38, 0],
            [-1.1, -1.4, 0],
            [-2.5, -1.97, 0],
            [-4.0, -0.9, 0],
            [-4.06, -0.1, 0],
            [-3.64, 0.25, 0],
            [-1.84, 1.48, 0],   # Close cluster loop
            [0.16, 1.64, 0],    # Bridge point
            [5.19, 2.5, 0]      # END POINT (Primary Star)
        ]
        pts = [np.array(p) for p in coords]

        # 2. Design Elements
        # Black "Technical" Shroud
        shroud = AnnularSector(
            inner_radius=3.5, outer_radius=7.5, 
            angle=100*DEGREES, start_angle=100*DEGREES, 
            color=BLACK, fill_opacity=1
        ).shift(RIGHT * 3.5 + DOWN * 3.5)

        # Lines (Drawing starts from the first point in coords)
        lines = VGroup()
        for i in range(len(pts) - 1):
            lines.add(Line(pts[i], pts[i+1], stroke_width=2, color=GRAY_A))

        # Stars
        stars = VGroup(*[Dot(p, radius=0.07, color=WHITE) for p in pts])
        primary_star = stars[-1].scale(4) # End point star
        
        # 3. Research-Heavy Typography
        # Using a monospaced "technical" font feel for the secondary text
        text_main = Text("ALPHA CARINA", weight=BOLD, font="Courier New").scale(0.8)
        text_sub = Text("", 
                        font="Courier New", line_spacing=1.2).scale(0.35)
        text_group = VGroup(text_main, text_sub).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        text_group.move_to(RIGHT * 3.2 + DOWN * 2.2)

        # 4. ANIMATION SEQUENCE
        self.add(shroud)
        
        # Draw lines in sequence (starting from left cluster)
        self.play(Create(lines), run_time=4, rate_func=linear)
        
        # Pop stars as path completes
        self.play(
            LaggedStart(*[GrowFromCenter(s) for s in stars[:-1]], lag_ratio=0.1),
            Write(text_group),
            run_time=1.5
        )

        # 5. THE GLOW EFFECT (At 5.19, 2.5)
        # Create a radial glow using multiple circles
        glow_layer = VGroup(*[
            Dot(pts[-1], radius=r, color=WHITE, fill_opacity=o)
            for r, o in zip([0.15, 0.3, 0.5], [0.8, 0.4, 0.15])
        ])
        
        self.play(
            GrowFromCenter(stars[-1]),
            FadeIn(glow_layer, scale=1.5),
            Flash(pts[-1], color=WHITE, line_length=0.4, num_lines=12, flash_radius=0.6),
            run_time=0.8
        )
        
        # Subtle pulsing of the final point
        self.play(glow_layer.animate.scale(1.2).set_opacity(0.1), rate_func=there_and_back, run_time=2)
        self.wait(2)
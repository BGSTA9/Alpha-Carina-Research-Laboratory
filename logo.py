from manim import *
import numpy as np
import random

class aCarina(ThreeDScene):
    def construct(self):
        # --- 1. CONFIGURATION & DATA ---
        COLOR_CYAN = "#00D4FF"
        COLOR_DARK = "#002233"
        
        coords = [
            [-1.84, 1.48, 0], [-2.37, -0.38, 0], [-1.1, -1.4, 0],
            [-2.5, -1.97, 0], [-4.0, -0.9, 0], [-4.06, -0.1, 0],
            [-3.64, 0.25, 0], [-1.84, 1.48, 0], [0.16, 1.64, 0],
            [5.19, 2.5, 0]
        ]
        pts = [np.array(p) for p in coords]

        # --- 2. SCROLLING DATA STREAM (Background) ---
        # A collection of physics/math formulas to scroll in the back
        formulas = [
            r"\nabla \cdot \vec{E} = \frac{\rho}{\epsilon_0}",
            r"E = mc^2",
            r"\psi(r, t) = A e^{i(kr - \omega t)}",
            r"R_{\mu\nu} - \frac{1}{2}Rg_{\mu\nu} = \frac{8\pi G}{c^4}T_{\mu\nu}",
            r"L = \sqrt{1 - \frac{v^2}{c^2}}",
            r"\hat{H}\Psi = E\Psi",
            r"\oint \vec{B} \cdot d\vec{l} = \mu_0 I"
        ]
        
        data_stream = VGroup(*[
            MathTex(random.choice(formulas), color=BLUE_E, fill_opacity=0.15).scale(0.4)
            for _ in range(15)
        ])
        
        for i, item in enumerate(data_stream):
            item.move_to([random.uniform(-7, 7), random.uniform(-4, 4), -1]) # Placed behind

        def update_stream(m, dt):
            for item in m:
                item.shift(UP * 0.3 * dt)
                if item.get_y() > 4:
                    item.set_y(-4)

        data_stream.add_updater(update_stream)
        self.add(data_stream)

        # --- 3. THE PATH & STARS ---
        path = VMobject(stroke_width=2, color=COLOR_CYAN)
        path.set_points_as_corners(pts)
        
        # --- 4. THE GLITCH TITLE FUNCTION ---
        title = Text("ALPHA CARINA", font="Orbitron", weight=BOLD).scale(0.8)
        subtitle = Text("SYSTEMS & RESEARCH LABORATORY", font="Monospace").scale(0.3)
        branding = VGroup(title, subtitle).arrange(DOWN, aligned_edge=LEFT).move_to(RIGHT*3 + DOWN*2)
        
        def glitch_effect(mob):
            """Animates a quick flickering/glitch reveal"""
            return Succession(
                FadeIn(mob, run_time=0.05, color=RED, scale=1.05),
                FadeOut(mob, run_time=0.05),
                FadeIn(mob, run_time=0.05, color=BLUE, shift=LEFT*0.1),
                FadeOut(mob, run_time=0.05),
                FadeIn(mob, run_time=0.1, color=WHITE)
            )

        # --- 5. ANIMATION SEQUENCE ---
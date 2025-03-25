from manim import *

class RotatingZoomingRectanglesWithCircuit(Scene):
    def construct(self):
        # Title text
        bjt_text = Text("BJT as a Switch", color=WHITE).scale(1).move_to([0, 3, 0])
        self.play(Write(bjt_text, run_time=1))
        self.wait(1)

        # First Rectangle (Blue) - N-emitter
        blue_rect = Polygon([-5, 2, 0], [-2, 2, 0], [-2, -2, 0], [-5, -2, 0], color=BLUE, fill_opacity=0.5)
        n_emitter_text = Text("N-emitter", color=BLUE).scale(0.6).move_to([-3.5, 0, 0])
        self.play(Create(blue_rect, run_time=2), Write(n_emitter_text, run_time=2))

        # Second Rectangle (White) - P-base
        white_rect = Polygon([-2, 2, 0], [0, 2, 0], [0, -2, 0], [-2, -2, 0], color=WHITE, fill_opacity=0.5)
        p_base_text = Text("P-base", color=WHITE).scale(0.6).move_to([-1, 0, 0])
        self.play(Create(white_rect, run_time=2), Write(p_base_text, run_time=2))

        # Third Rectangle (Red) - N-collector
        red_rect = Polygon([0, 2, 0], [4, 2, 0], [4, -2, 0], [0, -2, 0], color=RED, fill_opacity=0.5)
        n_collector_text = Text("N-collector", color=RED).scale(0.6).move_to([2, 0, 0])
        self.play(Create(red_rect, run_time=2), Write(n_collector_text, run_time=2))

        # Fade out text
        self.play(FadeOut(n_emitter_text, p_base_text, n_collector_text, run_time=1))

        # Group all rectangles
        rectangles = VGroup(blue_rect, white_rect, red_rect)
        self.play(rectangles.animate.rotate(PI / 2))
        self.play(rectangles.animate.scale(0.5))

        # Circuit Line
        circuit_line = Line(start=[0, 3.7, 0], end=[0, -3.5, 0], color=PURPLE)
        self.play(Create(circuit_line, run_time=2))
        self.add(circuit_line, rectangles)

        # First circuit path
        circuit_path_1 = VMobject()
        circuit_path_1.set_points_as_corners([[0, 3.7, 0], [6, 3.7, 0], [6, -3, 0], [0, -3, 0]])
        circuit_path_1.set_color(PURPLE)
        self.play(Create(circuit_path_1, run_time=3))

        # Second circuit path
        circuit_path_2 = VMobject()
        circuit_path_2.set_points_as_corners([[0, 0, 0], [-6, 0, 0], [-6, -3, 0], [0, -3, 0]])
        circuit_path_2.set_color(PURPLE)
        self.play(Create(circuit_path_2, run_time=3))

        # **Vbb Line**
        yellow_line_vbb = Line(start=[-6.3, -1.5, 0], end=[-5.7, -1.5, 0], color=YELLOW)
        vbb_text = Text("Vbb", color=YELLOW).scale(0.6).next_to(yellow_line_vbb, UP, buff=0.1)
        self.play(Create(yellow_line_vbb, run_time=1), Write(vbb_text, run_time=1))

        # Additional Vbb line
        yellow_line_3 = Line(start=[-6.2, -1.6, 0], end=[-5.8, -1.6, 0], color=YELLOW)
        self.play(Create(yellow_line_3, run_time=1))

        # **Vcc Line**
        yellow_line_vcc = Line(start=[5.7, 0, 0], end=[6.3, 0, 0], color=YELLOW)
        vcc_text = Text("Vcc", color=YELLOW).scale(0.6).next_to(yellow_line_vcc, UP, buff=0.1)
        self.play(Create(yellow_line_vcc, run_time=1), Write(vcc_text, run_time=1))

        # Additional Vcc line
        yellow_line_4 = Line(start=[5.8, -0.1, 0], end=[6.2, -0.1, 0], color=YELLOW)
        self.play(Create(yellow_line_4, run_time=1))

        # **Right-Pointing Triangle for "Ib"**
        ib_triangle_vertices = [
            [-4, 0.5, 0],  # Leftmost point
            [-4, -0.5, 0],  # Bottom right
            [-3, 0, 0]  # Top right
        ]
        ib_triangle = Polygon(*ib_triangle_vertices, color=YELLOW, fill_opacity=0.3).scale(0.5)
        ib_text = Text("Ib", color=YELLOW).scale(0.6).next_to(ib_triangle, UP, buff=0.1)

        self.play(Create(ib_triangle, run_time=2), Write(ib_text, run_time=1))

        # **Triangle for "Ic"**
        ic_triangle_vertices = [
            [0, 3, 0],  # Bottom middle
            [-0.3, 3.5, 0],  # Top left
            [0.3, 3.5, 0]   # Top right
        ]
        ic_triangle = Polygon(*ic_triangle_vertices, color=YELLOW, fill_opacity=0.3)
        ic_text = Text("Ic", color=YELLOW).scale(0.6).next_to(ic_triangle, DOWN, buff=0.1)

        self.play(Create(ic_triangle, run_time=2), Write(ic_text, run_time=1))

        # **New Triangle for "Ie"**
        ie_triangle_vertices = [
            [0, -3, 0],    # Bottom middle
            [-0.3, -2.5, 0],  # Top left
            [0.3, -2.5, 0]   # Top right
        ]
        ie_triangle = Polygon(*ie_triangle_vertices, color=YELLOW, fill_opacity=0.3)
        ie_text = Text("Ie", color=YELLOW).scale(0.6).next_to(ie_triangle, UP, buff=0.1)

        self.play(Create(ie_triangle, run_time=2), Write(ie_text, run_time=1))

        self.wait(2)

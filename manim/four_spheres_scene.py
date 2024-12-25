from manim import *
import numpy as np
from manim import (ThreeDScene, VGroup, Mobject, FadeOut, Text,
                   FadeIn, UP, RIGHT, BLUE, DEGREES, PI, Surface, ThreeDAxes)

class FourSpheresAnimation(ThreeDScene):
    def orient_label_to_camera(self, mob: Mobject):
        """
        Updater pour orienter `mob` de sorte qu'il fasse face à la caméra.
        """
        # On récupère les angles de la caméra
        phi = self.camera.get_phi()     # rotation autour de l’axe X
        theta = self.camera.get_theta() # rotation autour de l’axe Z (en manim, c’est 'theta')
        
        # Remettre à zéro toutes rotations précédentes
        mob.set_rotation(0)
        # Appliquer rotation inverse de phi autour de l'axe X (RIGHT) pour redresser le texte
        mob.rotate(-phi, axis=RIGHT)
        # Appliquer rotation theta autour de l'axe Z (OUT) ou autour de l'axe Y, 
        # selon la convention de Manim. En 3DScene, c’est souvent autour de l’axe UP.
        mob.rotate(theta, axis=UP)

    def create_3d_sphere(self, radius=1, color=BLUE, opacity=0.8):
        """
        Crée et retourne une sphère 3D (Surface) de rayon `radius`.
        """
        return Surface(
            lambda u, v: np.array([
                radius * np.sin(u) * np.cos(v),
                radius * np.sin(u) * np.sin(v),
                radius * np.cos(u)
            ]),
            u_range=[0, PI],
            v_range=[0, 2*PI],
            resolution=(32, 32),
        ).set_fill(color, opacity=opacity).set_stroke(color, width=0.5)

    def construct(self):
        # --- 1) Configuration de la scène
        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES)
        axes = ThreeDAxes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            z_range=[-5, 5, 1],
        )
        self.add(axes)

        # --- 2) Sphère unique au centre
        big_sphere = self.create_3d_sphere(radius=1.2, color=BLUE, opacity=0.6)
        self.add(big_sphere)
        self.wait(1)

        # --- 3) Préparer les 4 sphères en quadrants
        # positions (x, y, z) symétriques
        positions = [
            [ 2,  2,  0],  # quadrant haut-droit
            [-2,  2,  0],  # quadrant haut-gauche
            [ 2, -2,  0],  # quadrant bas-droit
            [-2, -2,  0],  # quadrant bas-gauche
        ]
        sphere_names = [
            "Customer Portal",
            "Partner Portal",
            "Vendor Portal",
            "Partner Offers"
        ]

        spheres_group = VGroup()
        labels_group = VGroup()
        
        for pos, title in zip(positions, sphere_names):
            sphere = self.create_3d_sphere(radius=0.8, color=BLUE, opacity=0.7)
            sphere.move_to(pos)  # positionner dans l'espace

            # Créer un texte 3D (en fait, c’est un Mobject 2D, mais on le place en 3D)
            label = Text(title, font_size=32)
            # on le place en dessous sur l'axe Y (pour "sous" la sphère)
            label.move_to(np.array([pos[0], pos[1] - 1.2, pos[2]]))

            # Ajouter l’updater pour qu’il fasse face à la caméra
            label.add_updater(self.orient_label_to_camera)

            spheres_group.add(sphere)
            labels_group.add(label)

        # --- 4) Animation : la grosse sphère disparaît, les 4 apparaissent
        self.play(
            FadeOut(big_sphere),
            *[FadeIn(sphere) for sphere in spheres_group],
            run_time=2
        )
        self.wait(0.5)

        # --- 5) Animation : les titres apparaissent
        self.play(*[FadeIn(label) for label in labels_group])
        self.wait(2)

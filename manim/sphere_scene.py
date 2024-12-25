from manim import *
from manim import ThreeDScene


class SphereScene(ThreeDScene):
    def construct(self):
        # Configurer l'orientation initiale de la caméra
        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES)

        # Créer les axes 3D
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-3, 3, 1]
        )

        # Créer la sphère via une surface paramétrique
        # Paramétrisation en coordonnées sphériques :
        # x = R * sin(u) * cos(v)
        # y = R * sin(u) * sin(v)
        # z = R * cos(u)
        sphere = Surface(
            lambda u, v: np.array([
                2 * np.sin(u) * np.cos(v),  # x
                2 * np.sin(u) * np.sin(v),  # y
                2 * np.cos(u)               # z
            ]),
            u_range=[0, PI],
            v_range=[0, 2*PI],
            resolution=(32, 32),
        )

        # Style de la sphère (couleur, transparence, etc.)
        sphere.set_fill(BLUE, opacity=0.5)
        sphere.set_stroke(BLUE_E, width=1)

        # Ajouter les axes et la sphère à la scène
        self.add(axes, sphere)

        # Petite pause pour contempler la scène
        self.wait(2)

manim -pqh sphere_scene.py SphereScene
manim -pqh four_spheres_scene.py FourSpheresScene
manim --disable_caching -pqh four_spheres_scene.py FourSpheresAnimation
manim render four_spheres_scene.py FourSpheresAnimation --renderer opengl



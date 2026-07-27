# /// script
# dependencies = [
#     "marimo",
#     "numpy==2.5.1",
#     "wigglystuff==0.5.21",
# ]
# requires-python = ">=3.13"
# ///

import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def titre(mo):
    mo.md(r"""
    # Cube 3D piloté par matrices (wigglystuff ThreeWidget)

    Manipule le cube avec **deux matrices** :

    - $R$ : matrice $3{\times}3$ (rotation — ou cisaillement/échelle si tu sors des rotations pures)
    - $t$ : vecteur de translation $3{\times}1$

    La transformation appliquée au cube est la matrice homogène
    $M = \begin{pmatrix} R & t \\ 0 & 1 \end{pmatrix}$.

    Astuce : fais glisser les valeurs des matrices horizontalement pour les modifier.
    """)
    return


@app.cell
def imports():
    import marimo as mo
    import numpy as np
    from wigglystuff import ThreeWidget

    return ThreeWidget, mo, np


@app.cell
def widgets(mo, np):
    rot_widget = mo.ui.matrix(
        np.eye(3), step=0.1)

    trans_widget = mo.ui.matrix(
        np.zeros((3, 1)), step=0.5)

    angle_slider = mo.ui.slider(
        -180, 180, value=0, step=5, label="θ (rotation Y en degrés)"
    )
    return angle_slider, rot_widget, trans_widget


@app.cell
def matrice_homogene(angle_slider, np, rot_widget, trans_widget):
    # R éditée à la main, composée avec la rotation Y du slider
    _theta = np.deg2rad(angle_slider.value)
    _c, _s = np.cos(_theta), np.sin(_theta)
    _Ry = np.array([
        [_c, 0.0, _s],
        [0.0, 1.0, 0.0],
        [-_s, 0.0, _c],
    ])

    R = np.asarray(rot_widget.value, dtype=float) @ _Ry
    t = np.asarray(trans_widget.value, dtype=float).ravel()

    M = np.eye(4)
    M[:3, :3] = R
    M[:3, 3] = t
    return (M,)


@app.cell(hide_code=True)
def affichage_matrice(M, mo, np):
    _rows = r" \\ ".join(
        " & ".join(f"{v:.2f}" for v in _row) for _row in np.asarray(M)
    )
    mo.md(
        rf"""
    Matrice homogène appliquée au cube :

    $$M = \begin{{pmatrix}} {_rows} \end{{pmatrix}}$$
    """
    )
    return


@app.cell
def geometrie_cube(np):
    # Cube de côté 2 centré à l'origine : 8 sommets + points échantillonnés
    # le long des 12 arêtes (pour dessiner le cube en nuage de points)
    cube_corners = np.array(
        [[x, y, z] for x in (-1, 1) for y in (-1, 1) for z in (-1, 1)],
        dtype=float,
    )

    _edge_pts = []
    for _i in range(8):
        for _j in range(_i + 1, 8):
            # deux sommets forment une arête s'ils ne diffèrent
            # que d'une coordonnée
            if np.sum(np.abs(cube_corners[_i] - cube_corners[_j])) == 2.0:
                _t = np.linspace(0.0, 1.0, 9)[1:-1, None]
                _edge_pts.append(
                    cube_corners[_i] * (1 - _t) + cube_corners[_j] * _t
                )
    cube_edges = np.vstack(_edge_pts)
    return cube_corners, cube_edges


@app.cell
def scene_three(ThreeWidget, mo):
    three_cube = ThreeWidget(
        data=[],
        width=640,
        height=420,
        xlim=(-4, 4),
        ylim=(-4, 4),
        zlim=(-4, 4),
        camera_azimuth=60,
        camera_elevation=25,
    )
    three_view = mo.ui.anywidget(three_cube)
    three_view
    return (three_cube,)


@app.cell
def maj_scene(M, cube_corners, cube_edges, three_cube):
    def _points(pts, color, size, opacity):
        return [
            {
                "x": float(_p[0]),
                "y": float(_p[1]),
                "z": float(_p[2]),
                "color": color,
                "size": size,
                "opacity": opacity,
            }
            for _p in pts
        ]

    _R, _t = M[:3, :3], M[:3, 3]
    _corners_tfm = cube_corners @ _R.T + _t
    _edges_tfm = cube_edges @ _R.T + _t

    # cube fantôme (référence, gris) + cube transformé (bleu)
    three_cube.data = (
        _points(cube_corners, "#888888", 0.10, 0.25)
        + _points(cube_edges, "#888888", 0.05, 0.25)
        + _points(_corners_tfm, "#4f9dff", 0.14, 1.0)
        + _points(_edges_tfm, "#7fc2ff", 0.07, 0.9)
    )
    return


@app.cell(hide_code=True)
def affichage_widgets(angle_slider, mo, rot_widget, trans_widget):
    mo.vstack(
        [
            mo.hstack(
                [
                    mo.vstack([mo.md("**Rotation $R$**"), rot_widget]),
                    mo.vstack([mo.md("**Translation $t$**"), trans_widget]),
                ],
                justify="start",
                gap=3,
            ),
            mo.md(
                "*Optionnel : le slider ci-dessous génère une rotation Y pure "
                "(il ne modifie pas la matrice éditable, il s'y compose).*"
            ),
            angle_slider,
        ]
    )
    return


if __name__ == "__main__":
    app.run()

# /// script
# dependencies = [
#     "altair==6.2.2",
#     "marimo",
#     "numpy==2.5.1",
#     "pandas==3.0.5",
#     "pillow==12.3.0",
#     "polars==1.43.1",
#     "pyarrow",
#     "wigglystuff==0.5.21",
# ]
# requires-python = ">=3.13"
# ///

import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # wigglystuff

    https://koaning.github.io/wigglystuff/
    """)
    return


@app.cell
def _():
    import wigglystuff 
    import marimo as mo
    import numpy as np
    import pandas as pd
    import altair as alt



    return alt, mo, np, pd


@app.cell(hide_code=True)
def slider2d(mo):
    mo.md(r"""
    ## Slider2D
    """)
    return


@app.cell
def _(mo):
    from wigglystuff import Slider2D

    widget = mo.ui.anywidget(
        Slider2D(
            width=320,
            height=320,
            x_bounds=(-2.0, 2.0),
            y_bounds=(-1.0, 1.5),
        )
    )
    return (widget,)


@app.cell
def _(widget):
    widget
    return


@app.cell
def _(mo, widget):
    mo.callout(
        f"x = {widget.x:.3f}, y = {widget.y:.3f}; bounds {widget.x_bounds} / {widget.y_bounds}"
    )
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Matrice 0 255
    """)
    return


@app.cell
def _(mo):
    slider_min = mo.ui.slider(0, 255, value=1, step=1, label="min")
    slider_max = mo.ui.slider(0, 255, value=1, step=1, label="max")
    mo.hstack([slider_min, slider_max], justify="start")
    return (slider_min,)


@app.cell(hide_code=True)
def _(np, slider_min):
    gradient_vertical = np.linspace(0, slider_min.value, 255)
    gradient_horizontal = np.linspace(0, slider_min.value, 255)

    rgb_mat2 = gradient_vertical[:, None] * gradient_horizontal[None, :]
    rgb_mat2 = rgb_mat2.astype(np.uint8)

    print(rgb_mat2.shape)
    # (2555, 255)
    return (rgb_mat2,)


@app.cell(hide_code=True)
def _(mo, np, rgb_mat2):
    from PIL import Image
    from wigglystuff import HoverZoom

    # Chaque couleur est répétée sur 200 pixels de largeur
    image_array = np.repeat(
        rgb_mat2[:, None, :],
        repeats=200,
        axis=1,
    )

    print(image_array.shape)
    # (1000, 200, 3)

    image = Image.fromarray(rgb_mat2)

    viewer = mo.ui.anywidget(
        HoverZoom(
            image,
            width=200,
            zoom_factor=4,
        )
    )

    viewer
    return


@app.cell(hide_code=True)
def matrix_pca(mo):
    mo.md(r"""
    ## Matrix / PCA

    Principal Component Analysis

    `wigglystuff.Matrix` has graduated to marimo core: this uses `mo.ui.matrix`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Cette ligne projette les 1000 couleurs RGB (3D) vers un espace 2D via un produit matriciel :

    - **`pca_mat.value`** : la valeur actuelle du widget `mo.ui.matrix`, une liste imbriquée de forme 3×2 (ex. `[[0.1, -0.5], [0.8, 0.2], [-0.3, 0.9]]`) que vous modifiez en glissant sur les cellules.
    - **`np.asarray(...)`** : convertit cette liste en tableau NumPy pour permettre l'algèbre linéaire.
    - **`@`** : l'opérateur de produit matriciel. `rgb_mat` est de forme (1000, 3), la matrice de forme (3, 2), donc le résultat `X_tfm` est de forme **(1000, 2)**.

    Concrètement : chaque couleur $(r, g, b)$ devient un point $(x, y)$ où chaque coordonnée est une combinaison linéaire des 3 canaux :

    $$x = r \cdot m_{11} + g \cdot m_{21} + b \cdot m_{31}, \qquad y = r \cdot m_{12} + g \cdot m_{22} + b \cdot m_{32}$$

    C'est exactement ce que fait une PCA (réduction de dimension 3D → 2D), sauf qu'ici c'est **vous** qui choisissez la matrice de projection interactivement — d'où le "PCA demo" : en ajustant les coefficients, vous cherchez la projection qui sépare le mieux les couleurs dans le scatter plot.
    """)
    return


@app.cell
def _(mo, np, pd):
    pca_mat = mo.ui.matrix(np.random.normal(0, 1, size=(3, 2)), step=0.1)
    rgb_mat = np.random.randint(0, 255, size=(1000, 3))
    color = ["#{0:02x}{1:02x}{2:02x}".format(r, g, b) for r, g, b in rgb_mat]

    rgb_df = pd.DataFrame(
        {"r": rgb_mat[:, 0], "g": rgb_mat[:, 1], "b": rgb_mat[:, 2], "color": color}
    )
    return color, pca_mat, rgb_mat


@app.cell
def _(rgb_mat):
    rgb_mat
    return


@app.cell
def _(alt, color, mo, np, pca_mat, pd, rgb_mat):
    X_tfm = rgb_mat @ np.asarray(pca_mat.value)
    df_pca = pd.DataFrame({"x": X_tfm[:, 0], "y": X_tfm[:, 1], "c": color})
    pca_chart = (
        alt.Chart(df_pca)
        .mark_point()
        .encode(x="x", y="y", color=alt.Color("c:N", scale=None))
        .properties(width=400, height=400)
    )

    mo.vstack(
        [
            mo.md("""
    ### PCA demo with `Matrix` 

    Ever want to do your own PCA? Try to figure out a mapping from a 3d color map to a 2d representation with the transformation matrix below."""),
            mo.hstack([pca_mat, pca_chart]),
        ]
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## produit matriciel
    """)
    return


@app.cell
def _(mo, np):
    get_mat1_init, set_mat1_init = mo.state(np.random.normal(0, 1, size=(4, 3)))
    get_mat2_init, set_mat2_init = mo.state(np.random.normal(0, 1, size=(3, 4)))
    reset_one = mo.ui.button(
        label="Reset to 1", on_click=lambda _: set_mat1_init(np.ones((4, 3)))
    )
    reset_zero = mo.ui.button(
        label="Reset to 0", on_click=lambda _: set_mat1_init(np.zeros((4, 3)))
    )
    reset_one2 = mo.ui.button(
        label="Reset to 1", on_click=lambda _: set_mat2_init(np.ones((3, 4)))
    )
    reset_zero2 = mo.ui.button(
        label="Reset to 0", on_click=lambda _: set_mat2_init(np.zeros((3, 4)))
    )
    mo.hstack(
        [
            mo.hstack([reset_one, reset_zero], justify="start"),
            mo.hstack([reset_one2, reset_zero2], justify="end"),
        ],
        justify="space-between",
        widths="equal",
    )
    return get_mat1_init, get_mat2_init


@app.cell(hide_code=True)
def mymat(get_mat1_init, get_mat2_init, mo):
    myMat1 = mo.ui.matrix(get_mat1_init(), step=0.1)
    myMat2 = mo.ui.matrix(get_mat2_init(), step=0.1)
    return myMat1, myMat2


@app.cell
def _(mo, myMat1, myMat2):
    mo.hstack([myMat1, myMat2])
    return


@app.cell
def _(mo, myMat1, myMat2, np):
    resultMat4 = np.asarray(myMat1.value) @ np.asarray(myMat2.value)
    resultMat3 = np.asarray(myMat2.value) @ np.asarray(myMat1.value)
    mo.hstack(
        [mo.plain_text(str(resultMat4)), mo.plain_text(str(resultMat3))],
        justify="space-between",
        widths="equal",
    )
    return


@app.cell
def diagonale(mo, np):
    identityMat = mo.ui.matrix(np.eye(4), step=0.1)
    identityMat
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## ThreeWidget
    """)
    return


@app.cell
def _(mo):
    import random

    from wigglystuff import ThreeWidget

    random.seed(42)
    data = []
    for _ in range(900):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        hex_value = f"#{r:02x}{g:02x}{b:02x}"
        data.append(
            {
                "x": r / 255.0,
                "y": g / 255.0,
                "z": b / 255.0,
                "color": hex_value,
              #  "size": random.uniform(0.08, 0.2),
                "size": 0.1,
                "opacity": random.uniform(0.3, 1.0),
            }
        )

    three = ThreeWidget(
        data=data,
        width=640,
        height=420,
        xlim=(0, 1),
        ylim=(0, 1),
        zlim=(0, 1),
        camera_azimuth=60,
        camera_elevation=25,
        # show_grid=True,
        # show_axes=True,
        # axis_labels=["R", "G", "B"],
    )
    three_widget = mo.ui.anywidget(three)

    def reset(_):
        three.data = data

    def shuffle(_):
        three.data = [
            {
                **d,
                "x": min(1.0, max(0.0, d["x"] + random.uniform(-0.15, 0.15))),
                "y": min(1.0, max(0.0, d["y"] + random.uniform(-0.15, 0.15))),
                "z": min(1.0, max(0.0, d["z"] + random.uniform(-0.15, 0.15))),
            }
            for d in three.data
        ]

    return random, reset, shuffle, three_widget


@app.cell
def _(mo, reset, shuffle, three_widget):
    btn_reset = mo.ui.button(on_click=reset, label="reset")
    btn_shuffle = mo.ui.button(on_click=shuffle, label="make some noise")
    mo.vstack(
        [mo.hstack([btn_reset, btn_shuffle], justify="start"), three_widget]
    )
    return


@app.cell
def _(three_widget):
    three_widget.start_rotate(speed=1.0)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## GraphWidget
    """)
    return


@app.cell
def _():
    from pathlib import Path
    import sys

    repo_root = Path(__file__).resolve().parents[1]
    if (repo_root / "wigglystuff").exists():
        sys.path.insert(0, str(repo_root))

    from wigglystuff import GraphWidget, PlaySlider

    return GraphWidget, PlaySlider


@app.cell
def _(GraphWidget, mo):
    graph = GraphWidget(
        nodes=[
            "Alpha",
            7,
            {"name": "Beta", "size": 20, "color": "#0f766e"},
            {"id": "gamma", "name": "Gamma", "color": "#7c3aed", "size": 17},
            {"name": "Delta", "data": {"kind": "generated"}},
        ],
        edges=[
            ("Alpha", "Beta"),
            {"source": "Beta", "target": "gamma", "name": "depends on", "width": 3},
            {"source": "gamma", "target": "7", "name": "scores"},
            ("Delta", "Alpha"),
        ],
        height=420,
        directed=False,
    )
    MyWidgetGraph = mo.ui.anywidget(graph)

    def add_node_bak(_):
        n = len(graph.nodes) + 1
        node_id = graph.add_node(f"Node {n}", id=f"py{n}", color="#ea580c")
        graph.add_edge(node_id, "Alpha")

    def add_node(_):
        index = len(MyWidgetGraph.nodes) + 1
        new_id = MyWidgetGraph.add_node(
            f"Node {index}",
            color="#b45309" if index % 2 else "#2563eb",
            size=12 + index,
        )
        MyWidgetGraph.add_edge("Alpha", new_id, name="added")

    return MyWidgetGraph, add_node


@app.cell
def _(MyWidgetGraph):
    MyWidgetGraph
    return


@app.cell
def _(add_node, mo):
    mo.ui.button(label="Add node from Python", on_click=add_node)
    return


@app.cell
def _(MyWidgetGraph, mo):
    mo.vstack(
        [
            mo.md(f"**Hovered node:** `{MyWidgetGraph.hovered_node}`"),
            mo.md(f"**Selected nodes:** `{MyWidgetGraph.selected_nodes}`"),
        ]
    )
    return


@app.cell
def _(MyWidgetGraph):
    MyWidgetGraph.get_selected_node_data()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Random growth graph
    """)
    return


@app.cell
def _(mo):
    num_nodes = mo.ui.slider(start=10, stop=100, step=5, value=40, label="Number of nodes")
    regenerate_button = mo.ui.button(label="Regenerate Graph")
    mo.hstack([num_nodes, regenerate_button])
    return num_nodes, regenerate_button


@app.cell
def _(num_nodes, random, regenerate_button):
    # Trigger generation on button click or slider changes
    _trigger = regenerate_button.value

    # Generate the growth steps
    steps = []

    # Step 0: start with 1 node
    _nodes = [{"id": "0", "name": "Node 0"}]
    _edges = []
    steps.append({
        "nodes": list(_nodes),
        "edges": list(_edges),
        "new_node": "0",
        "connected_to": None
    })

    for i in range(1, num_nodes.value):
        _new_node_id = str(i)
        # Select a random existing node to connect to
        _existing_node = random.choice(_nodes)
        _existing_id = _existing_node["id"]

        # Add new node
        _new_node = {
            "id": _new_node_id,
            "name": f"Node {i}"
        }
        _nodes.append(_new_node)

        # Add new edge
        _new_edge = {
            "source": _existing_id,
            "target": _new_node_id
        }
        _edges.append(_new_edge)

        steps.append({
            "nodes": list(_nodes),
            "edges": list(_edges),
            "new_node": _new_node_id,
            "connected_to": _existing_id
        })

    max_step = len(steps) - 1
    return max_step, steps


@app.cell
def _(PlaySlider, max_step, mo):
    play = mo.ui.anywidget(
        PlaySlider(
            min_value=0,
            max_value=max_step,
            step=1,
            interval_ms=300,
            loop=False,
        )
    )
    play
    return (play,)


@app.cell
def _(max_step, play, steps):
    step_index = int(play.value.get("value", 0))
    step_index = max(0, min(step_index, max_step))
    step = steps[step_index]
    return step, step_index


@app.cell
def _(GraphWidget, mo):
    growth_graph = mo.ui.anywidget(
        GraphWidget(
            nodes=[],
            edges=[],
            directed=False,
            bounded=False,
            width=720,
            height=460,
        )
    )
    growth_graph
    return (growth_graph,)


@app.cell
def _(growth_graph, step):
    _new_node_id = step["new_node"]
    _connected_to_id = step["connected_to"]

    _nodes = []
    for _node in step["nodes"]:
        _node_copy = dict(_node)
        if _node_copy["id"] == _new_node_id:
            _node_copy["color"] = "#10b981"  # Emerald/green for the newly added node
            _node_copy["size"] = 16
        elif _node_copy["id"] == _connected_to_id:
            _node_copy["color"] = "#ef4444"  # Red for the node it connected to
            _node_copy["size"] = 14
        else:
            _node_copy["color"] = "#3b82f6"  # Blue for normal nodes
            _node_copy["size"] = 11
        _nodes.append(_node_copy)

    _edges = []
    for _edge in step["edges"]:
        _edge_copy = dict(_edge)
        if (_edge_copy["source"] == _connected_to_id and _edge_copy["target"] == _new_node_id) or \
           (_edge_copy["source"] == _new_node_id and _edge_copy["target"] == _connected_to_id):
            _edge_copy["color"] = "#f59e0b"  # Amber for the new edge
            _edge_copy["width"] = 3
        else:
            _edge_copy["color"] = "#cbd5e1"  # Slate-300 for existing edges
            _edge_copy["width"] = 1.5
        _edges.append(_edge_copy)

    with growth_graph.hold_sync():
        growth_graph.nodes = _nodes
        growth_graph.edges = _edges
    return


@app.cell
def _(growth_graph, max_step, mo, step_index):
    mo.vstack(
        [
            mo.md(f"**Step:** `{step_index}` / `{max_step}`"),
            mo.md(f"**Hovered node:** `{growth_graph.hovered_node}`"),
            mo.md(f"**Selected nodes:** `{growth_graph.selected_nodes}`"),
            mo.md(f"**Selected edges:** `{growth_graph.selected_edges}`"),
        ]
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Scatterwidget
    """)
    return


@app.cell
def _(mo):
    from wigglystuff import ScatterWidget

    widget = mo.ui.anywidget(ScatterWidget(n_classes=3))
    widget
    return (widget,)


@app.cell
def _(widget):
    widget.data_as_polars
    return


@app.cell
def _(widget):
    widget.data_as_pandas
    return


if __name__ == "__main__":
    app.run()

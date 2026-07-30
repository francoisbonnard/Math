# /// script
# dependencies = [
#     "marimo",
#     "matplotlib==3.11.1",
#     "numpy==2.5.1",
#     "wigglystuff==0.5.23",
# ]
# requires-python = ">=3.13"
# ///

import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Source
    https://molab.marimo.io/github/koaning/wigglystuff/blob/main/demos/heatmap_select.py/wasm?utm_source=wigglystuff
    """)
    return


@app.cell
def _():
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

    import marimo as mo
    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.colors import Normalize, PowerNorm
    from wigglystuff import HeatmapSelect, Hint

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    https://worrydream.com/LadderOfAbstraction/

    One pixel is one cell, and the two strips along the left and bottom edges of the grid are interactive gutters.

    - Hover the grid to preview a single cell. Hover the left gutter for a whole row, or the bottom gutter for a whole column.
    - Click to pin. The three pins are independent and coexist — pin a cell, then a row, then a column, and all three stay. Clicking a region only replaces that region's pin; hovering never disturbs any of them.
    - Double-click a region to drop just that pin.

    Each axis has its own colour, in the widget's bands and in the charts beside them: blue for the y axis (a row) and orange for the x axis (a column). Hovering draws faint and transparent; pinning makes it solid. Making sense of a combination of pins is the caller's job, not the widget's.

    Below are two parameter spaces that want completely different things from you. The first is smooth enough that you can read conclusions straight off it. The second is chaotic, and poking at it is the only thing you can do.
    """)
    return


@app.cell
def _():
    # Shared by both examples, and by both sets of charts, so that "blue means the
    # y axis" is true everywhere on this page. ROW comes off the y axis, COL off
    # the x axis.
    ROW_COLOR = "#1f4fd8"
    COL_COLOR = "#e07b00"
    CELL_COLOR = "#111111"
    return


if __name__ == "__main__":
    app.run()

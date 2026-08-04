# /// script
# dependencies = [
#     "marimo",
#     "numpy==2.5.1",
#     "torch==2.13.0",
# ]
# requires-python = ">=3.13"
# ///

import marimo

__generated_with = "0.23.16"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import numpy as np

    return (np,)


@app.cell
def _():
    import torch

    return (torch,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    https://www.udemy.com/course/machine-learning-data-science-foundations-masterclass/learn/lecture/22930654#overview
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Norms, particularly L1 and L2, used to regularize objective functions
    """)
    return


@app.cell
def _(np):
    x = np.array([25, 2, 5])
    x
    return (x,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $$ L^1 Norm $$
    $$
    \|x\|_1 = {\sum_{i} |x_i|}
    $$
    """)
    return


@app.cell
def l1_norm(np):
    int(np.abs(25)+np.abs(2)+np.abs(5))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $$ L^2 Norm $$
    $$
    \|x\|_2 = \sqrt{\sum_{i} x_i^2}
    $$
    """)
    return


@app.cell
def _(np, x):
    np.linalg.norm(x)
    return


@app.cell
def _():
    (25**2+2**2+5**2)**(1/2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $$ Square \space L^2 Norm $$

    $$
    \|x\|_2^2 = {\sum_{i} x_i^2}
    $$
    Computationally cheaper to user because
    $$ Squared \space L^2 norm = x^Tx $$

    Et tout un délire que je n'ai pas compris ;

        • Computationally cheaper to use than (L^2) norm because:
         • Squared (L^2) norm equals simply (x^T x)
         • Derivative (used to train many ML algorithms) of element (x) requires that element alone, whereas (L^2) norm requires (x) vector

        • Downside is it grows slowly near origin so can’t be used if distinguishing between zero and near-zero is important
    """)
    return


@app.cell
def _():
    (25**2+2**2+5**2)
    return


@app.cell
def _(np, x):
    int(np.dot(x,x))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Max Norm
    $$ L^∞ Norm $$

    $$ \|x\|_∞ = max | x_i |$$
    """)
    return


@app.cell
def _(np):
    int(np.max([np.abs(25),np.abs(2),np.abs(5)]))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $$ Generalized \space L^P Norm $$
    $$
    \|x\|_p = \left(\sum_{i} |x_i|^p\right)^{1/p}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Basis Vectors
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Orthogonal Vectors
    $$ x^Ty=0 $$

    n-dimensional space has max n mutually orthogonal vectors
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Orthonormal Vectors

    Orthogonal & all have unit norm
    """)
    return


@app.cell
def _(np):
    i =np.array([1,0])
    j =np.array([0,1])
    i,j
    return i, j


@app.cell
def _(i, j, np):
    int(np.dot(i,j))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Rappel sur les matrices dans Marimo
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    $M = \begin{pmatrix} R & t \\ 0 & 1 \end{pmatrix}$.
    """)
    return


@app.cell
def _(mo):
    n = mo.ui.slider(start=1, stop=12, step=1, value=5, label="Taille n")
    n
    return (n,)


@app.cell
def _(n, np):
    M = np.eye(n.value)
    return (M,)


@app.cell
def _(M, np):
    np.asarray(M)
    return


@app.cell(hide_code=True)
def _(M, mo, np):

    _rows = r" \\ ".join(" & ".join(f"{v:.2f}" for v in _row) for _row in np.asarray(M)
    )

    _rows
    mo.md(
        rf"""
    $$M = \begin{{pmatrix}} {_rows} \end{{pmatrix}}$$
    """
    )
    return


@app.cell
def _(M, mo):
    rot_widget = mo.ui.matrix(
        M, step=0.1)
    rot_widget
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Matrix Tensors
    https://www.udemy.com/course/machine-learning-data-science-foundations-masterclass/learn/lecture/22930660#overview
    """)
    return


@app.cell
def _(np):
    x10=np.array([[25,2],[5,26],[3,7],[4,1]])
    x10
    return (x10,)


@app.cell
def _(x10):
    x10.shape
    return


@app.cell
def _(x10):
    x10.size
    return


@app.cell
def _(x10):
    x10[1,:]
    return


@app.cell
def _(x10):
    x10[:,0]
    return


@app.cell
def _(x10):
    x10[1:3,0:2]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Matrices in PyTorch
    """)
    return


@app.cell
def _(torch):
    X_pt = torch.tensor([[25,2],[5,26],[3,7],[4,1]])
    X_pt
    return (X_pt,)


@app.cell
def _(X_pt):
    X_pt.shape
    return


if __name__ == "__main__":
    app.run()

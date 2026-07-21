import marimo

__generated_with = "0.23.14"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import sympy as sp
    import numpy as np
    import matplotlib.pyplot as plt

    plt.style.use("dark_background")

    x = sp.symbols("x", positive=True)
    log_x = sp.log(x)
    log2_x = sp.log(x, 2)
    exp_x = sp.exp(x)
    log10_x = sp.log(x, 10)

    print("log(x)  =", log_x)
    print("log2(x) =", log2_x)
    print("exp(x)  =", exp_x)
    print("log10(x) =", log10_x)

    x_vals = np.linspace(0.1, 10, 400)
    f_log = sp.lambdify(x, log_x, "numpy")
    f_log2 = sp.lambdify(x, log2_x, "numpy")
    f_exp = sp.lambdify(x, exp_x, "numpy")

    fig, ax = plt.subplots()
    ax.plot(x_vals, f_log(x_vals), label="log(x)", color="#4FC3F7")
    ax.plot(x_vals, f_log2(x_vals), label="log2(x)", color="#FF8A65")
    ax.plot(x_vals, f_exp(x_vals), label="exp(x)", color="#CE93D8")
    ax.set_title("log(x), log2(x) et exp(x)")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_ylim(-3, 10)
    ax.grid(True, alpha=0.3)
    ax.legend()
    plt.show()

    x_vals_10 = np.linspace(1, 2000, 600)
    f_log10 = sp.lambdify(x, log10_x, "numpy")

    fig2, ax2 = plt.subplots()
    ax2.plot(x_vals_10, f_log10(x_vals_10), label="log10(x)", color="#81C784")
    ax2.scatter([1000], [3], color="#FFE082", zorder=3)
    ax2.annotate("log10(1000) = 3", (1000, 3), xytext=(1120, 2.7), color="#ECEFF1")
    ax2.set_title("Verification: log10(1000) = 3")
    ax2.set_xlabel("x")
    ax2.set_ylabel("log10(x)")
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $$\log_2(8) = 3 \text{ car } 2^3 = 8.$$
    $$log(1000) = 3$$
    $$log(e²) = 2$$
    """)
    return


if __name__ == "__main__":
    app.run()

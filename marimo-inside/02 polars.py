# /// script
# dependencies = [
#     "marimo",
#     "polars==1.43.1",
# ]
# requires-python = ">=3.13"
# ///

import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.cell
def _():
    return


@app.cell
def _():
    import polars as pl

    return (pl,)


@app.cell
def _(pl):
    pl.read_csv("https://calmcode.io/static/data/english_2grams.csv")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()

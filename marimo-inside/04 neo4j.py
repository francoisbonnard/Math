# /// script
# dependencies = [
#     "marimo",
#     "neo4j==6.2.0",
#     "wigglystuff==0.5.23",
# ]
# requires-python = ">=3.13"
# ///

import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo


    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    docker compose up -d

        http://localhost:7474

    - URI : bolt://localhost:7687
    - User : neo4j
    - Password : marimo12345
    - Database : neo4j
    """)
    return


@app.cell 
def _(mo):
    uri_input = mo.ui.text(value="bolt://localhost:7687", label="URI")
    user_input = mo.ui.text(value="neo4j", label="User")
    pass_input = mo.ui.text(value="marimo12345", label="Password", kind="password")
    db_input = mo.ui.text(value="neo4j", label="Database")
    mo.hstack([uri_input, user_input, pass_input, db_input])
    return db_input, pass_input, uri_input, user_input


@app.cell
def _(db_input, mo, pass_input, uri_input, user_input):
    from wigglystuff import Neo4jWidget

    widget = mo.ui.anywidget(
        Neo4jWidget(
            uri=uri_input.value,
            auth=(user_input.value, pass_input.value),
            database=db_input.value,
            height=400
        )
    )
    widget
    return


if __name__ == "__main__":
    app.run()

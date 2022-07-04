import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from ipywidgets import widgets
from plotly.subplots import make_subplots

from experiments.notebooks.visualizations.plotly_theme import (
    cadlabs_colors,
    cadlabs_colorway_sequence,
)
from model.system_parameters import parameters


# Set plotly as the default plotting backend for pandas. Banteg thinks this is a better default than matplotlib.
pd.options.plotting.backend = "plotly"

# 3D Surface


def plot_surface(df):
    grouped = df.groupby(["avg_price", "clients"]).last()["hosts"]

    x = df.groupby(["run"]).first()["avg_price"].unique()
    y = df.groupby(["run"]).first()["clients"].unique()
    z = []

    for avg_price in y:
        row = []
        for clients in x:
            z_value = grouped[avg_price][clients]
            row.append(z_value)
        z.append(row)

    fig = go.Figure(
        data=[
            go.Surface(
                x=x,
                y=y,
                z=z,
                colorbar=dict(
                    title="3D Plot",
                    titleside="right",
                    titlefont=dict(size=14),
                ),
                colorscale=cadlabs_colors,
            )
        ]
    )

    fig.update_traces(contours_z=dict(show=True, usecolormap=True, project_z=True))

    # update_legend_names(fig)

    fig.update_layout(
        title="3D Plot",
        autosize=False,
        legend_title="",
        margin=dict(l=65, r=50, b=65, t=90),
        scene={
            "xaxis": {
                "title": {"text": "AVG Price (ZAR/Mbps/Day)"},
                "type": "log",
            },
            "yaxis": {"title": {"text": "Clients"}},
            "zaxis": {"title": {"text": "Hosts"}},
        },
    )

    return fig

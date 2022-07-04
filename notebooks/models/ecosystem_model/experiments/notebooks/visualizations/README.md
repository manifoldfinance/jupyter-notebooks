

```python3
    def plot_validator_environment_yield_surface(df):
        grouped = df.groupby(["eth_price", "eth_staked"]).last()["total_profit_yields_pct"]

        x = df.groupby(["run"]).first()["eth_price"].unique()
        y = df.groupby(["run"]).first()["eth_staked"].unique()
        z = []

        for eth_staked in y:
            row = []
            for eth_price in x:
                z_value = grouped[eth_price][eth_staked]
                row.append(z_value)
            z.append(row)

        fig = go.Figure(
            data=[
                go.Surface(
                    x=x,
                    y=y,
                    z=z,
                    colorbar=dict(
                        title="Profit Yields (%/year)",
                        titleside="right",
                        titlefont=dict(size=14),
                    ),
                    colorscale=cadlabs_colors,
                )
            ]
        )

        fig.update_traces(contours_z=dict(show=True, usecolormap=True, project_z=True))

        update_legend_names(fig)

        fig.update_layout(
            title="Profit Yields Over ETH Price vs. ETH Staked",
            autosize=False,
            legend_title="",
            margin=dict(l=65, r=50, b=65, t=90),
            scene={
                "xaxis": {
                    "title": {"text": "ETH Price (USD/ETH)"},
                    "type": "log",
                },
                "yaxis": {"title": {"text": "ETH Staked (ETH)"}},
                "zaxis": {"title": {"text": "Profit Yields (%/year)"}},
            },
        )

        return fig
```
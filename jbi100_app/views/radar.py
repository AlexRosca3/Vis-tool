import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from dash import dcc, html


class Radar(html.Div):
    def __init__(self, name, feature_a, feature_b, feature_c, feature_d, feature_e, df):
        self.html_id = name.lower().replace(" ", "-")
        self.df = df
        self.feature_a = feature_a
        self.feature_b = feature_b
        self.feature_c = feature_c
        self.feature_d = feature_d
        self.feature_e = feature_e

        super().__init__(
            className="graph_card",
            children=[
                html.H6(name),
                dcc.Graph(id=self.html_id, figure = self.update())
            ],
        )

    def update(self):
        self.fig = go.Figure()

        values = ['processing cost','mechanical properties','chemical stability',
            'thermal stability', 'device integration']
        r=[1, 5, 2, 2, 3]

        self.fig.add_trace(go.Scatterpolar(r=[1, 5, 2, 2, 3], theta = values, fill='toself'))
        self.fig.update_layout(

        )
        return self.fig


from jbi100_app.main import app
from jbi100_app.views.menu import make_menu_layout
import plotly.graph_objects as go
import pandas as pd
import numpy as np
np.random.seed(1)

from jbi100_app.views.barplot import Barplot
from jbi100_app.views.radar import Radar
from jbi100_app.views.histogram import Histogram
from jbi100_app.views.scatterplot import Scatterplot


from dash import dcc, html
from dash.dependencies import Input, Output 

from pandas import read_csv

data_clean = pd.read_csv('datasets/airbnb_nyc_clean.csv', low_memory = False)
data_og = pd.read_csv('datasets/airbnb_open_data.csv', low_memory = False)

if __name__ == '__main__':
    # Create data

    hist_name_og = "Old Average Review Ratings by Listing Type"
    hist_name_clean = "Average Review Ratings by Listing Type"
    #histogam = Histogram(hist_name, 'review_rate_number', 'Private room', 'room_type', data)
    histogram_og = Histogram(hist_name_og, 'room type', 'review rate number', "Private room", data_og)
    histogram_clean = Histogram(hist_name_clean, 'room_type', 'review_rate_number', "Private room", data_clean)
    
    barplot = Barplot('Listing Type by Average Price', 'neighbourhood_group', 'price', data_clean)    
    barplot2 = Barplot('Average Review Rating by Listing Type', 'neighbourhood_group', 'review_rate_number', data_clean)

    scatterplot = Scatterplot('Listings by Price', 'price', 'id', data_clean)
    
    app.layout = html.Div(
        id="app-container",
        children=[
            # Left column
            html.Div(
                id="left-column",
                className="three columns",
                children=make_menu_layout()
            ),

            # Right columns
            html.Div(
                id="right-column",
                className="nine columns",
                children=[                 
                    histogram_og,
                    histogram_clean,
                    barplot,
                    barplot2,
                    scatterplot
                ],
            ),
        ],
    )
    
    #Define interactions
    
    
    def update_barplot_color(selected_color):
        barplot.color = selected_color
        barplot2.color = selected_color

    @app.callback(
        Output(barplot.html_id, "figure"),
        [Input("select-listing-type", "value"), Input("select-color-barplot", "value")])
    def update_barplot(selected_listing_type, selected_color):
        barplot.update(selected_listing_type, selected_color)
        return barplot.fig
    
    @app.callback(
        Output(barplot2.html_id, "figure"),
        [Input("select-listing-type", "value"), Input("select-color-barplot", "value")])
    def update_barplot2(selected_listing_type, selected_color):
        barplot2.update(selected_listing_type, selected_color)
        return barplot2.fig
    
    @app.callback(
        Output(scatterplot.html_id, "figure"),
        [Input("select-neighbourhood", "value"), Input("select-listing-type", "value")])
    def update_scatterplot(selected_neighbourhood, selected_listing_type):
        scatterplot.update(selected_neighbourhood, selected_listing_type)
        return scatterplot.fig


   
    
    
app.run_server(debug=False, dev_tools_ui=False)

    

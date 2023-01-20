from dash import dcc, html
from ..config import color_list_barplot, listing_type_options

def generate_title_card():
    """

    :return: A Div containing dashboard title & descriptions.
    """
    return html.Div(
        id="title-card",
        children=[
            html.H5("Visualization Tool"),
            html.Div(
                id="title_vis",
                children="Use the different plots to visualize data",
            ),
        ],
    )

def generate_description_card():
    """

    :return: A Div containing dashboard title & descriptions.
    """
    return html.Div(
        id="description-card",
        children=[
            html.H5("Dashboard"),
            html.Div(
                id="intro",
                children="Change the settings of the plots.",
            ),
        ],
    )


def generate_control_card():
    """

    :return: A Div containing controls for graphs.
    """
    return html.Div(
        id="control-card",
        children=[
            html.Label("Color barplot"),
            dcc.Dropdown(
                id="select-color-barplot",
                options=[{"label": i, "value": i} for i in color_list_barplot],
                value=color_list_barplot[0],
            ),
            html.Label("Listing type"),
            dcc.Dropdown(
                id="select-listing-type",
                options=[{"label": i, "value": i} for i in listing_type_options],
                value=listing_type_options[0],
            ),
        ], style={"position": "fixed", "top": "200px", "z-index": 1, "left": "35px", "width": "300px"}

    )




def make_menu_layout():
    return [generate_title_card(), generate_description_card(), generate_control_card()]



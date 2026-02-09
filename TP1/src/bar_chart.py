'''
    Contains some functions related to the creation of the bar chart.
    The bar chart displays the data either as counts or as percentages.
'''

import plotly.graph_objects as go
import plotly.io as pio

from hover_template import get_hover_template
from modes import MODE_TO_DATA, MODES, MODE_TO_COLUMN


def init_figure():
    '''
        Initializes the Graph Object figure used to display the bar chart.
        Sets the template to be used to "simple_white" as a base with
        our custom template on top. Sets the title to 'Lines per act'

        Returns:
            fig: The figure which will display the bar chart
    '''
    fig = go.Figure()

    # TODO : Update the template to include our new theme and set the title
    fig.update_layout(
        title="Lines per act",
        template = pio.templates["simple_white+custom_theme"],
        dragmode=False,
        barmode='relative'
    )

    return fig


def draw(fig, data, mode):
    '''
        Draws the bar chart.

        Arg:
            fig: The figure comprising the bar chart
            data: The data to be displayed
            mode: Whether to display the count or percent data.
        Returns:
            fig: The figure comprising the drawn bar chart
    '''

    # TODO : Update the figure's data according to the selected mode
    fig = go.Figure(fig)
    fig.data = []

    for player in data['Player'].unique():
        player_data = data[data['Player']==player]
        fig.add_bar(
            x=[f"Act {a}" for a in player_data['Act']],
            y=player_data[MODE_TO_DATA[mode]],
            name=player,
            hovertemplate=get_hover_template(player, mode)
        ) 
    return update_y_axis(fig,mode)


def update_y_axis(fig, mode):
    '''
        Updates the y axis to say 'Lines (%)' or 'Lines (Count) depending on
        the current display.

        Args:
            mode: Current display mode
        Returns: 
            The updated figure
    '''
    # TODO : Update the y axis title according to the current mode
    if mode == 'Count':
        fig.update_layout(
            yaxis_title= 'Lines (Count)'
        )
    else:
        fig.update_layout(
            yaxis_title= 'Lines (%)'
        )
    return fig
'''
    Contains some functions related to the creation of the bar chart.
    The bar chart displays the data either as counts or as percentages.
'''

import plotly.graph_objects as go
import plotly.io as pio

from hover_template import get_hover_template
from modes import MODE_TO_DATA, MODES, MODE_TO_COLUMN
from template import THEME


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
    custom_template = go.layout.Template(
        layout=go.Layout(
            colorway=THEME['bar_colors'],
            plot_bgcolor=THEME['background_color'],
            paper_bgcolor=THEME['background_color'],
            font=dict(
                family=THEME['font_family'],
                color=THEME['font_color']
            ),
            xaxis=dict
                (title_font=dict(
                           size=THEME["label_font_size"],)
            ),
            yaxis=dict(
                title_font=dict(
                           size=THEME["label_font_size"],)
            )
        )
    )
    fig.update_layout(
        title="Lines per act",
        template=custom_template,
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
    fig = go.Figure(fig)  # conversion back to Graph Object
    # TODO : Update the figure's data according to the selected mode
    for player in data['Player'].unique():
        player_data = data[data['Player']==player]
        fig.add_bar(
            x=[f"Act {a}" for a in player_data['Act']],
            y=player_data[MODE_TO_DATA[MODES[mode]]],
            name=player
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
    fig.update_layout(
        yaxis_title=MODE_TO_COLUMN[MODES[mode]]
    )
    return fig
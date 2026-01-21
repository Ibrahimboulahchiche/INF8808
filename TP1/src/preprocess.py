'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd
from modes import MODE_TO_COLUMN

def summarize_lines(my_df):
    '''
        Sums each player's total of number of lines and  its
        corresponding percentage per act.

        The sum of lines per player per act is in a new
        column named 'PlayerLine'.

        The percentage of lines per player per act is
        in a new column named 'PlayerPercent'

        Args:
            my_df: The pandas dataframe containing the data from the .csv file
        Returns:
            The modified pandas dataframe containing the
            information described above.
    '''
    # TODO : Modify the dataframe, removing the line content and replacing
    # it by line count and percent per player per act
    my_df = my_df.groupby(['Act', 'Player']).size().reset_index(name='PlayerLine')
    totals = my_df.groupby('Act')['PlayerLine'].sum().reset_index(name='ActTotal')
    my_df = pd.merge(my_df, totals, on='Act')
    my_df['PlayerPercent'] = (my_df['PlayerLine'] / my_df['ActTotal']) * 100
    my_df['PlayerPercent'] = my_df['PlayerPercent'].round(6)
    return my_df


def replace_others(my_df):
    '''
        For each act, keeps the 5 players with the most lines
        throughout the play and groups the other plyaers
        together in a new line where :

        - The 'Act' column contains the act
        - The 'Player' column contains the value 'OTHER'
        - The 'LineCount' column contains the sum
            of the counts of lines in that act of
            all players who are not in the top
            5 players who have the most lines in
            the play
        - The 'PercentCount' column contains the sum
            of the percentages of lines in that
            act of all the players who are not in the
            top 5 players who have the most lines in
            the play

        Returns:
            The df with all players not in the top
            5 for the play grouped as 'OTHER'
    '''
    # TODO : Replace players in each act not in the top 5 by a
    # new player 'OTHER' which sums their line count and percentage
    total_per_players = my_df.groupby('Player')['PlayerLine'].sum()
    top_5_series = total_per_players.sort_values(ascending=False).head(5)
    top_5_names= top_5_series.index.tolist()
    my_df['Player'] = my_df['Player'].apply(lambda x: x if x in top_5_names else 'OTHER')
    my_df = my_df.groupby(['Act', 'Player']).agg(
    PlayerLine=('PlayerLine', 'sum'),
    PlayerPercent=('PlayerPercent', 'sum')).reset_index()
    return my_df


def clean_names(my_df):
    '''
        In the dataframe, formats the players'
        names so each word start with a capital letter.

        Returns:
            The df with formatted names
    '''
    # TODO : Clean the player names
    my_df['Player'] = my_df['Player'].str.title()
    return my_df

df = pd.read_csv('src/assets/data/romeo_and_juliet.csv')
df = clean_names(df)
df = summarize_lines(df)
df = replace_others(df)
print(df.head(100))
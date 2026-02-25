'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd


def convert_dates(dataframe):
    '''
        Converts the dates in the dataframe to datetime objects.

        Args:
            dataframe: The dataframe to process
        Returns:
            The processed dataframe with datetime-formatted dates.
    '''
    # TODO : Convert dates
    data = dataframe.copy()
    
    if 'Date_Plantation' in data.columns:
        data['Date_Plantation'] = pd.to_datetime(
            data['Date_Plantation'], 
            format='%Y-%m-%d', 
            errors='coerce'
        )
            
    return data


def filter_years(dataframe, start, end):
    '''
        Filters the elements of the dataframe by date, making sure
        they fall in the desired range.

        Args:
            dataframe: The dataframe to process
            start: The starting year (inclusive)
            end: The ending year (inclusive)
        Returns:
            The dataframe filtered by date.
    '''
    # TODO : Filter by dates
    return dataframe[dataframe['Date_Plantation'].dt.year.between(start, end)]



def summarize_yearly_counts(dataframe):
    '''
        Groups the data by neighborhood and year,
        summing the number of trees planted in each neighborhood
        each year.

        Args:
            dataframe: The dataframe to process
        Returns:
            The processed dataframe with column 'Counts'
            containing the counts of planted
            trees for each neighborhood each year.
    '''
    # TODO : Summarize df
    df = dataframe.copy()
    df['Date_Plantation'] = df['Date_Plantation'].dt.to_period('Y').dt.to_timestamp(how='end').dt.normalize()
    summary = df.groupby(['Arrond_Nom', 'Date_Plantation']).size()
    return summary.reset_index(name='Counts')


def restructure_df(yearly_df):
    '''
        Restructures the dataframe into a format easier
        to be displayed as a heatmap.

        The resulting dataframe should have as index
        the names of the neighborhoods, while the columns
        should be each considered year. The values
        in each cell represent the number of trees
        planted by the given neighborhood the given year.

        Any empty cells are filled with zeros.

        Args:
            yearly_df: The dataframe to process
        Returns:
            The restructured dataframe
    '''
    # TODO : Restructure df and fill empty cells with 0
    df_pivoted = yearly_df.pivot(index='Arrond_Nom', columns='Date_Plantation', values='Counts')
    return df_pivoted.fillna(0)

def get_daily_info(dataframe, arrond, year):
    '''
        From the given dataframe, gets
        the daily amount of planted trees
        in the given neighborhood and year.

        Args:
            dataframe: The dataframe to process
            arrond: The desired neighborhood
            year: The desired year
        Returns:
            The daily tree count data for that
            neighborhood and year.
    '''
    # TODO : Get daily tree count data and return
    df = dataframe[dataframe['Arrond_Nom'] == arrond]
    df = df[df['Date_Plantation'].dt.year == year]
    resultat = df.groupby('Date_Plantation').size()
    resultat = resultat.asfreq('D', fill_value=0)
    return resultat.reset_index(name='Counts')

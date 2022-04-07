import pandas as pd
import numpy as np


def combine_by_country(google, admob, facebook, playconsole):
    admob.drop(['App', 'Source', 'Platform', 'Date'], inplace=True, axis=1)
    google.drop('App', inplace=True, axis=1)
    fb_by_country = facebook.groupby('Country').agg('sum')
    google_by_country = google.groupby('Country').agg('sum')
    admob_by_country = admob.groupby('Country').agg('sum')
    playconsole = playconsole[['Country', 'Charged Amount']]
    playconsole = playconsole.groupby('Country').agg('sum')
    combined_on_country = pd.merge(
        admob_by_country, google_by_country, on='Country', how='left')
    combined_on_country = pd.merge(
        combined_on_country, playconsole, on='Country', how='left')
    combined_on_country = pd.merge(
        combined_on_country, fb_by_country, on='Country', how='left')
    combined_on_country.fillna(0, inplace=True)
    combined_on_country['All_Spend'] = combined_on_country['Campaign_Cost'] + \
        combined_on_country['Spend']
    combined_on_country['Revenue'] = combined_on_country['Revenue'] + \
        combined_on_country['Charged Amount']
    combined_on_country['ROI'] = combined_on_country['Revenue'] - \
        combined_on_country['All_Spend']
    combined_on_country['Gain'] = combined_on_country['Revenue'] / \
        combined_on_country['All_Spend']
    combined_on_country = combined_on_country.replace(
        [np.inf, -np.inf], np.nan)
    combined_on_country.fillna(0, inplace=True)
    combined_on_country.drop(['Average_Cpv', 'Average_Cpc',	'Average_Cpe',
                          'Average_Cost', 'Cost_Per_All_Conversions'], inplace=True, axis=1)
    combined_on_country.sort_values(
        by='All_Spend', inplace=True, ascending=False)
    return combined_on_country

import pandas as pd
import numpy as np


def combine_by_app(google, admob, facebook, playconsole):
    admob.drop(['Country', 'Source', 'Platform', 'Date'], inplace=True, axis=1)
    google.drop('Country', inplace=True, axis=1)
    facebook.drop(['Country'], inplace=True, axis=1)
    fb_by_app = facebook.groupby('App').agg('sum')
    google_by_app = google.groupby('App').agg('sum')
    admob_by_app = admob.groupby('App').agg('sum')
    playconsole = playconsole[['App', 'Charged Amount']]
    playconsole = playconsole.groupby('App').agg('sum')
    combined_on_app = pd.merge(
        admob_by_app, google_by_app, on='App', how='right')
    combined_on_app = pd.merge(
        combined_on_app, playconsole, on='App', how='left')
    combined_on_app = pd.merge(
        combined_on_app, fb_by_app, on='App', how='left')
    combined_on_app.fillna(0, inplace=True)
    combined_on_app['Revenue'] = combined_on_app['Revenue'] + \
        combined_on_app['Charged Amount']
    combined_on_app['All_Spend'] = combined_on_app['Campaign_Cost'] + \
        combined_on_app['Spend']
    combined_on_app['ROI'] = combined_on_app['Revenue'] - \
        combined_on_app['All_Spend']
    combined_on_app['Gain'] = combined_on_app['Revenue'] / \
        combined_on_app['All_Spend']
    combined_on_app = combined_on_app.replace([np.inf, -np.inf], np.nan)
    combined_on_app.fillna(0, inplace=True)
    combined_on_app.drop(['Average_Cpv', 'Average_Cpc',	'Average_Cpe',
                          'Average_Cost', 'Cost_Per_All_Conversions'], inplace=True, axis=1)
    combined_on_app.sort_values(by='All_Spend', inplace=True, ascending=False)
    return combined_on_app

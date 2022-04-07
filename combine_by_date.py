from playconsole_sales_parser import sales_parser
from apscheduler.schedulers.blocking import BlockingScheduler
from Google_Ads_Api import ads_data_parser
from Google_Analytics_Api import analytics_data_parser
from Facebook_Api import facebook_data_parser
from Google_Admob_Api import admob_data_parser
import combine_by_app
import combine_by_country
from datetime import date, datetime

import pandas as pd
import time
import os

today_date = datetime.today().strftime("%Y-%m-%d")


def data_joiner_by_app():
    combined_data = pd.read_csv(
        '/home/saadhaxxan/vyroapp/datasheets/Combined_Data_By_App/combined_data_by_app.csv')
    combined_data['Date'] = today_date
    if today_date == '2021-10-04':
        combined_data.to_csv(
            '/home/saadhaxxan/vyroapp/datasheets/Combined_Data_By_Date/combined_data_by_date_app.csv', index=False)
    else:
        combined_data.to_csv(
            '/home/saadhaxxan/vyroapp/datasheets/Combined_Data_By_Date/combined_data_by_date_app.csv', index=False, mode='a', header=False)


def data_joiner_by_country():
    combined_data = pd.read_csv(
        '/home/saadhaxxan/vyroapp/datasheets/Combined_Data_By_Country/combined_data_by_country.csv')
    combined_data['Date'] = today_date
    if today_date == '2021-10-04':
        combined_data.to_csv(
            '/home/saadhaxxan/vyroapp/datasheets/Combined_Data_By_Date/combined_data_by_date_country.csv', index=False)
    else:
        combined_data.to_csv(
            '/home/saadhaxxan/vyroapp/datasheets/Combined_Data_By_Date/combined_data_by_date_country.csv', index=False, mode='a', header=False)


def playconsole_data():
    print("PlayConsole_From_GSUTIL")
    combined_data = pd.read_csv(
        "/home/saadhaxxan/vyroapp/datasheets/PlayConsole_Api/Play_Console_All_Data.csv")
    combined_data['Date'] = today_date
    if today_date == '2021-10-04':
        combined_data.to_csv(
            '/home/saadhaxxan/vyroapp/datasheets/Combined_Data_By_Date/combined_data_by_date_PlayConsole.csv', index=False)
    else:
        combined_data.to_csv(
            '/home/saadhaxxan/vyroapp/datasheets/Combined_Data_By_Date/combined_data_by_date_PlayConsole.csv', index=False, mode='a', header=False)


def fetch_all():
    data_joiner_by_app()
    data_joiner_by_country()
    playconsole_data()


fetch_all()

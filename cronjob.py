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
date = today_date[0:4]+today_date[5:7]+today_date[8:10]


def fetch_ads_data():
    print("Fetching_Ads_job")
    os.system(
        "sudo rm /home/saadhaxxan/vyroapp/datasheets/Google_Ads_Api/Google_Ads_All_Data.csv")
    df = ads_data_parser.fetch_data()
    df.to_csv(
        f"/home/saadhaxxan/vyroapp/datasheets/Google_Ads_Api/{date}_Google_Ads_All_Data.csv", index=False)
    df.to_csv(
        "/home/saadhaxxan/vyroapp/datasheets/Google_Ads_Api/Google_Ads_All_Data.csv", index=False)


def fetch_analytics_data():
    os.system(
        "sudo rm /home/saadhaxxan/vyroapp/datasheets/Google_Analytics_Api/Google_Analytics_All_Data.csv")
    print("Fetching_Analytics_Job")
    appended = False

    app_ids = {
        "AnalyticsAppName": "Appid",
    }

    for idx, value in enumerate(app_ids):
        df = analytics_data_parser.fetch_data(
            value, app_ids[value], "/home/saadhaxxan/vyroapp/Google_Analytics_Api/service_account.json")
        if appended != True:
            df.to_csv(
                f"/home/saadhaxxan/vyroapp/datasheets/Google_Analytics_Api/{date}_Google_Analytics_All_Data.csv", index=False)
            df.to_csv(
                "/home/saadhaxxan/vyroapp/datasheets/Google_Analytics_Api/Google_Analytics_All_Data.csv", index=False)
            appended = True

        elif appended == True:
            df.to_csv(
                f"/home/saadhaxxan/vyroapp/datasheets/Google_Analytics_Api/{date}_Google_Analytics_All_Data.csv", mode="a", index=False, header=False)
            df.to_csv("/home/saadhaxxan/vyroapp/datasheets/Google_Analytics_Api/Google_Analytics_All_Data.csv",
                      mode="a", index=False, header=False)
    print("Fetching_Analytics_Job_Completed")


def fetch_facebook_data():
    print("Fetching_Facebook_Job")
    df = facebook_data_parser.fetch_data()
    df.to_csv(
        f"/home/saadhaxxan/vyroapp/datasheets/Facebook_Ads_Api/{date}_Facebook_Ads_All_Data.csv", index=False)
    df.to_csv(
        "/home/saadhaxxan/vyroapp/datasheets/Facebook_Ads_Api/Facebook_Ads_All_Data.csv", index=False)


def fetch_admob_data():
    print("Fetching_Admob_Job")
    df = admob_data_parser.fetch_data(
        '/home/saadhaxxan/vyroapp/Google_Admob_Api/token.pickle', '/home/saadhaxxan/vyroapp/Google_Admob_Api/credentials.json')
    df.to_csv(
        f"/home/saadhaxxan/vyroapp/datasheets/Google_Admob_Api/{date}_Google_Admob_All_Data.csv", index=False)
    df.to_csv(
        "/home/saadhaxxan/vyroapp/datasheets/Google_Admob_Api/Google_Admob_All_Data.csv", index=False)


def data_joiner_by_app():
    print("Data_Joining_By_App")
    facebook = pd.read_csv(
        "/home/saadhaxxan/vyroapp/datasheets/Facebook_Ads_Api/Facebook_Ads_All_Data.csv")
    google = pd.read_csv(
        "/home/saadhaxxan/vyroapp/datasheets/Google_Ads_Api/Google_Ads_All_Data.csv")
    admob = pd.read_csv(
        "/home/saadhaxxan/vyroapp/datasheets/Google_Admob_Api/Google_Admob_All_Data.csv")
    playconsole = pd.read_csv(
        "/home/saadhaxxan/vyroapp/datasheets/PlayConsole_Api/Play_Console_All_Data.csv")
    by_app = combine_by_app.combine_by_app(
        google, admob, facebook, playconsole)
    by_app.to_csv(
        "/home/saadhaxxan/vyroapp/datasheets/Combined_Data_By_App/combined_data_by_app.csv")
    by_app.to_csv(
        f"/home/saadhaxxan/vyroapp/datasheets/Combined_Data_By_App/{date}_combined_data_by_app.csv")


def data_joiner_by_country():
    print("Joining_By_Country")
    facebook = pd.read_csv(
        "/home/saadhaxxan/vyroapp/datasheets/Facebook_Ads_Api/Facebook_Ads_All_Data.csv")
    google = pd.read_csv(
        "/home/saadhaxxan/vyroapp/datasheets/Google_Ads_Api/Google_Ads_All_Data.csv")
    admob = pd.read_csv(
        "/home/saadhaxxan/vyroapp/datasheets/Google_Admob_Api/Google_Admob_All_Data.csv")
    playconsole = pd.read_csv(
        "/home/saadhaxxan/vyroapp/datasheets/PlayConsole_Api/Play_Console_All_Data.csv")
    by_country = combine_by_country.combine_by_country(
        google, admob, facebook, playconsole)
    by_country.to_csv(
        "/home/saadhaxxan/vyroapp/datasheets/Combined_Data_By_Country/combined_data_by_country.csv")
    by_country.to_csv(
        f"/home/saadhaxxan/vyroapp/datasheets/Combined_Data_By_Country/{date}_combined_data_by_country.csv")


def playconsole_data():
    print("PlayConsole_From_GSUTIL")
    df = sales_parser()
    if not df.empty:
        df.to_csv(
            f"/home/saadhaxxan/vyroapp/datasheets/PlayConsole_Api/{date}_Play_Console_All_Data.csv", index=False)
        df.to_csv(
            "/home/saadhaxxan/vyroapp/datasheets/PlayConsole_Api/Play_Console_All_Data.csv", index=False)


def fetch_all():
    fetch_ads_data()
    fetch_facebook_data()
    fetch_admob_data()
    playconsole_data()
    data_joiner_by_app()
    data_joiner_by_country()
    fetch_analytics_data()
    print("Cronjob Completed\n")


fetch_all()

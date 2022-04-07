from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange
from google.analytics.data_v1beta.types import Dimension
from google.analytics.data_v1beta.types import Metric
from google.analytics.data_v1beta.types import RunReportRequest

import pandas as pd
import numpy as np
import os
import datetime
today_date = datetime.date.today()
yesterday_date = today_date - datetime.timedelta(days=1)
today_date = today_date.strftime("%Y-%m-%d")
yesterday_date = yesterday_date.strftime("%Y-%m-%d")

GOOGLE_APPLICATION_CREDENTIALS_PATH = ""


def fetch_data(app, property_id, credentials_path):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = GOOGLE_APPLICATION_CREDENTIALS_PATH
    client = BetaAnalyticsDataClient()
    request = RunReportRequest(property=f"properties/{property_id}",
                               dimensions=[Dimension(name="country"),
                                           Dimension(name="firstUserMedium")],
                               metrics=[Metric(name="newUsers"),
                                        Metric(name="averageRevenuePerUser"),
                                        Metric(name="totalRevenue"),
                                        Metric(name="purchaseRevenue")],
                               date_ranges=[DateRange(start_date=yesterday_date, end_date=yesterday_date)],)

    response = client.run_report(request)
    df = run_report_response(response, app)
    return df


def run_report_response(response, app):

    totalRevenue = []
    country = []
    averageRevenuePerUser = []
    purchaseRevenue = []
    app_name = []
    organic = []
    cpc = []
    noSource = []
    wishList = []
    notset = []
    others = []
    notification = []
    date = []
    others = []
    data_frame = {}

    for row in response.rows:
        date.append(yesterday_date)
        app_name.append(app)
        for idx, value in enumerate(row.dimension_values):
            if idx == 0:
                if value.value == "United States":
                    country.append("United States of America")
                else:
                    country.append(value.value)
            elif idx == 1:
                if value.value == "organic":
                    organic.append(row.metric_values[0].value)
                    cpc.append(0)
                    noSource.append(0)
                    notification.append(0)
                    wishList.append(0)
                    notset.append(0)
                    others.append(0)
                if value.value == "cpc":
                    cpc.append(row.metric_values[0].value)
                    organic.append(0)
                    noSource.append(0)
                    notification.append(0)
                    wishList.append(0)
                    notset.append(0)
                    others.append(0)
                if value.value == "(none)":
                    noSource.append(row.metric_values[0].value)
                    cpc.append(0)
                    organic.append(0)
                    notification.append(0)
                    wishList.append(0)
                    notset.append(0)
                    others.append(0)
                if value.value == "notification":
                    notification.append(row.metric_values[0].value)
                    cpc.append(0)
                    noSource.append(0)
                    organic.append(0)
                    wishList.append(0)
                    others.append(0)
                    notset.append(0)
                if value.value == "WishList":
                    wishList.append(row.metric_values[0].value)
                    cpc.append(0)
                    noSource.append(0)
                    notification.append(0)
                    organic.append(0)
                    notset.append(0)
                    others.append(0)
                if value.value == "(not set)":
                    notset.append(row.metric_values[0].value)
                    cpc.append(0)
                    noSource.append(0)
                    notification.append(0)
                    wishList.append(0)
                    others.append(0)
                    organic.append(0)
                if value.value == "(other)":
                    others.append(row.metric_values[0].value)
                    cpc.append(0)
                    noSource.append(0)
                    notification.append(0)
                    wishList.append(0)
                    notset.append(0)
                    organic.append(0)
        for idx, value in enumerate(row.metric_values):
            if idx == 1:
                totalRevenue.append(value.value)
            elif idx == 2:
                averageRevenuePerUser.append(value.value)
            elif idx == 3:
                purchaseRevenue.append(value.value)

    for x in range(len(cpc), len(response.rows)):
        others.append(0)
        cpc.append(0)
        noSource.append(0)
        notification.append(0)
        wishList.append(0)
        notset.append(0)
        organic.append(0)

    data = {"Date": date, "App": app_name, "Country": country, "Average_Revenue_Per_User": averageRevenuePerUser,
            "Total_Revenue": totalRevenue, "Purchase_Revenue": purchaseRevenue,
            "Paid_installs": cpc, 'Installs': organic, "No source": noSource,
            'Not Set': notset, "Notifications": notification,
            "WishList": wishList, "(Other)": others}
    data_frame = pd.DataFrame(data)
    return data_frame

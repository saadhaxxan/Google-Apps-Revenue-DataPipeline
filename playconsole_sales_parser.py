import os
import re
import pandas as pd
import numpy as np
import requests
from datetime import datetime, timedelta
from zipfile import ZipFile
import sys
country_abbr = {
    'AD': 'Andorra',
    'AE': 'United Arab Emirates',
    'AF': 'Afghanistan',
    'AG': 'Antigua & Barbuda',
    'AI': 'Anguilla',
    'AL': 'Albania',
    'AM': 'Armenia',
    'AN': 'Netherlands Antilles',
    'AO': 'Angola',
    'AQ': 'Antarctica',
    'AR': 'Argentina',
    'AS': 'American Samoa',
    'AT': 'Austria',
    'AU': 'Australia',
    'AW': 'Aruba',
    'AZ': 'Azerbaijan',
    'BA': 'Bosnia and Herzegovina',
    'BB': 'Barbados',
    'BD': 'Bangladesh',
    'BE': 'Belgium',
    'BF': 'Burkina Faso',
    'BG': 'Bulgaria',
    'BH': 'Bahrain',
    'BI': 'Burundi',
    'BJ': 'Benin',
    'BM': 'Bermuda',
    'BN': 'Brunei Darussalam',
    'BO': 'Bolivia',
    'BR': 'Brazil',
    'BS': 'Bahama',
    'BT': 'Bhutan',
    'BU': 'Burma (no longer exists)',
    'BV': 'Bouvet Island',
    'BW': 'Botswana',
    'BY': 'Belarus',
    'BZ': 'Belize',
    'CA': 'Canada',
    'CC': 'Cocos (Keeling) Islands',
    'CF': 'Central African Republic',
    'CD': 'Congo',
    'CH': 'Switzerland',
    'CI': 'Côte D\'ivoire (Ivory Coast)',
    'CK': 'Cook Iislands',
    'CL': 'Chile',
    'CM': 'Cameroon',
    'CN': 'China',
    'CO': 'Colombia',
    'CR': 'Costa Rica',
    'CS': 'Czechoslovakia (no longer exists)',
    'CU': 'Cuba',
    'CV': 'Cape Verde',
    'CX': 'Christmas Island',
    'CY': 'Cyprus',
    'CZ': 'Czech Republic',
    'DD': 'German Democratic Republic (no longer exists)',
    'DE': 'Germany',
    'DJ': 'Djibouti',
    'DK': 'Denmark',
    'DM': 'Dominica',
    'DO': 'Dominican Republic',
    'DZ': 'Algeria',
    'EC': 'Ecuador',
    'EE': 'Estonia',
    'EG': 'Egypt',
    'EH': 'Western Sahara',
    'ER': 'Eritrea',
    'ES': 'Spain',
    'ET': 'Ethiopia',
    'FI': 'Finland',
    'FJ': 'Fiji',
    'FK': 'Falkland Islands (Malvinas)',
    'FM': 'Micronesia',
    'FO': 'Faroe Islands',
    'FR': 'France',
    'FX': 'France, Metropolitan',
    'GA': 'Gabon',
    'GB': 'United Kingdom',
    'GD': 'Grenada',
    'GE': 'Georgia',
    'GF': 'French Guiana',
    'GH': 'Ghana',
    'GI': 'Gibraltar',
    'GL': 'Greenland',
    'GM': 'Gambia',
    'GN': 'Guinea',
    'GP': 'Guadeloupe',
    'GQ': 'Equatorial Guinea',
    'GR': 'Greece',
    'GS': 'South Georgia and the South Sandwich Islands',
    'GT': 'Guatemala',
    'GU': 'Guam',
    'GW': 'Guinea-Bissau',
    'GY': 'Guyana',
    'HK': 'Hong Kong',
    'HM': 'Heard & McDonald Islands',
    'HN': 'Honduras',
    'HR': 'Croatia',
    'HT': 'Haiti',
    'HU': 'Hungary',
    'ID': 'Indonesia',
    'IE': 'Ireland',
    'IL': 'Israel',
    'IN': 'India',
    'IO': 'British Indian Ocean Territory',
    'IQ': 'Iraq',
    'IR': 'Islamic Republic of Iran',
    'IS': 'Iceland',
    'IT': 'Italy',
    'JM': 'Jamaica',
    'JO': 'Jordan',
    'JP': 'Japan',
    'KE': 'Kenya',
    'KG': 'Kyrgyzstan',
    'KH': 'Cambodia',
    'KI': 'Kiribati',
    'KM': 'Comoros',
    'KN': 'St. Kitts and Nevis',
    'KP': 'Korea, Democratic People\'s Republic of',
    'KR': 'Korea, Republic of',
    'KW': 'Kuwait',
    'KY': 'Cayman Islands',
    'KZ': 'Kazakhstan',
    'LA': 'Lao People\'s Democratic Republic',
    'LB': 'Lebanon',
    'LC': 'Saint Lucia',
    'LI': 'Liechtenstein',
    'LK': 'Sri Lanka',
    'LR': 'Liberia',
    'LS': 'Lesotho',
    'LT': 'Lithuania',
    'LU': 'Luxembourg',
    'LV': 'Latvia',
    'LY': 'Libyan Arab Jamahiriya',
    'MA': 'Morocco',
    'MC': 'Monaco',
    'MD': 'Moldova, Republic of',
    'MG': 'Madagascar',
    'MH': 'Marshall Islands',
    'ML': 'Mali',
    'MN': 'Mongolia',
    'MM': 'Myanmar',
    'MO': 'Macau',
    'MP': 'Northern Mariana Islands',
    'MQ': 'Martinique',
    'MR': 'Mauritania',
    'MS': 'Monserrat',
    'MT': 'Malta',
    'MU': 'Mauritius',
    'MV': 'Maldives',
    'MW': 'Malawi',
    'MX': 'Mexico',
    'MY': 'Malaysia',
    'MZ': 'Mozambique',
    'NA': 'Namibia',
    'NC': 'New Caledonia',
    'NE': 'Niger',
    'NF': 'Norfolk Island',
    'NG': 'Nigeria',
    'NI': 'Nicaragua',
    'NL': 'Netherlands',
    'NO': 'Norway',
    'NP': 'Nepal',
    'NR': 'Nauru',
    'NT': 'Neutral Zone (no longer exists)',
    'NU': 'Niue',
    'NZ': 'New Zealand',
    'OM': 'Oman',
    'PA': 'Panama',
    'PE': 'Peru',
    'PF': 'French Polynesia',
    'PG': 'Papua New Guinea',
    'PH': 'Philippines',
    'PK': 'Pakistan',
    'PL': 'Poland',
    'PM': 'St. Pierre & Miquelon',
    'PN': 'Pitcairn',
    'PR': 'Puerto Rico',
    'PT': 'Portugal',
    'PW': 'Palau',
    'PY': 'Paraguay',
    'QA': 'Qatar',
    'RE': 'Réunion',
    'RO': 'Romania',
    'RU': 'Russian Federation',
    'RW': 'Rwanda',
    'SA': 'Saudi Arabia',
    'SB': 'Solomon Islands',
    'SC': 'Seychelles',
    'SD': 'Sudan',
    'SE': 'Sweden',
    'SG': 'Singapore',
    'SH': 'St. Helena',
    'SI': 'Slovenia',
    'SJ': 'Svalbard & Jan Mayen Islands',
    'SK': 'Slovakia',
    'SL': 'Sierra Leone',
    'SM': 'San Marino',
    'SN': 'Senegal',
    'SO': 'Somalia',
    'SR': 'Suriname',
    'ST': 'Sao Tome & Principe',
    'SU': 'Union of Soviet Socialist Republics (no longer exists)',
    'SV': 'El Salvador',
    'SY': 'Syrian Arab Republic',
    'SZ': 'Swaziland',
    'TC': 'Turks & Caicos Islands',
    'TD': 'Chad',
    'TF': 'French Southern Territories',
    'TG': 'Togo',
    'TH': 'Thailand',
    'TJ': 'Tajikistan',
    'TK': 'Tokelau',
    'TM': 'Turkmenistan',
    'TN': 'Tunisia',
    'TO': 'Tonga',
    'TP': 'East Timor',
    'TR': 'Turkey',
    'TT': 'Trinidad & Tobago',
    'TV': 'Tuvalu',
    'TW': 'Taiwan, Province of China',
    'TZ': 'Tanzania, United Republic of',
    'UA': 'Ukraine',
    'UG': 'Uganda',
    'UM': 'United States Minor Outlying Islands',
    'US': 'United States of America',
    'UY': 'Uruguay',
    'UZ': 'Uzbekistan',
    'VA': 'Vatican City State (Holy See)',
    'VC': 'St. Vincent & the Grenadines',
    'VE': 'Venezuela',
    'VG': 'British Virgin Islands',
    'VI': 'United States Virgin Islands',
    'VN': 'Viet Nam',
    'VU': 'Vanuatu',
    'WF': 'Wallis & Futuna Islands',
    'WS': 'Samoa',
    'YD': 'Democratic Yemen (no longer exists)',
    'YE': 'Yemen',
    'YT': 'Mayotte',
    'YU': 'Yugoslavia',
    'ZA': 'South Africa',
    'ZM': 'Zambia',
    'ZR': 'Zaire',
    'ZW': 'Zimbabwe',
    'ZZ': 'Unknown or unspecified country',
}

app_names = {
    'AppNameInPlayConsole': 'Name to store in CSV',
}


def sub_type(val):
    if 'yearly' in val:
        val = 'yearly'
    elif 'weekly' in val:
        val = 'weekly'
    else:
        val = 'monthly'
    return val


def to_timestamp(val):
    tmstp = datetime.fromtimestamp(val).strftime('%Y-%m-%d %H:%M:%S')
    return tmstp


def sales_parser():

    itemPrice = []
    taxesCollected = []
    productName = []
    country = []
    now = datetime.now()
    month = now.strftime("%m")
    prev_month = (now - timedelta(days=30)).strftime("%m")

    try:
        command = f"/home/saadhaxxan/google-cloud-sdk/google-cloud-sdk/bin/gsutil cp -r Your sales report from google cloud storage{month}.zip /home/saadhaxxan/vyroapp/"
        os.system(command)
    except Exception as e:
        print("No sales report for this month")
    finally:
        command = f"/home/saadhaxxan/google-cloud-sdk/google-cloud-sdk/bin/gsutil cp -r Your sales report from google cloud storage{prev_month}.zip /home/saadhaxxan/vyroapp/"
        os.system(command)

    if os.path.exists(f"/home/saadhaxxan/vyroapp/salesreport_2021{month}.zip"):
        with ZipFile(f'/home/saadhaxxan/vyroapp/salesreport_2021{month}.zip', 'r') as zipObj:
            zipObj.extractall()
    else:
        with ZipFile(f'/home/saadhaxxan/vyroapp/salesreport_2021{prev_month}.zip', 'r') as zipObj:
            zipObj.extractall()
    if os.path.exists(f"/home/saadhaxxan/vyroapp/salesreport_2021{month}.csv"):
        report = pd.read_csv(
            f"/home/saadhaxxan/vyroapp/salesreport_2021{month}.csv")
    else:
        report = pd.read_csv(
            f"/home/saadhaxxan/vyroapp/salesreport_2021{prev_month}.csv")
    df = pd.DataFrame(report)
    df = df[df["Financial Status"] == "Charged"]
    df = df[df["Order Charged Date"] == datetime.today().strftime('%Y-%m-%d')]
    df = df[["Order Charged Date", "Order Charged Timestamp", "Product ID", "Product Type", "Currency of Sale",
             "Item Price", "Taxes Collected", "Country of Buyer", "SKU ID"]]
    items = df["Item Price"]
    taxes = df["Taxes Collected"]
    products = df["Product ID"]
    df["Country of Buyer"] = df["Country of Buyer"].fillna('ZZ')
    country_codes = df["Country of Buyer"]

    for price in items:
        price = price.split(',')
        price = ''.join(price)
        itemPrice.append(price)

    for tax in taxes:
        tax = tax.split(',')
        tax = ''.join(tax)
        taxesCollected.append(tax)

    for product in products:
        product = product.split('.')
        productName.append(app_names[product[2]])

    for code in country_codes:
        country.append(country_abbr[code])

    df["Item Price"] = itemPrice
    df["Taxes Collected"] = taxesCollected
    df["App"] = productName
    df["Country"] = country
    df['sub_type'] = df['SKU ID'].apply(sub_type)
    df['Taxes Collected'] = df['Taxes Collected'].astype('float')
    df['Item Price'] = df['Item Price'].astype('float')
    df["Charged Amount"] = df["Item Price"] - df["Taxes Collected"]
    df['Timestamp'] = df['Order Charged Timestamp'].apply(to_timestamp)
    df = df.drop(columns=["Item Price", "Taxes Collected",
                          "Product ID", "Country of Buyer"])

    symbols = list(df["Currency of Sale"])
    symbols = ' '.join(map(str, symbols))
    symbols = symbols.replace(" ", ",")
    response = requests.get(
        "http://data.fixer.io/api/latest?access_key=YOUR_ACCESSKEY&format=1&base=USD&symbols="+symbols).json()
    rates = response["rates"]
    currencies = df["Currency of Sale"]
    native_amount = list(df["Charged Amount"])

    amount_in_dollors = []
    for it, currency in enumerate(currencies):
        amount_in_dollors.append(native_amount[it]/rates[currency])

    df = df.drop(columns=["Currency of Sale", "Charged Amount"])
    df["Charged Amount"] = amount_in_dollors

    return df

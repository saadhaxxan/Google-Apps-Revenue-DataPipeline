import pandas as pd
import os
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import datetime

PUBLISHER_ID = 'YourPublisherID'
API_NAME = 'admob'
API_VERSION = 'v1'
API_SCOPE = 'https://www.googleapis.com/auth/admob.readonly'


def country_list():
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
    return country_abbr


def generate_mediation_report(service, publisher_id):

    dt = datetime.date.today()

    date_range = {
        'start_date': {'year': dt.year, 'month': dt.month, 'day': (dt.day)},
        'end_date': {'year': dt.year, 'month': dt.month, 'day': (dt.day)}
    }

    # Set dimensions.
    dimensions = ['DATE', 'APP', 'COUNTRY', "AD_SOURCE", "PLATFORM"]

    # Set metrics.
    metrics = ['ESTIMATED_EARNINGS', 'OBSERVED_ECPM']

    # Set sort conditions.
    sort_conditions = {'dimension': 'DATE', 'order': 'DESCENDING'}

    country_codes = []
    country_abbr = country_list()
    for key in country_abbr:
        country_codes.append(key)
    # Set dimension filters.
    dimension_filters = {
        'dimension': 'COUNTRY',
        'matches_any': {
            'values': country_codes
        }
    }

    # Create mediation report specifications.
    report_spec = {
        'date_range': date_range,
        'dimensions': dimensions,
        'metrics': metrics,
        'sort_conditions': [sort_conditions],
        'dimension_filters': [dimension_filters]
    }

    # Create mediation report request.
    request = {'report_spec': report_spec}

    # Execute mediation report request.
    response = service.accounts().mediationReport().generate(
        parent='accounts/{}'.format(publisher_id), body=request).execute()

    return response


def load_user_credentials(credentials_file):
    client_secrets = os.path.join(
        os.path.dirname(__file__), credentials_file)  # 'credentials.json'
    return client_secrets


def authenticate(token_file, credentials_file):

    TOKEN_FILE = token_file  # 'token.pickle'
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            credentials = pickle.load(token)

        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())

    # If there are no valid stored credentials, authenticate using the
    # client_secrets file.
    else:
        client_secrets = load_user_credentials(credentials_file)
        flow = InstalledAppFlow.from_client_secrets_file(
            client_secrets,
            scopes=[API_SCOPE],
            redirect_uri='urn:ietf:wg:oauth:2.0:oob')

        # Redirect the user to auth_url on your platform.
        auth_url, _ = flow.authorization_url()
        print('Please go to this URL: {}\n'.format(auth_url))

        # The user will get an authorization code. This code is used to get the
        # access token.
        code = input('Enter the authorization code: ')
        flow.fetch_token(code=code)
        credentials = flow.credentials

    # Save the credentials for the next run.
        with open('token.pickle', 'wb') as token:
            pickle.dump(credentials, token)

    # Build the AdMob service.
    admob = build(API_NAME, API_VERSION, credentials=credentials)
    return admob


def fetch_data(token_file, credentials_file):
    all_data = []
    date = []
    app = []
    country = []
    platform = []
    ad_source = []
    estimated_earnings = []
    observed_ecpm = []
    micro = 1000000
    required = False

    service = authenticate(token_file, credentials_file)
    response = generate_mediation_report(service, PUBLISHER_ID)

    for report in response:
        all_data.append(report)

    rows = {"rows": all_data[1:-1]}

    for idx, values in enumerate(rows["rows"]):
        app_name = ""
        required = False
        res_app_name = rows["rows"][idx]["row"]["dimensionValues"]["APP"]["displayLabel"]
        date_ = rows["rows"][idx]["row"]["dimensionValues"]["DATE"]["value"]
        final_date = date_[0:4] + "-" + date_[4:6] + "-" + date_[6:8]
        date.append(final_date)
        ad_source.append(rows["rows"][idx]["row"]
                         ["dimensionValues"]["AD_SOURCE"]["displayLabel"])
        platform.append(
            (rows["rows"][idx]["row"]["dimensionValues"]["PLATFORM"]["value"]))
        app.append(res_app_name)
        country_abbr = country_list()
        country.append(
            country_abbr[rows["rows"][idx]["row"]["dimensionValues"]["COUNTRY"]["value"]])
        estimated_earnings.append(float(
            rows["rows"][idx]["row"]["metricValues"]["ESTIMATED_EARNINGS"]["microsValue"])/micro)
        observed_ecpm.append(float(
            rows["rows"][idx]["row"]["metricValues"]["OBSERVED_ECPM"]["microsValue"])/micro)

    data_frame = {"Date": date,  "Revenue": estimated_earnings, "ECPM": observed_ecpm,
                  "App": app, "Platform": platform, "Source": ad_source, "Country": country}
    df = pd.DataFrame(data_frame)
    return df

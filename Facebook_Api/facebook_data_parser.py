import pandas as pd
from datetime import date
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adsinsights import AdsInsights
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
import time


def country_list():
    country_abbr = {
        'WW': 'World Wide',
        'BQ': 'Bonaire',
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
        'GER': 'Germany',
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


def connector():
    my_app_id = 'YourAppId'
    my_app_secret = 'YourAppSecret'
    my_access_token = 'YourAccessToken'
    FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
    my_account = AdAccount('YourAdAccountID')

    params = {
        'effective_status': ['ACTIVE'],
        'date_preset': 'today',
        'breakdowns': ['country'],
        'level': 'campaign',
    }

    fields = [
        AdsInsights.Field.spend,
        AdsInsights.Field.campaign_name,

    ]

    campaigns = my_account.get_campaigns(
        fields=fields,
        params=params,
    )

    insights = []

    for campaign in campaigns:
        c_id = campaign['id']
        campaign = Campaign(c_id)
        insights.append(campaign.get_insights(fields=fields, params=params))
    return insights


def fetch_data():
    spend = []
    country = []
    app = []
    app_names = [
        "Your Campaign Identifiers in a list"
    ]

    required = False
    insights = connector()

    for record in insights:
        required = False
        app_name = ''

        for rec in record:

            res = rec['campaign_name']
            app_name = res.split('_')[0]

            for name in app_names:
                if app_name == name:
                    required = True

            if required == True:
                app.append(app_name)
                country_abbr = country_list()

                if res.split('_')[1] == "DE":
                    country_name = "GER"
                else:
                    country_name = res.split('_')[1]

                country.append(country_abbr.get(
                    country_name, "Wrong Country name"))
                spend.append(rec['spend'])

    df_dict = {'App': app, 'Country': country, 'Spend': spend, }
    df = pd.DataFrame(df_dict)
    return df

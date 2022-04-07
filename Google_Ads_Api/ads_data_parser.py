import pandas as pd
from google.ads.googleads.client import GoogleAdsClient
from datetime import datetime

today_date = datetime.today().strftime("%Y-%m-%d")
customer_id = "YourCustomerID"


def country_list():
    country_abbr = {
        'NotDefined': 'NAN',
        'WW': 'World Wide',
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
        'UK': 'United Kingdom',
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


def fetch_data():
    googleads_client = GoogleAdsClient.load_from_storage(version="v8")
    cost_per_all_conversions = []
    average_cost = []
    all_conversions = []
    all_conversions_value = []
    campaign_name = []
    date = []
    average_cpv = []
    average_cpc = []
    average_cpe = []
    cost = []
    campaign_id = []
    country_name = []
    app_name = []

    ga_service = googleads_client.get_service("GoogleAdsService")

    query = f"""
        SELECT segments.date, campaign.id, campaign.name, campaign.status, metrics.average_cpv, metrics.average_cpe, metrics.average_cpc, campaign.start_date, 
        metrics.cost_per_all_conversions,metrics.average_cost, metrics.all_conversions, metrics.cost_micros,
        metrics.all_conversions_value FROM campaign_budget WHERE segments.date = '{today_date}' AND campaign.status = "ENABLED"
        """

    # Issues a search request using streaming.
    response = ga_service.search_stream(customer_id=customer_id, query=query)
    actual_cost = []

    for batch in response:
        for row in batch.results:
            campaign = row.campaign.name
            campaign = campaign.split("_")
            country = campaign[1]
            app_name.append(campaign[0])
            list = country_list()
            country_name.append(list[country])
            date.append(datetime.today().strftime('%Y-%m-%d'))
            campaign_name.append(row.campaign.name)
            campaign_id.append(row.campaign.id)
            average_cpv.append(row.metrics.average_cpv)
            average_cpc.append(row.metrics.average_cpc)
            average_cpe.append(row.metrics.average_cpe)
            actual_cost = row.metrics.cost_micros / 1000000
            cost.append(actual_cost)
            all_conversions.append(row.metrics.cost_per_all_conversions)
            all_conversions_value.append(row.metrics.all_conversions_value)
            average_cost.append(row.metrics.average_cost)
            cost_per_all_conversions.append(
                row.metrics.cost_per_all_conversions)

    df_dict = {
        "Campaign_id": campaign_id,
        "Date": date,
        "App": app_name,
        "Campaign_Name": campaign_name,
        "Campaign_Cost": cost,
        "Country": country_name,
        "Average_Cpv": average_cpv,
        "Average_Cpc": average_cpc,
        "Average_Cpe": average_cpe,
        "Average_Cost": average_cost,
        "All_Conversions_Value": all_conversions_value,
        "Cost_Per_All_Conversions": all_conversions,
    }
    date = today_date[0:4] + today_date[5:7] + today_date[8:10]
    df = pd.DataFrame(df_dict)
    df = df.set_index(df["Campaign_id"])
    return df


if __name__ == "__main__":
    fetch_data()
